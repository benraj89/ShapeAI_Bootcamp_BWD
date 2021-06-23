{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "weather.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMLoL6L5kGebd2U2+/H/4SX",
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
        "<a href=\"https://colab.research.google.com/github/benraj89/ShapeAI_Bootcamp_BWD/blob/main/weather.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P8_k6dAhfR__",
        "outputId": "8f920240-17bb-4b61-b6cf-7cbe2a4f33f5"
      },
      "source": [
        "import requests\n",
        "from datetime import datetime\n",
        "\n",
        "api_key = '9eef7d72b38059cf56b03fc86cf28f2e'\n",
        "location = input(\"Enter the city name: \")\n",
        "\n",
        "complete_api_link = \"https://api.openweathermap.org/data/2.5/weather?q=\"+location+\"&appid=\"+api_key\n",
        "api_link = requests.get(complete_api_link)\n",
        "api_data = api_link.json()\n",
        "\n",
        "temp_city = ((api_data['main']['temp']) - 273.15)\n",
        "weather_desc = api_data['weather'][0]['description']\n",
        "hmdt = api_data['main']['humidity']\n",
        "wind_spd = api_data['wind']['speed']\n",
        "date_time = datetime.now().strftime(\"%d %b %Y | %I:%M:%S %p\")\n",
        "\n",
        "print (\"-------------------------------------------------------------\")\n",
        "print (\"Weather Stats for - {}  || {}\".format(location.upper(), date_time))\n",
        "print (\"-------------------------------------------------------------\")\n",
        "\n",
        "print (\"Current temperature is: {:.2f} deg C\".format(temp_city))\n",
        "print (\"Current weather desc  :\",weather_desc)\n",
        "print (\"Current Humidity      :\",hmdt, '%')"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the city name: muvattupuzha\n",
            "-------------------------------------------------------------\n",
            "Weather Stats for - MUVATTUPUZHA  || 23 Jun 2021 | 10:52:52 AM\n",
            "-------------------------------------------------------------\n",
            "Current temperature is: 28.78 deg C\n",
            "Current weather desc  : overcast clouds\n",
            "Current Humidity      : 78 %\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "w3zKDlTifXDP"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}