{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled9.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMAUkOssR2q/GG3iniNBPQg",
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
        "<a href=\"https://colab.research.google.com/github/costagean/Redes_Neurais/blob/main/desejabilidade%20ponto%20otimo%20HTC.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hKOOCe3N5s1g",
        "outputId": "f098e6a2-b463-46bf-e054-3c057bbc767a"
      },
      "source": [
        "import numpy as np\n",
        "\n",
        "a = np.linspace(-1.2872,1.2872,99)\n",
        "b = np.linspace(-1.2872,1.2872,99)\n",
        "c = np.linspace(-1.2872,1.2872,99)\n",
        "\n",
        "x1 = 0\n",
        "x2 = 0\n",
        "x3 = 0\n",
        "\n",
        "y1=0\n",
        "y2=0\n",
        "\n",
        "d1=0\n",
        "d2=0\n",
        "d3=0\n",
        "\n",
        "d=0\n",
        "D=0\n",
        "\n",
        "y1_maxi = 54.0885 - 7.54505 * (x1) - 1.02238 * (x1) * (x1) - 1.25961 * (x2) - 0.72966 * (x2) * (x2) - 1.9597 * (x3) - 0.66750 * (x1) * (x2) - 0.58000 * (x1) * (x3)\n",
        "y2_maxi = 62.33011 - 3.22941 * (x1) - 1.48243 * (x2) * (x2) - 1.10089 * (x3) - 1.60750 * (x1) * (x2) - 0.96250 * (x1) * (x3)\n",
        "\n",
        "y1_mini = 54.0885 - 7.54505 * (x1) - 1.02238 * (x1) * (x1) - 1.25961 * (x2) - 0.72966 * (x2) * (x2) - 1.9597 * (x3) - 0.66750 * (x1) * (x2) - 0.58000 * (x1) * (x3)\n",
        "y2_mini = 62.33011 - 3.22941 * (x1) - 1.48243 * (x2) * (x2) - 1.10089 * (x3) - 1.60750 * (x1) * (x2) - 0.96250 * (x1) * (x3)\n",
        "\n",
        "x1_maxi_y1 = 0\n",
        "x2_maxi_y1 = 0\n",
        "\n",
        "x1_mini_y1 = 0\n",
        "x2_mini_y1 = 0\n",
        "\n",
        "x1_maxi_y2 = 0\n",
        "x2_maxi_y2 = 0\n",
        "\n",
        "x1_mini_y2 = 0\n",
        "x2_mini_y2 = 0\n",
        "\n",
        "for i in range(0, len(a)):\n",
        "    x1 = a[i]\n",
        "    for j in range(0, len(b)):\n",
        "        x2 = b[j]\n",
        "        for k in range(0, len(c)):\n",
        "            x3 = c[k]\n",
        "            y1 = 54.0885 - 7.54505 * (x1) - 1.02238 * (x1) * (x1) - 1.25961 * (x2) - 0.72966 * (x2) * (x2) - 1.9597 * (x3) - 0.66750 * (x1) * (x2) - 0.58000 * (x1) * (x3)\n",
        "            y2 = 62.33011 - 3.22941 * (x1) - 1.48243 * (x2) * (x2) - 1.10089 * (x3) - 1.60750 * (x1) * (x2) - 0.96250 * (x1) * (x3)\n",
        "\n",
        "            if y1>y1_maxi:\n",
        "                y1_maxi = y1\n",
        "                x1_maxi_y1 = x1\n",
        "                x2_maxi_y1 = x2\n",
        "                x3_maxi_y1 = x3\n",
        "            elif y1<y1_mini:\n",
        "                y1_mini = y1\n",
        "                x1_mini_y1 = x1\n",
        "                x2_mini_y1 = x2\n",
        "                x3_mini_y1 = x3\n",
        "            if y2 > y2_maxi:\n",
        "                y2_maxi = y2\n",
        "                x1_maxi_y2 = x1\n",
        "                x2_maxi_y2 = x2\n",
        "                x3_maxi_y2 = x3\n",
        "            elif y2 < y2_mini:\n",
        "                y2_mini = y2\n",
        "                x1_mini_y2 = x1\n",
        "                x2_mini_y2 = x2\n",
        "                x3_mini_y2 = x3\n",
        "\n",
        "print('=============================================================================================')\n",
        "print(' maximo de y1 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y1_maxi,x1_maxi_y1,x2_maxi_y1,x3_maxi_y1))\n",
        "print(' minimo de y1 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y1_mini,x1_mini_y1,x2_mini_y1,x3_mini_y1))\n",
        "print('=============================================================================================')\n",
        "print(' maximo de y2 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y2_maxi,x1_maxi_y2,x2_maxi_y2,x3_maxi_y2))\n",
        "print(' minimo de y2 eh de {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(y2_mini,x1_mini_y2,x2_mini_y2,x3_mini_y2))\n",
        "print('=============================================================================================')\n",
        "\n",
        "for i in range(0, len(a)):\n",
        "    x1 = a[i]\n",
        "    for j in range(0, len(b)):\n",
        "        x2 = b[j]\n",
        "        for k in range(0, len(c)):\n",
        "            x3 = c[k]\n",
        "            y1 = 54.0885 - 7.54505 * (x1) - 1.02238 * (x1) * (x1) - 1.25961 * (x2) - 0.72966 * (x2) * (x2) - 1.9597 * (x3) - 0.66750 * (x1) * (x2) - 0.58000 * (x1) * (x3)\n",
        "            y2 = 62.33011 - 3.22941 * (x1) - 1.48243 * (x2) * (x2) - 1.10089 * (x3) - 1.60750 * (x1) * (x2) - 0.96250 * (x1) * (x3)\n",
        "\n",
        "            d1=(y1-y1_mini)/(y1_maxi-y1_mini) #maximizar\n",
        "            d2=(y2-y2_mini)/(y2_maxi-y2_mini) #maximizar\n",
        "            d = d1 * d2\n",
        "\n",
        "            if d > D:\n",
        "                D = d\n",
        "                x1_opt = x1\n",
        "                x2_opt = x2\n",
        "                x3_opt = x3\n",
        "                y1_opt=y1\n",
        "                y2_opt=y2\n",
        "\n",
        "print('=============================================================================================')\n",
        "print(' A desejabilidade foi {:.2f} com x1 de {:.2f}, x2 de {:.2f} e x3 de {:.2f}'.format(D,x1_opt,x2_opt,x3_opt))\n",
        "print(' y1 com valor de {:.2f}'.format(y1_opt))\n",
        "print(' y2 com valor de {:.2f}'.format(y2_opt))"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "=============================================================================================\n",
            " maximo de y1 eh de 63.72 com x1 de -1.29, x2 de -0.26 e x3 de -1.29\n",
            " minimo de y1 eh de 35.26 com x1 de 1.29, x2 de 1.29 e x3 de 1.29\n",
            "=============================================================================================\n",
            " maximo de y2 eh de 67.39 com x1 de -1.29, x2 de 0.71 e x3 de 1.29\n",
            " minimo de y2 eh de 50.04 com x1 de 1.29, x2 de 1.29 e x3 de 1.29\n",
            "=============================================================================================\n",
            "=============================================================================================\n",
            " A desejabilidade foi 0.96 com x1 de -1.29, x2 de 0.47 e x3 de -1.29\n",
            " y1 com valor de 63.32\n",
            " y2 com valor de 66.96\n"
          ]
        }
      ]
    }
  ]
}