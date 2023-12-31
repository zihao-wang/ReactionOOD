Leaderboard
==============

In this new leaderboard, hyperparameter spaces are larger, and all hyperparameters are selected according to 3-run
average performance. The hyperparameter searching spaces can be found at `sweep_configs <https://github.com/divelab/GOOD/tree/GOODv1/configs/sweep_configs>`_,
and the chosen hyperparameters are listed in `final_configs <https://github.com/divelab/GOOD/tree/GOODv1/configs/final_configs>`_.
All OOD test results are obtained by 10 runs according to OOD validation set. Values in parenthesis are standard deviations.
We use bold to denote the best results. -(-) denotes abnormal results caused by under-fitting.

Graph-level
------------



..  table::
    :widths: auto
    :class: std-table-style

    +------------+-----------------------------------+-----------------------------------+
    |            | basis                             | size                              |
    |GOOD-Motif  +-----------------+-----------------+-----------------+-----------------+
    |            | covariate       | concept         | covariate       | concept         |
    +============+=================+=================+=================+=================+
    | ERM        | 63.80(10.36)    | 81.31(0.69)     | 53.46(4.08)     | **70.83(0.79)** |
    +------------+-----------------+-----------------+-----------------+-----------------+
    | IRM        | 59.93(11.46)    | 80.37(0.80)     | 53.68(4.11)     | 70.15(0.64)     |
    +------------+-----------------+-----------------+-----------------+-----------------+
    | VREx       | 66.53(4.04)     | 81.34(0.75)     | 54.47(3.42)     | 70.58(1.16)     |
    +------------+-----------------+-----------------+-----------------+-----------------+
    | GroupDRO   | 61.96(8.27)     | 81.00(0.60)     | 51.69(2.22)     | 70.35(0.40)     |
    +------------+-----------------+-----------------+-----------------+-----------------+
    | Coral      | 66.23(9.01)     | 81.47(0.49)     | 53.71(2.75)     | 70.52(0.59)     |
    +------------+-----------------+-----------------+-----------------+-----------------+
    | DANN       | 51.54(7.28)     | 81.43(0.60)     | 51.86(2.44)     | 70.74(0.65)     |
    +------------+-----------------+-----------------+-----------------+-----------------+
    | Mixup      | **69.67(5.86)** | 77.64(0.58)     | 51.31(2.56)     | 68.21(0.89)     |
    +------------+-----------------+-----------------+-----------------+-----------------+
    | DIR        | 39.99(5.50)     | **82.96(4.47)** | 44.83(4.00)     | 54.96(9.32)     |
    +------------+-----------------+-----------------+-----------------+-----------------+
    | GSAT       | 55.13(5.41)     | 75.30(1.57)     | **60.76(5.94)** | 59.00(3.42)     |
    +------------+-----------------+-----------------+-----------------+-----------------+
    | CIGAv1     | 66.43(11.31)    | 72.5(4.02)      | 49.14(8.34)     | 58.63(6.66)     |
    +------------+-----------------+-----------------+-----------------+-----------------+
    | CIGAv2     | 67.15(8.19)     | 77.48(2.54)     | 54.42(3.11)     | 70.65(4.81)     |
    +------------+-----------------+-----------------+-----------------+-----------------+



..  table::
    :widths: auto
    :class: std-table-style

    +-------------+-----------------------------------------+
    |             | color                                   |
    | GOOD-CMNIST +--------------------+--------------------+
    |             | covariate          | concept            |
    +=============+====================+====================+
    | ERM         | 27.82(3.24)        | 42.90(0.67)        |
    +-------------+--------------------+--------------------+
    | IRM         | 29.04(2.10)        | 42.73(0.71)        |
    +-------------+--------------------+--------------------+
    | VREx        | 27.65(2.31)        | 43.22(0.64)        |
    +-------------+--------------------+--------------------+
    | GroupDRO    | 29.23(2.12)        | 43.33(0.67)        |
    +-------------+--------------------+--------------------+
    | Coral       | 29.47(3.15)        | 42.98(0.59)        |
    +-------------+--------------------+--------------------+
    | DANN        | 28.77(1.49)        | 42.84(0.61)        |
    +-------------+--------------------+--------------------+
    | Mixup       | 28.30(1.74)        | 40.70(0.56)        |
    +-------------+--------------------+--------------------+
    | DIR         | 26.20(4.48)        | 28.71(4.66)        |
    +-------------+--------------------+--------------------+
    | GSAT        |  **35.62(5.52)**   | **47.58(1.15)**    |
    +-------------+--------------------+--------------------+
    | CIGAv1      | 32.22(2.67)        | 34.80(3.33)        |
    +-------------+--------------------+--------------------+
    | CIGAv2      | 32.11(2.53)        | 39.39(3.3)         |
    +-------------+--------------------+--------------------+


