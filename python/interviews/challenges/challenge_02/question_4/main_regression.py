from challenge02package.utils import simple_linear_regr, benchmark

if __name__ == '__main__':
    print('Running model')
    simple_linear_regr.make_model(evaluate_flag=True)
    print('Running benchmark')
    benchmark.run_benchmark()
