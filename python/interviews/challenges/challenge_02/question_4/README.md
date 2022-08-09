##Question 4
Package your code into a python package to make it easily installable and testable for developers.

##Solution

1. Go to `./question_4/setup_package` directory to set as root directory.
2. To build the package:
   - `python setup.py build --build-base ./packages/ egg_info --egg-base ./packages/ bdist_wheel --dist-dir ./packages/`
3. To install package:
   - `pip install ./packages/challenge02package-0.1.0-py3-none-any.whl`
4. To test the api package:
   - `python ../main_app.py`
   - Same testing/checking process as question 3
5. Test the model and see the benchmark run package:
   - `python ../main_regression.py`
6. `pip uninstall challenge02package --yes` When package is no longer required.