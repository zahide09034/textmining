{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN+5VEFg7v04cwStjJ9KomW",
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
      "execution_count": 1,
      "metadata": {
        "id": "-Hd71FEuk1yX"
      },
      "outputs": [],
      "source": [
        "def forecast_distribution(self, data, **kwargs):\n",
        "        ret = []\n",
        "\n",
        "        smooth = kwargs.get(\"smooth\", \"KDE\")\n",
        "        alpha = kwargs.get(\"alpha\", None)\n",
        "\n",
        "        uod = self.get_UoD()\n",
        "\n",
        "        for k in np.arange(self.order, len(data)):\n",
        "\n",
        "            sample = data[k-self.order : k]\n",
        "\n",
        "            forecasts = self.get_models_forecasts(sample)\n",
        "\n",
        "            if alpha is None:\n",
        "                forecasts = np.ravel(forecasts).tolist()\n",
        "            else:\n",
        "                forecasts = self.get_distribution_interquantile(np.ravel(forecasts).tolist(), alpha)\n",
        "\n",
        "            dist = ProbabilityDistribution.ProbabilityDistribution(smooth, uod=uod, data=forecasts,\n",
        "                                                                   name=\"\", **kwargs)\n",
        "\n",
        "            ret.append(dist)\n",
        "\n",
        "        return ret "
      ]
    }
  ]
}