#pragma once
#include <cstdarg>
namespace Eloquent {
    namespace ML {
        namespace Port {
            class DecisionTree {
                public:
                    /**
                    * Predict class for features vector
                    */
                    int predict(float *x) {
                        if (x[2] <= 0.1577478125691414) {
                            if (x[2] <= 0.07133215665817261) {
                                return 0;
                            }

                            else {
                                return 0;
                            }
                        }

                        else {
                            if (x[2] <= 0.33722373843193054) {
                                return 1;
                            }

                            else {
                                return 1;
                            }
                        }
                    }

                protected:
                };
            }
        }
    }