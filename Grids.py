{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMKSVC8lyQFoIQf/ZQay/Bm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/zahide09034/textmining/blob/master/Grids.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "-Hd71FEuk1yX"
      },
      "outputs": [],
      "source": [
        "arima = {\n",
        "\t'order':[(2,1,0),(0,1,2),(1,1,1)],\n",
        "\t'seasonal_order':[(0,0,0,0),(0,1,1,12)],\n",
        "\t'trend':['n','c','t','ct']\n",
        "}\n",
        "\n",
        "elasticnet = {\n",
        "\t'alpha':[i/10 for i in range(1,101)],\n",
        "\t'l1_ratio':[0,0.25,0.5,0.75,1],\n",
        "\t'normalizer':['scale','minmax',None]\n",
        "}\n",
        "\n",
        "gbt = {\n",
        "\t'max_depth':[2,3],\n",
        "\t'n_estimators':[100,500]\n",
        "}\n",
        "\n",
        "hwes = {\n",
        "\t'trend':[None,'add','mul'],\n",
        "\t'seasonal':[None,'add','mul'],\n",
        "\t'damped_trend':[True,False]\n",
        "}\n",
        "\n",
        "knn = {\n",
        "\t'n_neighbors':range(2,20),\n",
        "\t'weights':['uniform','distance']\n",
        "}\n",
        "\n",
        "mlp = {\n",
        "\t'activation':['relu','tanh'],\n",
        "\t'hidden_layer_sizes':[(25,),(25,25,)],\n",
        "\t'solver':['lbfgs','adam'],\n",
        "\t'normalizer':['scale','minmax',None],\n",
        "\t'random_state':[20]\n",
        "}\n",
        "\n",
        "mlr = {\n",
        "\t'normalizer':['scale','minmax',None]\n",
        "}\n",
        "\n",
        "prophet = {\n",
        "\t'n_changepoints':range(5)\n",
        "}\n",
        "\n",
        "rf = {\n",
        "\t'max_depth':[5,10,None],\n",
        "\t'n_estimators':[100,500,1000]\n",
        "}\n",
        "\n",
        "svr={\n",
        "\t'kernel':['linear'],\n",
        "        'C':[.5,1,2,3],\n",
        "        'epsilon':[0.01,0.1,0.5]\n",
        "}\n",
        "\n",
        "xgboost = {\n",
        "\t'max_depth':[2,3,4,5,6]\n",
        "}"
      ]
    }
  ]
}