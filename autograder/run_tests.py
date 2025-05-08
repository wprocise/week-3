import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')

    # Get a default output from the results file
    output = '''
    When you're ready, make sure to submit your code for review on Canvas!
    '''

    # Run the tests and write the results to /autograder/results/results.json
    with open('/autograder/results/results.json', 'w') as f:
        runner = JSONTestRunner(stream=f, 
                                verbosity=2, 
                                buffer=True, 
                                visibility="visible")
        
        runner.json_data['output'] = output
        runner.run(suite)