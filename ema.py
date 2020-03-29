def ema(L, alpha=None):
    """
       here we use 'exponential moving average' to predict the next time period data value
    # EMA Formula:
         X(0),X(1),X(2),...,X(t-1) : data-sets total with "t" time-period-points
         EMA(1) = X(0) // initial point            -> 1 terms
         EMA(2) = EMA(1) + alpha*(X(1)-EMA(1))
                = alpha*[X(1)] + (1-alpha)*X(0)    -> 2 terms
         EMA(3) = EMA(2) + alpha*[X(2)-EMA(2)]
                = [alpha*X(1)+(1-alpha)*X(0)] + alpha*[X(2)-(alpha*X(1)+(1-alpha)*X(0))]
                = alpha*[X(2)+(1-alpha)*X(1)] + (1-alpha-alpha-alpha^2)*X(0)
                = alph*[X(2)+(1-alpha)*X(1)] + (1-alpha)^2*X(0)     -> 3 terms
           .
           .
         EMA(t) = alpha*X(t-1) + (1-alpha)*EMA(t-1) = EMA(t-1) + alpha*[X(t-1) - EMA(t-1)]
                  = ...
                                    1st               2nd                     3rd                            (t-1)-th
                  = alpha*[ (1-alpha)^(0)*X(t-1) + (1-alpha)^(1)*X(t-2) + (1-alpha)^(2)*X(t-3) + ...+ (1-alpha)^(t-2)*X(t-(t-1)) ]
                            t-th
                    + (1-alpha)^(t-1)*X(0)
         alpha = 1 /(number of data-points)
         where alpha: smoothing factor
               X(t-1) is observation value at time (t-1) period
               EMA(t-1) is prediction value at time (t-1) periods
               EMA(t) is prediction value at time t periods
    """
    ema_data = []
    if not alpha:
        alpha = 1 / (len(L) + 1.25)  # defaults
    if (alpha < 0) or (alpha > 1):
        raise ValueError("0 < smoothing factor <= 1")
    alpha_bar = float(1 - alpha)

    """ generate [x(0)], [x(1),x(0)], [x(2),x(1),x(0)],.... """
    num_terms_list = [sorted(L[:i], reverse=True) for i in range(1, len(L) + 1)]
    # print num_terms_list
    # return
    for nterms in num_terms_list:
        # calculate 1st~(t-1)-th terms corresponding exponential factor
        pre_exp_factor = [float(alpha_bar ** (i - 1)) for i in range(1, len(nterms))]
        # calculate the ema at the next time periods
        ema_data.append(
            alpha * float(sum(float(a) * float(b) for a, b in zip(tuple(pre_exp_factor), tuple(nterms[:-1])))) + \
            (alpha_bar ** (len(nterms) - 1)) * float(nterms[-1]))
    return ema_data


# if __name__ == "__main__":
    # this is your code
#data = [97.6, 95.1, 90.3, 92.5, 89.8, 92.7, 94.4, 96.2]
#data = [i for i in range(0, 10)]
# print ("data=%s" % data)
# print ("ema=%s" % ema(data, 0.5))