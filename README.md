# Python Mocking POC
This proof of concept is set around 3 objectives:
- basic mocking example in Python
- determing code coverage stats using the Coverage.py module
- implement a basic code quality gating mechanism.


## Mocking
The mocking example is based on the YouTube module from Red Eye Coder Club:
https://www.youtube.com/watch?v=xT4SV7AH3G8&t=97s

Here the idea is how to implement `patch` and how to mock out a 3rd party API.


## Code Coverage Stats
Code coverage stats are built on the fly using Coverage.py and GitHub Actions.  Documentation on Coverage.py can be found at : https://coverage.readthedocs.io/en/6.4.1/

Generating the coverage report can be seen in the pipeline steps: https://github.com/AnnawanDev/Python-Mocking-POC/blob/main/.github/workflows/pipeline_with_code_coverage.yml#L43-L52


### Code Quality Gating
The idea of a code quality gate is that if a certain threshold of code quality is not met, then the build fails; otherwise, it passes.

Based on having already run the code coverage, the exact percentage is isolated with the help of [jq](https://stedolan.github.io/jq/) in the steps: https://github.com/AnnawanDev/Python-Mocking-POC/blob/main/.github/workflows/pipeline_with_code_coverage.yml#L54-L59 

It then determines whether that code coverage value is above the threshold (here set to 80) or below.  If it's at 80 or above, it passes; otherwise, the build fails.  https://github.com/AnnawanDev/Python-Mocking-POC/blob/main/.github/workflows/pipeline_with_code_coverage.yml#L62-L69


## Reference & Further reading for fun
* A Quick Intro to Test Coverage in Python : https://python.plainenglish.io/a-quick-intro-to-to-test-coverage-in-python-9bf299711c6c
* jq: https://stedolan.github.io/jq/
* GitHub Actions environment variables: https://docs.github.com/en/actions/learn-github-actions/environment-variables
* Workflow commands in GitHub Actions: https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions
* YAML checker: https://yamlchecker.com/
* Mocking APIs in Python: https://realpython.com/testing-third-party-apis-with-mocks/
