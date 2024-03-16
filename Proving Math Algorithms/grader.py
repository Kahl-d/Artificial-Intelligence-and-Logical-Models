#!/usr/bin/env python3

from logic import *

import pickle, gzip, os, random
import grader_util

grader = grader_util.Grader()
submission = grader.load('submission')

# name: name of this formula (used to load the models)
# predForm: the formula predicted in the submission
# preconditionForm: only consider models such that preconditionForm is true
def checkFormula(name, predForm, preconditionForm=None, handle_grader=True):
    filename = os.path.join('models', name + '.pklz')
    objects, targetModels = pickle.load(gzip.open(filename))
    # If preconditionion exists, change the formula to
    preconditionPredForm = And(preconditionForm, predForm) if preconditionForm else predForm
    predModels = performModelChecking([preconditionPredForm], findAll=True, objects=objects)
    ok = True
    def hashkey(model): return tuple(sorted(str(atom) for atom in model))
    targetModelSet = set(hashkey(model) for model in targetModels)
    predModelSet = set(hashkey(model) for model in predModels)
    for model in targetModels:
        if hashkey(model) not in predModelSet:
            if handle_grader:
                grader.fail("Your formula (%s) says the following model is FALSE, but it should be TRUE:" % predForm)
            ok = False
            printModel(model)
            return ok
    for model in predModels:
        if hashkey(model) not in targetModelSet:
            if handle_grader:
                grader.fail("Your formula (%s) says the following model is TRUE, but it should be FALSE:" % predForm)
            ok = False
            printModel(model)
            return ok
    if handle_grader:
        grader.add_message('You matched the %d models' % len(targetModels))
        grader.add_message('Example model: %s' % rstr(random.choice(targetModels)))
        grader.assign_full_credit()
    return ok

# name: name of this formula set (used to load the models)
# predForms: formulas predicted in the submission
# predQuery: query formula predicted in the submission
def addParts(name, numForms, predictionFunc):
    # part is either an individual formula (0:numForms), all (combine everything)
    def check(part):
        predForms, predQuery = predictionFunc()
        if len(predForms) < numForms:
            grader.fail("Wanted %d formulas, but got %d formulas:" % (numForms, len(predForms)))
            for form in predForms: print(('-', form))
            return
        if part == 'all':
            checkFormula(name + '-all', AndList(predForms))
        elif part == 'run':
            # Actually run it on a knowledge base
            kb = createModelCheckingKB()

            # Need to tell the KB about the objects to do model checking
            filename = os.path.join('models', name + '-all.pklz')
            objects, targetModels = pickle.load(gzip.open(filename))
            for obj in objects:
                kb.tell(Atom('Object', obj))

            # Add the formulas
            for predForm in predForms:
                response = kb.tell(predForm)
                showKBResponse(response)
                grader.require_is_true(response.status in [CONTINGENT, ENTAILMENT])
            response = kb.ask(predQuery)
            showKBResponse(response)

        else:  # Check the part-th formula
            checkFormula(name + '-' + str(part), predForms[part])

    def createCheck(part): return lambda : check(part)  # To create closure

    # run part-all once first for combined correctness, if true, trivially assign full score for all subparts
    # this is to account for student adding formulas to the list in different orders but still get
    # the combined preds correct.
    all_is_correct = False
    try:
        predForms, predQuery = predictionFunc()
        all_is_correct = checkFormula(name + '-all', AndList(predForms), handle_grader=False)
    except BaseException:
        pass

    for part in list(range(numForms)) + ['all', 'run']:
        if part == 'all':
            description = 'test implementation of %s for %s' % (part, name)
        elif part == 'run':
            description = 'test implementation of %s for %s' % (part, name)
        else:
            description = 'test implementation of statement %s for %s' % (part, name)
        if all_is_correct and not part in ['all', 'run']:
            grader.add_basic_part(name + '-' + str(part), lambda : grader.assign_full_credit(), max_points=1, max_seconds=10000, description=description)
        else:
            grader.add_basic_part(name + '-' + str(part), createCheck(part), max_points=1, max_seconds=10000, description=description)

############################################################
# Problem 4: odd and even integers

# Add 5a-[0-5], 5a-all, 5a-run
addParts('4a', 6, submission.ints)


grader.grade()
