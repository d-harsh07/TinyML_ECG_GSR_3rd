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
                        if (x[3] <= 165.63500213623047) {
                            return 0;
                        }

                        else {
                            return 1;
                        }
                    }

                protected:
                };
            }
        }
    }