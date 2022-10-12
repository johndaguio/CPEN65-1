{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPydhbc7LJC32KzMkoH3Sxz",
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
        "<a href=\"https://colab.research.google.com/github/johndaguio/CPEN65-1/blob/main/Activity_in_CPEN65_Area_of_a_Circle_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V8EqfAeQ4HO-",
        "outputId": "3a326251-a42c-476f-e54d-891b282d3898"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "78.53975 is the area of the circle \n",
            "while 50.26544 is the area of the circle using diameter \n"
          ]
        }
      ],
      "source": [
        "class Circle:\n",
        "    def __init__(self, pi, r, d):\n",
        "        self.pi = pi\n",
        "        self.r = r\n",
        "        self.d = d\n",
        "\n",
        "    def Area(self):\n",
        "        print(self.pi * self.r ** 2, \"is the area of the circle \")\n",
        "\n",
        "    def Area2(self):\n",
        "        print(\"while\", self.pi * self.d ** 2 / 4, \"is the area of the circle using diameter \")\n",
        "\n",
        "\n",
        "c = Circle (3.14159, 5, 8)\n",
        "c.Area()\n",
        "c.Area2()"
      ]
    }
  ]
}