..  table::
    :widths: auto
    :class: std-table-style

    +----------+-----------------------------------+-----------------------------------+
    |          | scaffold                          | size                              |
    |GOOD-HIV  +-----------------+-----------------+-----------------+-----------------+
    |          | covariate       | concept         | covariate       | concept         |
    +==========+=================+=================+=================+=================+
    | ERM      | 69.55(2.39)     | 72.48(1.26)     | 59.19(2.29)     | 61.91(2.29)     |
    +----------+-----------------+-----------------+-----------------+-----------------+
    | IRM      | 70.17(2.78)     | 71.78(1.37)     | 59.94(1.59)     | -(-)            |
    +----------+-----------------+-----------------+-----------------+-----------------+
    | VREx     | 69.34(3.54)     | 72.21(1.42)     | 58.49(2.28)     | 61.21(2.00)     |
    +----------+-----------------+-----------------+-----------------+-----------------+
    | GroupDRO | 68.15(2.84)     | 71.48(1.27)     | 57.75(2.86)     | 59.77(1.95)     |
    +----------+-----------------+-----------------+-----------------+-----------------+
    | Coral    | **70.69(2.25)** | **72.96(1.06)** | 59.39(2.90)     | 60.29(2.50)     |
    +----------+-----------------+-----------------+-----------------+-----------------+
    | DANN     | 69.43(2.42)     | 71.70(0.90)     | **62.38(2.65)** | 65.15(3.13)     |
    +----------+-----------------+-----------------+-----------------+-----------------+
    | Mixup    | 70.65(1.86)     | 71.89(1.73)     | 59.11(3.11)     | 62.80(2.43)     |
    +----------+-----------------+-----------------+-----------------+-----------------+
    | DIR      | 68.44(2.51)     | 71.40(1.48)     | 57.67(3.75)     | **74.39(1.45)** |
    +----------+-----------------+-----------------+-----------------+-----------------+
    | GSAT     | 70.07(1.76)     | 72.51(0.97)     | 60.73(2.39)     | 56.96(1.76)     |
    +----------+-----------------+-----------------+-----------------+-----------------+
    | CIGAv1   | 69.40(2.39)     | 70.79(1.55)     | 61.81(1.68)     | 72.8(1.35)      |
    +----------+-----------------+-----------------+-----------------+-----------------+
    | CIGAv2   | 69.40(1.97)     | 71.65(1.33)     | 59.55(2.56)     | 73.62(1.33)     |
    +----------+-----------------+-----------------+-----------------+-----------------+


..  table::
    :widths: auto
    :class: std-table-style

    +-----------+-------------------+--------------------+--------------------+--------------------+
    |           |     scaffold                           |        size                             |
    | GOOD-ZINC +-------------------+--------------------+--------------------+--------------------+
    |           |     covariate     |      concept       |     covariate      |      concept       |
    +===========+===================+====================+====================+====================+
    |    ERM    |  0.1802(0.0174)   |   0.1301(0.0052)   |   0.2319(0.0072)   |   0.1325(0.0085)   |
    +-----------+-------------------+--------------------+--------------------+--------------------+
    |    IRM    |  0.2164(0.0160)   |   0.1339(0.0043)   |   0.6984(0.2809)   |   0.1336(0.0055)   |
    +-----------+-------------------+--------------------+--------------------+--------------------+
    |   VREx    |  0.1815(0.0154)   |   0.1287(0.0053)   |   0.2270(0.0136)   |   0.1311(0.0067)   |
    +-----------+-------------------+--------------------+--------------------+--------------------+
    | GroupDRO  |  0.1870(0.0128)   |   0.1323(0.0041)   |   0.2377(0.0147)   |   0.1333(0.0064)   |
    +-----------+-------------------+--------------------+--------------------+--------------------+
    |   Coral   |  0.1769(0.0152)   |   0.1303(0.0057)   |   0.2292(0.0090)   |   0.1261(0.0060)   |
    +-----------+-------------------+--------------------+--------------------+--------------------+
    |   DANN    |  0.1746(0.0084)   |   0.1269(0.0042)   |   0.2326(0.0140)   |   0.1348(0.0091)   |
    +-----------+-------------------+--------------------+--------------------+--------------------+
    |   Mixup   |  0.2066(0.0123)   |   0.1391(0.0071)   |   0.2531(0.0150)   |   0.1547(0.0082)   |
    +-----------+-------------------+--------------------+--------------------+--------------------+
    |    DIR    |  0.3682(0.0639)   |   0.2543(0.0454)   |   0.4578(0.0412)   |   0.3146(0.1225)   |
    +-----------+-------------------+--------------------+--------------------+--------------------+
    |   GSAT    | **0.1418(0.0077)**| **0.1066(0.0046)** | **0.2101(0.0095)** | **0.1038(0.0030)** |
    +-----------+-------------------+--------------------+--------------------+--------------------+

