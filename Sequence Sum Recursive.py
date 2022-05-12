def sequence_sum(begin, end, step):
    return 0 if begin>end else begin+sequence_sum(begin+step,end, step)