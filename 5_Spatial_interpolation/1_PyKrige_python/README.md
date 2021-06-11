# PyKrige
**Kriging是理解稀疏数据行为的宝贵工具**。  
## Purpose
该代码支持 2D 和 3D 普通克里金法和通用克里金法。内置标准变异函数模型（线性、幂、球面、高斯、指数），但也可以使用自定义变异函数模型。 2D 通用克里金码目前支持区域线性、点对数和外部漂移项，而 3D 通用克里金码支持所有三个空间维度的区域线性漂移项。两个通用克里金法类还支持通用的“指定”和“功能”漂移功能。使用“指定”漂移能力，用户可以手动指定每个数据点和所有网格点的漂移值。利用“功能性”漂移能力，用户可以提供定义漂移的空间坐标的可调用函数。该包包含一个模块，该模块包含在处理 ASCII 网格文件时应该有用的函数 ()```\*.asc```
## Features
### Kriging算法
  ``` OrdinaryKriging```： 2D ordinary kriging with estimated mean
  ``` UniversalKriging```:2D universal kriging providing drift terms
  ```OrdinaryKriging3D: ```3D ordinary kriging
  ```UniversalKriging3D: ```3D universal kriging
  ```RegressionKriging:``` An implementation of Regression-Kriging
  ```ClassificationKriging:``` An implementation of Simplicial Indicator Kriging
  