..  table::
    :widths: auto
    :class: std-table-style

    +-----------+-----------------+-----------------+-----------------+-----------------+
    | GOOD-PCBA |    scaffold     |                 |      size       |                 |
    +===========+=================+=================+=================+=================+
    |           |    covariate    |     concept     |    covariate    |      size       |
    +-----------+-----------------+-----------------+-----------------+-----------------+
    |    ERM    |   17.11(0.34)   |   21.93(0.74)   |   17.75(0.46)   |   15.60(0.55)   |
    +-----------+-----------------+-----------------+-----------------+-----------------+
    |    IRM    |   16.89(0.29)   |   22.37(0.43)   |   17.68(0.36)   |   15.82(0.52)   |
    +-----------+-----------------+-----------------+-----------------+-----------------+
    |   VREx    |   17.10(0.20)   |   21.65(0.82)   |   17.80(0.35)   |   15.85(0.47)   |
    +-----------+-----------------+-----------------+-----------------+-----------------+
    | GroupDRO  |   16.55(0.39)   |   21.91(0.93)   |   16.74(0.60)   |   15.21(0.66)   |
    +-----------+-----------------+-----------------+-----------------+-----------------+
    |   Coral   |   17.00(0.38)   |   22.00(0.46)   | **17.83(0.31)** | **16.88(0.58)** |
    +-----------+-----------------+-----------------+-----------------+-----------------+
    |   DANN    | **17.20(0.46)** |   22.03(0.72)   |   17.71(0.26)   |   15.78(0.40)   |
    +-----------+-----------------+-----------------+-----------------+-----------------+
    |   Mixup   |   16.52(0.33)   |   20.52(0.50)   |   17.42(0.29)   |   13.71(0.37)   |
    +-----------+-----------------+-----------------+-----------------+-----------------+
    |    DIR    |   16.33(0.39)   | **23.82(0.89)** |   16.04(1.14)   |   16.80(1.17)   |
    +-----------+-----------------+-----------------+-----------------+-----------------+
    |   GSAT    |   16.45(0.17)   |   20.18(0.74)   |   17.57(0.40)   |   13.52(0.90)   |
    +-----------+-----------------+-----------------+-----------------+-----------------+

..  table::
    :widths: auto
    :class: std-table-style

    +-----------+-----------------+-----------------+
    |           |     length                        |
    | GOOD-SST2 +-----------------+-----------------+
    |           |    covariate    |     concept     |
    +===========+=================+=================+
    |    ERM    |   80.52(1.13)   |   72.92(1.10)   |
    +-----------+-----------------+-----------------+
    |    IRM    |   80.75(1.17)   | **77.45(2.37)** |
    +-----------+-----------------+-----------------+
    |   VREx    |   80.20(1.39)   |   72.92(0.95)   |
    +-----------+-----------------+-----------------+
    | GroupDRO  | **81.67(0.45)** |   72.51(0.79)   |
    +-----------+-----------------+-----------------+
    |   Coral   |   78.94(1.22)   |   72.98(0.46)   |
    +-----------+-----------------+-----------------+
    |   DANN    |   80.53(1.40)   |   74.10(1.49)   |
    +-----------+-----------------+-----------------+
    |   Mixup   |   80.77(1.03)   |   72.57(0.76)   |
    +-----------+-----------------+-----------------+
    |    DIR    |   81.55(1.06)   |   67.98(3.07)   |
    +-----------+-----------------+-----------------+
    |   GSAT    |   81.49(0.76)   |   74.54(1.40)   |
    +-----------+-----------------+-----------------+
    | CIGAv1    | 80.44(1.24)     | 71.18(1.91)     |
    +-----------+-----------------+-----------------+
    | CIGAv2    | 80.46(2.00)     | 70.33(1.73)     |
    +-----------+-----------------+-----------------+

Node level
-----------

More results will be available soon...

