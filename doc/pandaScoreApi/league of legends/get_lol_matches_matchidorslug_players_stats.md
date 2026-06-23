> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get stats for LoL players on match

Get detailed statistics of League-of-Legends players for the given match
> ℹ️  
> 
> This endpoint is only available to customers with a historical or real-time data plan

# OpenAPI definition

```json
{
  "components": {
    "responses": {
      "Error400": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Bad request"
      },
      "Error401": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Unauthorized"
      },
      "Error403": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Forbidden"
      },
      "Error404": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Not found"
      },
      "Error422": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Unprocessable Entity"
      },
      "LoLStatsForAllPlayersByMatch": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/matches/549811/players/stats": {
                "description": "/lol/matches/549811/players/stats",
                "value": {
                  "teams": [
                    {
                      "id": 1452,
                      "name": "Griffin",
                      "players": [
                        {
                          "first_name": "Lee",
                          "id": 958,
                          "last_name": "Seung-yong",
                          "name": "Tarzan",
                          "stats": {
                            "averages": {
                              "assists": 7,
                              "cs_at_14": 71,
                              "cs_diff_at_14": 8,
                              "deaths": 2,
                              "gold_earned": 11510,
                              "gold_percentage": 20.4,
                              "gold_spent": 10575,
                              "kill_counters": {
                                "inhibitors": 0,
                                "neutral_minions": 128,
                                "neutral_minions_enemy_jungle": 5,
                                "neutral_minions_team_jungle": 76,
                                "players": 9,
                                "turrets": 0,
                                "wards": 8
                              },
                              "kills": 9,
                              "magic_damage": {
                                "dealt": 21569,
                                "dealt_percentage": 9.35,
                                "dealt_to_champions": 1215,
                                "dealt_to_champions_percentage": 4.64,
                                "taken": null
                              },
                              "minions_killed": 147,
                              "physical_damage": {
                                "dealt": 106192,
                                "dealt_percentage": 28.96,
                                "dealt_to_champions": 11084,
                                "dealt_to_champions_percentage": 32.31,
                                "taken": 19267
                              },
                              "total_damage": {
                                "dealt": 137939,
                                "dealt_percentage": 21.79,
                                "dealt_to_champions": 13037,
                                "dealt_to_champions_percentage": 21.08,
                                "taken": 27318
                              },
                              "total_heal": 10385,
                              "total_time_crowd_control_dealt": 363,
                              "total_units_healed": 1,
                              "true_damage": {
                                "dealt": 10177,
                                "dealt_percentage": 28.38,
                                "dealt_to_champions": 737,
                                "dealt_to_champions_percentage": 54.07,
                                "taken": 1338
                              },
                              "vision_wards_bought_in_game": 16,
                              "wards_placed": 22
                            },
                            "games_count": 1,
                            "totals": {
                              "assists": 7,
                              "deaths": 2,
                              "games_lost": 0,
                              "games_played": 1,
                              "games_won": 1,
                              "kill_counters": {
                                "inhibitors": 0,
                                "turrets": 0,
                                "wards": 8
                              },
                              "kills": 9,
                              "kills_series": {
                                "double_kills": 0,
                                "penta_kills": 0,
                                "quadra_kills": 0,
                                "triple_kills": 0
                              },
                              "matches_lost": 0,
                              "matches_played": 1,
                              "matches_won": 1,
                              "wards_placed": 22
                            }
                          }
                        },
                        {
                          "first_name": "Son",
                          "id": 1210,
                          "last_name": "Si-woo",
                          "name": "Lehends",
                          "stats": {
                            "averages": {
                              "assists": 18,
                              "cs_at_14": 8,
                              "cs_diff_at_14": -11,
                              "deaths": 2,
                              "gold_earned": 8093,
                              "gold_percentage": 14.34,
                              "gold_spent": 7500,
                              "kill_counters": {
                                "inhibitors": 0,
                                "neutral_minions": 0,
                                "neutral_minions_enemy_jungle": 0,
                                "neutral_minions_team_jungle": 0,
                                "players": 1,
                                "turrets": 0,
                                "wards": 15
                              },
                              "kills": 1,
                              "magic_damage": {
                                "dealt": 9056,
                                "dealt_percentage": 3.93,
                                "dealt_to_champions": 4726,
                                "dealt_to_champions_percentage": 18.05,
                                "taken": null
                              },
                              "minions_killed": 20,
                              "physical_damage": {
                                "dealt": 6979,
                                "dealt_percentage": 1.9,
                                "dealt_to_champions": 1027,
                                "dealt_to_champions_percentage": 2.99,
                                "taken": 4841
                              },
                              "total_damage": {
                                "dealt": 16036,
                                "dealt_percentage": 2.53,
                                "dealt_to_champions": 5754,
                                "dealt_to_champions_percentage": 9.3,
                                "taken": 11378
                              },
                              "total_heal": 5836,
                              "total_time_crowd_control_dealt": 65,
                              "total_units_healed": 5,
                              "true_damage": {
                                "dealt": 0,
                                "dealt_percentage": 0,
                                "dealt_to_champions": 0,
                                "dealt_to_champions_percentage": 0,
                                "taken": 1628
                              },
                              "vision_wards_bought_in_game": 14,
                              "wards_placed": 42
                            },
                            "games_count": 1,
                            "totals": {
                              "assists": 18,
                              "deaths": 2,
                              "games_lost": 0,
                              "games_played": 1,
                              "games_won": 1,
                              "kill_counters": {
                                "inhibitors": 0,
                                "turrets": 0,
                                "wards": 15
                              },
                              "kills": 1,
                              "kills_series": {
                                "double_kills": 0,
                                "penta_kills": 0,
                                "quadra_kills": 0,
                                "triple_kills": 0
                              },
                              "matches_lost": 0,
                              "matches_played": 1,
                              "matches_won": 1,
                              "wards_placed": 42
                            }
                          }
                        },
                        {
                          "first_name": "Choi",
                          "id": 8135,
                          "last_name": "Sung-won",
                          "name": "Sw0rd",
                          "stats": {
                            "averages": {
                              "assists": 12,
                              "cs_at_14": 89,
                              "cs_diff_at_14": -16,
                              "deaths": 0,
                              "gold_earned": 9328,
                              "gold_percentage": 16.53,
                              "gold_spent": 8625,
                              "kill_counters": {
                                "inhibitors": 0,
                                "neutral_minions": 8,
                                "neutral_minions_enemy_jungle": 0,
                                "neutral_minions_team_jungle": 4,
                                "players": 1,
                                "turrets": 0,
                                "wards": 4
                              },
                              "kills": 1,
                              "magic_damage": {
                                "dealt": 35966,
                                "dealt_percentage": 15.6,
                                "dealt_to_champions": 4984,
                                "dealt_to_champions_percentage": 19.03,
                                "taken": null
                              },
                              "minions_killed": 175,
                              "physical_damage": {
                                "dealt": 58481,
                                "dealt_percentage": 15.95,
                                "dealt_to_champions": 4245,
                                "dealt_to_champions_percentage": 12.37,
                                "taken": 11019
                              },
                              "total_damage": {
                                "dealt": 100218,
                                "dealt_percentage": 15.83,
                                "dealt_to_champions": 9399,
                                "dealt_to_champions_percentage": 15.19,
                                "taken": 17954
                              },
                              "total_heal": 5145,
                              "total_time_crowd_control_dealt": 539,
                              "total_units_healed": 1,
                              "true_damage": {
                                "dealt": 5770,
                                "dealt_percentage": 16.09,
                                "dealt_to_champions": 170,
                                "dealt_to_champions_percentage": 12.47,
                                "taken": 0
                              },
                              "vision_wards_bought_in_game": 5,
                              "wards_placed": 14
                            },
                            "games_count": 1,
                            "totals": {
                              "assists": 12,
                              "deaths": 0,
                              "games_lost": 0,
                              "games_played": 1,
                              "games_won": 1,
                              "kill_counters": {
                                "inhibitors": 0,
                                "turrets": 0,
                                "wards": 4
                              },
                              "kills": 1,
                              "kills_series": {
                                "double_kills": 0,
                                "penta_kills": 0,
                                "quadra_kills": 0,
                                "triple_kills": 0
                              },
                              "matches_lost": 0,
                              "matches_played": 1,
                              "matches_won": 1,
                              "wards_placed": 14
                            }
                          }
                        },
                        {
                          "first_name": "Park",
                          "id": 8176,
                          "last_name": "Do-hyeon",
                          "name": "Viper",
                          "stats": {
                            "averages": {
                              "assists": 6,
                              "cs_at_14": 108,
                              "cs_diff_at_14": 2,
                              "deaths": 0,
                              "gold_earned": 14853,
                              "gold_percentage": 26.32,
                              "gold_spent": 13175,
                              "kill_counters": {
                                "inhibitors": 0,
                                "neutral_minions": 32,
                                "neutral_minions_enemy_jungle": 8,
                                "neutral_minions_team_jungle": 16,
                                "players": 9,
                                "turrets": 2,
                                "wards": 8
                              },
                              "kills": 9,
                              "magic_damage": {
                                "dealt": 5039,
                                "dealt_percentage": 2.19,
                                "dealt_to_champions": 856,
                                "dealt_to_champions_percentage": 3.27,
                                "taken": null
                              },
                              "minions_killed": 276,
                              "physical_damage": {
                                "dealt": 189954,
                                "dealt_percentage": 51.8,
                                "dealt_to_champions": 17775,
                                "dealt_to_champions_percentage": 51.81,
                                "taken": 6803
                              },
                              "total_damage": {
                                "dealt": 211851,
                                "dealt_percentage": 33.46,
                                "dealt_to_champions": 19088,
                                "dealt_to_champions_percentage": 30.86,
                                "taken": 11774
                              },
                              "total_heal": 966,
                              "total_time_crowd_control_dealt": 85,
                              "total_units_healed": 1,
                              "true_damage": {
                                "dealt": 16858,
                                "dealt_percentage": 47.01,
                                "dealt_to_champions": 456,
                                "dealt_to_champions_percentage": 33.46,
                                "taken": 418
                              },
                              "vision_wards_bought_in_game": 7,
                              "wards_placed": 12
                            },
                            "games_count": 1,
                            "totals": {
                              "assists": 6,
                              "deaths": 0,
                              "games_lost": 0,
                              "games_played": 1,
                              "games_won": 1,
                              "kill_counters": {
                                "inhibitors": 0,
                                "turrets": 2,
                                "wards": 8
                              },
                              "kills": 9,
                              "kills_series": {
                                "double_kills": 3,
                                "penta_kills": 0,
                                "quadra_kills": 0,
                                "triple_kills": 1
                              },
                              "matches_lost": 0,
                              "matches_played": 1,
                              "matches_won": 1,
                              "wards_placed": 12
                            }
                          }
                        },
                        {
                          "first_name": "Jeong",
                          "id": 15000,
                          "last_name": "Ji-hoon",
                          "name": "Chovy",
                          "stats": {
                            "averages": {
                              "assists": 12,
                              "cs_at_14": 128,
                              "cs_diff_at_14": -4,
                              "deaths": 0,
                              "gold_earned": 12648,
                              "gold_percentage": 22.41,
                              "gold_spent": 11575,
                              "kill_counters": {
                                "inhibitors": 0,
                                "neutral_minions": 9,
                                "neutral_minions_enemy_jungle": 0,
                                "neutral_minions_team_jungle": 5,
                                "players": 3,
                                "turrets": 4,
                                "wards": 10
                              },
                              "kills": 3,
                              "magic_damage": {
                                "dealt": 158933,
                                "dealt_percentage": 68.93,
                                "dealt_to_champions": 14405,
                                "dealt_to_champions_percentage": 55.01,
                                "taken": null
                              },
                              "minions_killed": 251,
                              "physical_damage": {
                                "dealt": 5133,
                                "dealt_percentage": 1.4,
                                "dealt_to_champions": 175,
                                "dealt_to_champions_percentage": 0.51,
                                "taken": 12741
                              },
                              "total_damage": {
                                "dealt": 167123,
                                "dealt_percentage": 26.39,
                                "dealt_to_champions": 14580,
                                "dealt_to_champions_percentage": 23.57,
                                "taken": 15448
                              },
                              "total_heal": 4216,
                              "total_time_crowd_control_dealt": 58,
                              "total_units_healed": 1,
                              "true_damage": {
                                "dealt": 3057,
                                "dealt_percentage": 8.52,
                                "dealt_to_champions": 0,
                                "dealt_to_champions_percentage": 0,
                                "taken": 278
                              },
                              "vision_wards_bought_in_game": 5,
                              "wards_placed": 14
                            },
                            "games_count": 1,
                            "totals": {
                              "assists": 12,
                              "deaths": 0,
                              "games_lost": 0,
                              "games_played": 1,
                              "games_won": 1,
                              "kill_counters": {
                                "inhibitors": 0,
                                "turrets": 4,
                                "wards": 10
                              },
                              "kills": 3,
                              "kills_series": {
                                "double_kills": 0,
                                "penta_kills": 0,
                                "quadra_kills": 0,
                                "triple_kills": 0
                              },
                              "matches_lost": 0,
                              "matches_played": 1,
                              "matches_won": 1,
                              "wards_placed": 14
                            }
                          }
                        }
                      ],
                      "slug": "griffin"
                    },
                    {
                      "id": 88,
                      "name": "G2 Esports",
                      "players": [
                        {
                          "first_name": "Luka",
                          "id": 470,
                          "last_name": "Perković",
                          "name": "Perkz",
                          "stats": {
                            "averages": {
                              "assists": 0,
                              "cs_at_14": 106,
                              "cs_diff_at_14": -2,
                              "deaths": 2,
                              "gold_earned": 10025,
                              "gold_percentage": 23.15,
                              "gold_spent": 9150,
                              "kill_counters": {
                                "inhibitors": 0,
                                "neutral_minions": 4,
                                "neutral_minions_enemy_jungle": 0,
                                "neutral_minions_team_jungle": 4,
                                "players": 2,
                                "turrets": 0,
                                "wards": 3
                              },
                              "kills": 2,
                              "magic_damage": {
                                "dealt": 91801,
                                "dealt_percentage": 37.81,
                                "dealt_to_champions": 10910,
                                "dealt_to_champions_percentage": 46.73,
                                "taken": null
                              },
                              "minions_killed": 212,
                              "physical_damage": {
                                "dealt": 12875,
                                "dealt_percentage": 4.99,
                                "dealt_to_champions": 1124,
                                "dealt_to_champions_percentage": 4.89,
                                "taken": 8129
                              },
                              "total_damage": {
                                "dealt": 114274,
                                "dealt_percentage": 21.31,
                                "dealt_to_champions": 12889,
                                "dealt_to_champions_percentage": 26.85,
                                "taken": 13542
                              },
                              "total_heal": 1996,
                              "total_time_crowd_control_dealt": 149,
                              "total_units_healed": 1,
                              "true_damage": {
                                "dealt": 9597,
                                "dealt_percentage": 26.92,
                                "dealt_to_champions": 855,
                                "dealt_to_champions_percentage": 51.38,
                                "taken": 0
                              },
                              "vision_wards_bought_in_game": 4,
                              "wards_placed": 11
                            },
                            "games_count": 1,
                            "totals": {
                              "assists": 0,
                              "deaths": 2,
                              "games_lost": 1,
                              "games_played": 1,
                              "games_won": 0,
                              "kill_counters": {
                                "inhibitors": 0,
                                "turrets": 0,
                                "wards": 3
                              },
                              "kills": 2,
                              "kills_series": {
                                "double_kills": 0,
                                "penta_kills": 0,
                                "quadra_kills": 0,
                                "triple_kills": 0
                              },
                              "matches_lost": 1,
                              "matches_played": 1,
                              "matches_won": 0,
                              "wards_placed": 11
                            }
                          }
                        },
                        {
                          "first_name": "Mihael",
                          "id": 605,
                          "last_name": "Mehle",
                          "name": "Mikyx",
                          "stats": {
                            "averages": {
                              "assists": 0,
                              "cs_at_14": 19,
                              "cs_diff_at_14": 11,
                              "deaths": 7,
                              "gold_earned": 5935,
                              "gold_percentage": 13.7,
                              "gold_spent": 5300,
                              "kill_counters": {
                                "inhibitors": 0,
                                "neutral_minions": 0,
                                "neutral_minions_enemy_jungle": 0,
                                "neutral_minions_team_jungle": 0,
                                "players": 1,
                                "turrets": 0,
                                "wards": 13
                              },
                              "kills": 1,
                              "magic_damage": {
                                "dealt": 2468,
                                "dealt_percentage": 1.02,
                                "dealt_to_champions": 681,
                                "dealt_to_champions_percentage": 2.92,
                                "taken": null
                              },
                              "minions_killed": 45,
                              "physical_damage": {
                                "dealt": 6791,
                                "dealt_percentage": 2.63,
                                "dealt_to_champions": 1716,
                                "dealt_to_champions_percentage": 7.46,
                                "taken": 11383
                              },
                              "total_damage": {
                                "dealt": 17273,
                                "dealt_percentage": 3.22,
                                "dealt_to_champions": 3131,
                                "dealt_to_champions_percentage": 6.52,
                                "taken": 16331
                              },
                              "total_heal": 973,
                              "total_time_crowd_control_dealt": 64,
                              "total_units_healed": 3,
                              "true_damage": {
                                "dealt": 8013,
                                "dealt_percentage": 22.47,
                                "dealt_to_champions": 734,
                                "dealt_to_champions_percentage": 44.11,
                                "taken": 498
                              },
                              "vision_wards_bought_in_game": 20,
                              "wards_placed": 45
                            },
                            "games_count": 1,
                            "totals": {
                              "assists": 0,
                              "deaths": 7,
                              "games_lost": 1,
                              "games_played": 1,
                              "games_won": 0,
                              "kill_counters": {
                                "inhibitors": 0,
                                "turrets": 0,
                                "wards": 13
                              },
                              "kills": 1,
                              "kills_series": {
                                "double_kills": 0,
                                "penta_kills": 0,
                                "quadra_kills": 0,
                                "triple_kills": 0
                              },
                              "matches_lost": 1,
                              "matches_played": 1,
                              "matches_won": 0,
                              "wards_placed": 45
                            }
                          }
                        },
                        {
                          "first_name": "Rasmus",
                          "id": 1132,
                          "last_name": "Winther",
                          "name": "Caps",
                          "stats": {
                            "averages": {
                              "assists": 2,
                              "cs_at_14": 132,
                              "cs_diff_at_14": 4,
                              "deaths": 4,
                              "gold_earned": 9877,
                              "gold_percentage": 22.8,
                              "gold_spent": 9725,
                              "kill_counters": {
                                "inhibitors": 0,
                                "neutral_minions": 20,
                                "neutral_minions_enemy_jungle": 1,
                                "neutral_minions_team_jungle": 16,
                                "players": 1,
                                "turrets": 1,
                                "wards": 3
                              },
                              "kills": 1,
                              "magic_damage": {
                                "dealt": 121090,
                                "dealt_percentage": 49.88,
                                "dealt_to_champions": 11004,
                                "dealt_to_champions_percentage": 47.14,
                                "taken": null
                              },
                              "minions_killed": 245,
                              "physical_damage": {
                                "dealt": 11368,
                                "dealt_percentage": 4.41,
                                "dealt_to_champions": 655,
                                "dealt_to_champions_percentage": 2.85,
                                "taken": 12130
                              },
                              "total_damage": {
                                "dealt": 142962,
                                "dealt_percentage": 26.66,
                                "dealt_to_champions": 11659,
                                "dealt_to_champions_percentage": 24.29,
                                "taken": 17907
                              },
                              "total_heal": 4982,
                              "total_time_crowd_control_dealt": 525,
                              "total_units_healed": 1,
                              "true_damage": {
                                "dealt": 10504,
                                "dealt_percentage": 29.46,
                                "dealt_to_champions": 0,
                                "dealt_to_champions_percentage": 0,
                                "taken": 212
                              },
                              "vision_wards_bought_in_game": 5,
                              "wards_placed": 13
                            },
                            "games_count": 1,
                            "totals": {
                              "assists": 2,
                              "deaths": 4,
                              "games_lost": 1,
                              "games_played": 1,
                              "games_won": 0,
                              "kill_counters": {
                                "inhibitors": 0,
                                "turrets": 1,
                                "wards": 3
                              },
                              "kills": 1,
                              "kills_series": {
                                "double_kills": 0,
                                "penta_kills": 0,
                                "quadra_kills": 0,
                                "triple_kills": 0
                              },
                              "matches_lost": 1,
                              "matches_played": 1,
                              "matches_won": 0,
                              "wards_placed": 13
                            }
                          }
                        },
                        {
                          "first_name": "Martin",
                          "id": 1172,
                          "last_name": "Hansen",
                          "name": "Wunder",
                          "stats": {
                            "averages": {
                              "assists": 0,
                              "cs_at_14": 105,
                              "cs_diff_at_14": 16,
                              "deaths": 4,
                              "gold_earned": 9779,
                              "gold_percentage": 22.58,
                              "gold_spent": 9100,
                              "kill_counters": {
                                "inhibitors": 0,
                                "neutral_minions": 18,
                                "neutral_minions_enemy_jungle": 0,
                                "neutral_minions_team_jungle": 7,
                                "players": 0,
                                "turrets": 0,
                                "wards": 4
                              },
                              "kills": 0,
                              "magic_damage": {
                                "dealt": 12354,
                                "dealt_percentage": 5.09,
                                "dealt_to_champions": 501,
                                "dealt_to_champions_percentage": 2.15,
                                "taken": null
                              },
                              "minions_killed": 231,
                              "physical_damage": {
                                "dealt": 129752,
                                "dealt_percentage": 50.33,
                                "dealt_to_champions": 13235,
                                "dealt_to_champions_percentage": 57.56,
                                "taken": 7626
                              },
                              "total_damage": {
                                "dealt": 142107,
                                "dealt_percentage": 26.5,
                                "dealt_to_champions": 13736,
                                "dealt_to_champions_percentage": 28.61,
                                "taken": 15197
                              },
                              "total_heal": 866,
                              "total_time_crowd_control_dealt": 102,
                              "total_units_healed": 1,
                              "true_damage": {
                                "dealt": 0,
                                "dealt_percentage": 0,
                                "dealt_to_champions": 0,
                                "dealt_to_champions_percentage": 0,
                                "taken": 317
                              },
                              "vision_wards_bought_in_game": 4,
                              "wards_placed": 13
                            },
                            "games_count": 1,
                            "totals": {
                              "assists": 0,
                              "deaths": 4,
                              "games_lost": 1,
                              "games_played": 1,
                              "games_won": 0,
                              "kill_counters": {
                                "inhibitors": 0,
                                "turrets": 0,
                                "wards": 4
                              },
                              "kills": 0,
                              "kills_series": {
                                "double_kills": 0,
                                "penta_kills": 0,
                                "quadra_kills": 0,
                                "triple_kills": 0
                              },
                              "matches_lost": 1,
                              "matches_played": 1,
                              "matches_won": 0,
                              "wards_placed": 13
                            }
                          }
                        },
                        {
                          "first_name": "Marcin",
                          "id": 2147,
                          "last_name": "Jankowski",
                          "name": "Jankos",
                          "stats": {
                            "averages": {
                              "assists": 2,
                              "cs_at_14": 63,
                              "cs_diff_at_14": -8,
                              "deaths": 6,
                              "gold_earned": 7696,
                              "gold_percentage": 17.77,
                              "gold_spent": 7400,
                              "kill_counters": {
                                "inhibitors": 0,
                                "neutral_minions": 122,
                                "neutral_minions_enemy_jungle": 5,
                                "neutral_minions_team_jungle": 103,
                                "players": 0,
                                "turrets": 0,
                                "wards": 10
                              },
                              "kills": 0,
                              "magic_damage": {
                                "dealt": 15052,
                                "dealt_percentage": 6.2,
                                "dealt_to_champions": 249,
                                "dealt_to_champions_percentage": 1.07,
                                "taken": null
                              },
                              "minions_killed": 138,
                              "physical_damage": {
                                "dealt": 97019,
                                "dealt_percentage": 37.63,
                                "dealt_to_champions": 6264,
                                "dealt_to_champions_percentage": 27.24,
                                "taken": 15531
                              },
                              "total_damage": {
                                "dealt": 119610,
                                "dealt_percentage": 22.31,
                                "dealt_to_champions": 6589,
                                "dealt_to_champions_percentage": 13.73,
                                "taken": 21939
                              },
                              "total_heal": 7509,
                              "total_time_crowd_control_dealt": 206,
                              "total_units_healed": 1,
                              "true_damage": {
                                "dealt": 7539,
                                "dealt_percentage": 21.15,
                                "dealt_to_champions": 75,
                                "dealt_to_champions_percentage": 4.51,
                                "taken": 335
                              },
                              "vision_wards_bought_in_game": 7,
                              "wards_placed": 21
                            },
                            "games_count": 1,
                            "totals": {
                              "assists": 2,
                              "deaths": 6,
                              "games_lost": 1,
                              "games_played": 1,
                              "games_won": 0,
                              "kill_counters": {
                                "inhibitors": 0,
                                "turrets": 0,
                                "wards": 10
                              },
                              "kills": 0,
                              "kills_series": {
                                "double_kills": 0,
                                "penta_kills": 0,
                                "quadra_kills": 0,
                                "triple_kills": 0
                              },
                              "matches_lost": 1,
                              "matches_played": 1,
                              "matches_won": 0,
                              "wards_placed": 21
                            }
                          }
                        }
                      ],
                      "slug": "g2-esports"
                    }
                  ]
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLStatsForAllPlayersByMatch"
            }
          }
        },
        "description": "Statistics of all Lol players by match"
      }
    },
    "schemas": {
      "LoLStatsForAllPlayersByMatch": {
        "additionalProperties": false,
        "deprecated": false,
        "properties": {
          "teams": {
            "items": {
              "additionalProperties": false,
              "deprecated": false,
              "properties": {
                "id": {
                  "description": "The ID of the team.",
                  "minimum": 1,
                  "title": "TeamID",
                  "type": "integer"
                },
                "name": {
                  "description": "The name of the team.",
                  "title": "TeamName",
                  "type": "string"
                },
                "players": {
                  "items": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "first_name": {
                        "deprecated": false,
                        "description": "First name of the player. `null` if unknown",
                        "nullable": true,
                        "title": "PlayerFirstName",
                        "type": "string"
                      },
                      "id": {
                        "description": "ID of the player",
                        "minimum": 1,
                        "title": "PlayerID",
                        "type": "integer"
                      },
                      "last_name": {
                        "deprecated": false,
                        "description": "Last name of the player. `null` if unknown",
                        "nullable": true,
                        "title": "PlayerLastName",
                        "type": "string"
                      },
                      "name": {
                        "description": "Professional name of the player",
                        "title": "PlayerName",
                        "type": "string"
                      },
                      "stats": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "description": "Statistics for all players for a match",
                        "properties": {
                          "averages": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "assists": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAverageAssists",
                                "type": "number"
                              },
                              "cs_at_14": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LolAverageCreepScoreAt14",
                                "type": "number"
                              },
                              "cs_diff_at_14": {
                                "deprecated": false,
                                "description": "Player CS difference compared to their lane opponent at the 14th minute in-game",
                                "nullable": true,
                                "title": "LolAverageCreepScoreDifferenceAt14",
                                "type": "number"
                              },
                              "deaths": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAverageDeaths",
                                "type": "number"
                              },
                              "gold_earned": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAverageGoldEarned",
                                "type": "number"
                              },
                              "gold_percentage": {
                                "deprecated": false,
                                "description": "Percentage of gold the player had compared to the total gold of the team",
                                "maximum": 100,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLPlayerGoldErnedPercentage",
                                "type": "number"
                              },
                              "gold_spent": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAverageGoldSpent",
                                "type": "number"
                              },
                              "kill_counters": {
                                "additionalProperties": false,
                                "deprecated": false,
                                "properties": {
                                  "inhibitors": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageInhibitorKills",
                                    "type": "number"
                                  },
                                  "neutral_minions": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageNeutralMinionKills",
                                    "type": "number"
                                  },
                                  "neutral_minions_enemy_jungle": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageMinionsEnemyJungleKills",
                                    "type": "number"
                                  },
                                  "neutral_minions_team_jungle": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageMinionsTeamJungleKills",
                                    "type": "number"
                                  },
                                  "players": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageKills",
                                    "type": "number"
                                  },
                                  "turrets": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageTurretKills",
                                    "type": "number"
                                  },
                                  "wards": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageWardKills",
                                    "type": "number"
                                  }
                                },
                                "required": [
                                  "inhibitors",
                                  "neutral_minions",
                                  "neutral_minions_enemy_jungle",
                                  "neutral_minions_team_jungle",
                                  "players",
                                  "turrets",
                                  "wards"
                                ],
                                "title": "LoLAverageKillCounters",
                                "type": "object"
                              },
                              "kills": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAverageKills",
                                "type": "number"
                              },
                              "magic_damage": {
                                "additionalProperties": false,
                                "deprecated": false,
                                "properties": {
                                  "dealt": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealt",
                                    "type": "number"
                                  },
                                  "dealt_percentage": {
                                    "deprecated": false,
                                    "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                                    "maximum": 100,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtPercentage",
                                    "type": "number"
                                  },
                                  "dealt_to_champions": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtToChampions",
                                    "type": "number"
                                  },
                                  "dealt_to_champions_percentage": {
                                    "deprecated": false,
                                    "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                                    "maximum": 100,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtToChampionsPercentage",
                                    "type": "number"
                                  },
                                  "taken": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageTaken",
                                    "type": "number"
                                  }
                                },
                                "required": [
                                  "dealt",
                                  "dealt_percentage",
                                  "dealt_to_champions",
                                  "dealt_to_champions_percentage",
                                  "taken"
                                ],
                                "title": "LoLAverageMagicDamage",
                                "type": "object"
                              },
                              "minions_killed": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAverageMinionsKilled",
                                "type": "number"
                              },
                              "physical_damage": {
                                "additionalProperties": false,
                                "deprecated": false,
                                "properties": {
                                  "dealt": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealt",
                                    "type": "number"
                                  },
                                  "dealt_percentage": {
                                    "deprecated": false,
                                    "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                                    "maximum": 100,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtPercentage",
                                    "type": "number"
                                  },
                                  "dealt_to_champions": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtToChampions",
                                    "type": "number"
                                  },
                                  "dealt_to_champions_percentage": {
                                    "deprecated": false,
                                    "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                                    "maximum": 100,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtToChampionsPercentage",
                                    "type": "number"
                                  },
                                  "taken": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageTaken",
                                    "type": "number"
                                  }
                                },
                                "required": [
                                  "dealt",
                                  "dealt_percentage",
                                  "dealt_to_champions",
                                  "dealt_to_champions_percentage",
                                  "taken"
                                ],
                                "title": "LoLAveragePhysicalDamage",
                                "type": "object"
                              },
                              "total_damage": {
                                "additionalProperties": false,
                                "deprecated": false,
                                "properties": {
                                  "dealt": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealt",
                                    "type": "number"
                                  },
                                  "dealt_percentage": {
                                    "deprecated": false,
                                    "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                                    "maximum": 100,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtPercentage",
                                    "type": "number"
                                  },
                                  "dealt_to_champions": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtToChampions",
                                    "type": "number"
                                  },
                                  "dealt_to_champions_percentage": {
                                    "deprecated": false,
                                    "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                                    "maximum": 100,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtToChampionsPercentage",
                                    "type": "number"
                                  },
                                  "taken": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageTaken",
                                    "type": "number"
                                  }
                                },
                                "required": [
                                  "dealt",
                                  "dealt_percentage",
                                  "dealt_to_champions",
                                  "dealt_to_champions_percentage",
                                  "taken"
                                ],
                                "title": "LoLAverageTotalDamage",
                                "type": "object"
                              },
                              "total_heal": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAverageTotalHeal",
                                "type": "number"
                              },
                              "total_time_crowd_control_dealt": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAverageTotalTimeCrowdControlDealt",
                                "type": "number"
                              },
                              "total_units_healed": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAverageTotalUnitsHealed",
                                "type": "number"
                              },
                              "true_damage": {
                                "additionalProperties": false,
                                "deprecated": false,
                                "properties": {
                                  "dealt": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealt",
                                    "type": "number"
                                  },
                                  "dealt_percentage": {
                                    "deprecated": false,
                                    "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                                    "maximum": 100,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtPercentage",
                                    "type": "number"
                                  },
                                  "dealt_to_champions": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtToChampions",
                                    "type": "number"
                                  },
                                  "dealt_to_champions_percentage": {
                                    "deprecated": false,
                                    "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                                    "maximum": 100,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageDealtToChampionsPercentage",
                                    "type": "number"
                                  },
                                  "taken": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLAverageDamageTaken",
                                    "type": "number"
                                  }
                                },
                                "required": [
                                  "dealt",
                                  "dealt_percentage",
                                  "dealt_to_champions",
                                  "dealt_to_champions_percentage",
                                  "taken"
                                ],
                                "title": "LoLAverageTrueDamage",
                                "type": "object"
                              },
                              "vision_wards_bought_in_game": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAverageVisionWardsBoughtInGame",
                                "type": "number"
                              },
                              "wards_placed": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAverageWardsPlaced",
                                "type": "number"
                              }
                            },
                            "required": [
                              "assists",
                              "cs_at_14",
                              "cs_diff_at_14",
                              "deaths",
                              "gold_earned",
                              "gold_percentage",
                              "gold_spent",
                              "kill_counters",
                              "kills",
                              "magic_damage",
                              "minions_killed",
                              "physical_damage",
                              "total_damage",
                              "total_heal",
                              "total_time_crowd_control_dealt",
                              "total_units_healed",
                              "true_damage",
                              "vision_wards_bought_in_game",
                              "wards_placed"
                            ],
                            "title": "LoLPlayerAverages",
                            "type": "object"
                          },
                          "games_count": {
                            "deprecated": false,
                            "description": "Number of games",
                            "minimum": 0,
                            "nullable": true,
                            "title": "GameCount",
                            "type": "integer"
                          },
                          "totals": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "assists": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLAssistCount",
                                "type": "integer"
                              },
                              "deaths": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLDeathCount",
                                "type": "integer"
                              },
                              "games_lost": {
                                "deprecated": false,
                                "description": "Number of games",
                                "minimum": 0,
                                "nullable": true,
                                "title": "GameCount",
                                "type": "integer"
                              },
                              "games_played": {
                                "deprecated": false,
                                "description": "Number of games",
                                "minimum": 0,
                                "nullable": true,
                                "title": "GameCount",
                                "type": "integer"
                              },
                              "games_won": {
                                "deprecated": false,
                                "description": "Number of games",
                                "minimum": 0,
                                "nullable": true,
                                "title": "GameCount",
                                "type": "integer"
                              },
                              "kill_counters": {
                                "additionalProperties": false,
                                "deprecated": false,
                                "properties": {
                                  "inhibitors": {
                                    "deprecated": false,
                                    "description": "Number of inhibitors killed by the player",
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLInhibitorCount",
                                    "type": "integer"
                                  },
                                  "turrets": {
                                    "deprecated": false,
                                    "description": "Number of turrets killed",
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLTurretCount",
                                    "type": "integer"
                                  },
                                  "wards": {
                                    "deprecated": false,
                                    "description": "Number of wards killed by the player",
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLWardCount",
                                    "type": "integer"
                                  }
                                },
                                "required": [
                                  "inhibitors",
                                  "turrets",
                                  "wards"
                                ],
                                "title": "LoLPlayerTotalKillCounters",
                                "type": "object"
                              },
                              "kills": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLKillCount",
                                "type": "integer"
                              },
                              "kills_series": {
                                "additionalProperties": false,
                                "deprecated": false,
                                "properties": {
                                  "double_kills": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLKillsSerieDouble",
                                    "type": "integer"
                                  },
                                  "penta_kills": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLKillsSeriePenta",
                                    "type": "integer"
                                  },
                                  "quadra_kills": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLKillsSerieQuadra",
                                    "type": "integer"
                                  },
                                  "triple_kills": {
                                    "deprecated": false,
                                    "minimum": 0,
                                    "nullable": true,
                                    "title": "LoLKillsSerieTriple",
                                    "type": "integer"
                                  }
                                },
                                "required": [
                                  "double_kills",
                                  "penta_kills",
                                  "quadra_kills",
                                  "triple_kills"
                                ],
                                "title": "LoLKillsSeries",
                                "type": "object"
                              },
                              "matches_lost": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "MatchCount",
                                "type": "integer"
                              },
                              "matches_played": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "MatchCount",
                                "type": "integer"
                              },
                              "matches_won": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "MatchCount",
                                "type": "integer"
                              },
                              "wards_placed": {
                                "deprecated": false,
                                "minimum": 0,
                                "nullable": true,
                                "title": "LoLWardsPlaced",
                                "type": "integer"
                              }
                            },
                            "required": [
                              "assists",
                              "deaths",
                              "games_lost",
                              "games_played",
                              "games_won",
                              "kill_counters",
                              "kills",
                              "kills_series",
                              "matches_lost",
                              "matches_played",
                              "matches_won",
                              "wards_placed"
                            ],
                            "title": "LoLPlayerStatsTotals",
                            "type": "object"
                          }
                        },
                        "required": [
                          "averages",
                          "games_count",
                          "totals"
                        ],
                        "title": "LoLPlayerStatsForAllPlayersByMatch",
                        "type": "object"
                      }
                    },
                    "required": [
                      "first_name",
                      "id",
                      "last_name",
                      "name",
                      "stats"
                    ],
                    "title": "LoLPlayerForAllStatsPlayers",
                    "type": "object"
                  },
                  "title": "LoLPlayersForAllStatsPlayers",
                  "type": "array"
                },
                "slug": {
                  "minLength": 1,
                  "pattern": "^[a-z0-9_-]+$",
                  "title": "TeamSlug",
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "players",
                "slug"
              ],
              "title": "LoLTeamForAllStatsPlayers",
              "type": "object"
            },
            "title": "LoLTeamsForAllStatsPlayers",
            "type": "array"
          }
        },
        "required": [
          "teams"
        ],
        "title": "LoLStatsForAllPlayersByMatch",
        "type": "object"
      },
      "MatchIDOrSlug": {
        "description": "A match ID or slug",
        "oneOf": [
          {
            "minimum": 1,
            "title": "MatchID",
            "type": "integer"
          },
          {
            "minLength": 1,
            "pattern": "^[ a-zA-Z0-9_-]+$",
            "title": "MatchSlug",
            "type": "string"
          }
        ],
        "title": "MatchIDOrSlug"
      }
    },
    "securitySchemes": {
      "BearerToken": {
        "scheme": "bearer",
        "type": "http"
      },
      "QueryToken": {
        "in": "query",
        "name": "token",
        "type": "apiKey"
      }
    }
  },
  "info": {
    "title": "League of Legends",
    "version": "2.62.8"
  },
  "openapi": "3.0.0",
  "paths": {
    "/lol/matches/{match_id_or_slug}/players/stats": {
      "get": {
        "description": "Get detailed statistics of League-of-Legends players for the given match\n> ℹ️  \n> \n> This endpoint is only available to customers with a historical or real-time data plan",
        "operationId": "get_lol_matches_matchIdOrSlug_players_stats",
        "parameters": [
          {
            "description": "A match ID or slug",
            "in": "path",
            "name": "match_id_or_slug",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/MatchIDOrSlug"
            }
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLStatsForAllPlayersByMatch"
          },
          "400": {
            "$ref": "#/components/responses/Error400"
          },
          "401": {
            "$ref": "#/components/responses/Error401"
          },
          "403": {
            "$ref": "#/components/responses/Error403"
          },
          "404": {
            "$ref": "#/components/responses/Error404"
          },
          "422": {
            "$ref": "#/components/responses/Error422"
          }
        },
        "summary": "Get stats for LoL players on match",
        "tags": [
          "LoL stats"
        ],
        "x-pandascore-plan": "Historical plan",
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/matches/{match_id_or_slug}/players/stats' \\\n     --header 'accept: application/json'\n",
              "language": "curl"
            }
          ]
        }
      }
    }
  },
  "security": [
    {
      "BearerToken": []
    },
    {
      "QueryToken": []
    }
  ],
  "servers": [
    {
      "url": "https://api.pandascore.co/",
      "variables": {}
    }
  ],
  "x-readme": {
    "explorer-enabled": false,
    "samples-languages": [
      "curl"
    ]
  }
}
```