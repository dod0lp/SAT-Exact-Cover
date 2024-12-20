c
c This is glucose 4.1 --  based on MiniSAT (Many thanks to MiniSAT team)
c
c ========================================[ Problem Statistics ]===========================================
c |                                                                                                       |
c |  Number of variables:             6                                                                   |
c |  Number of clauses:              21                                                                   |
c |  Parse time:                   0.00 s                                                                 |
c |                                                                                                       |
c | Preprocesing is fully done
c |  Eliminated clauses:           0.00 Mb                                                                |
c |  Simplification time:          0.00 s                                                                 |
c |                                                                                                       |
c ========================================[ MAGIC CONSTANTS ]==============================================
c | Constants are supposed to work well together :-)                                                      |
c | however, if you find better choices, please let us known...                                           |
c |-------------------------------------------------------------------------------------------------------|
c | Adapt dynamically the solver after 100000 conflicts (restarts, reduction strategies...)               |
c |-------------------------------------------------------------------------------------------------------|
c |                                |                                |                                     |
c | - Restarts:                    | - Reduce Clause DB:            | - Minimize Asserting:               |
c |   * LBD Queue    :     50      |   * First     :   2000         |    * size <  30                     |
c |   * Trail  Queue :   5000      |   * Inc       :    300         |    * lbd  <   6                     |
c |   * K            :   0.80      |   * Special   :   1000         |                                     |
c |   * R            :   1.40      |   * Protected :  (lbd)< 30     |                                     |
c |                                |                                |                                     |
c ==================================[ Search Statistics (every  10000 conflicts) ]=========================
c |                                                                                                       |
c |          RESTARTS           |          ORIGINAL         |              LEARNT              | Progress |
c |       NB   Blocked  Avg Cfc |    Vars  Clauses Literals |   Red   Learnts    LBD2  Removed |          |
c =========================================================================================================
c last restart ## conflicts  :  0 0 
c =========================================================================================================
c restarts              : 1 (0 conflicts in avg)
c blocked restarts      : 0 (multiple: 0) 
c last block at restart : 0
c nb ReduceDB           : 0
c nb removed Clauses    : 0
c nb learnts DL2        : 0
c nb learnts size 2     : 0
c nb learnts size 1     : 0
c conflicts             : 0              (nan /sec)
c decisions             : 1              (0.00 % random) (inf /sec)
c propagations          : 5              (inf /sec)
c nb reduced Clauses    : 0
c CPU time              : 0 s

s SATISFIABLE
v -1 2 -3 4 -5 6 0
