> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get stats for LoL team

Get detailed statistics of a given League-of-Legends team
> ℹ️  
> 
> This endpoint is only available to customers with a historical or real-time data plan

# OpenAPI definition

```json
{
  "components": {
    "parameters": {
      "GamesCount": {
        "description": "The amount of games used for the statistics.\n\nFor example if `?games_count=5`, it would show the statistics for the most recent 5 games played\n",
        "in": "query",
        "name": "games_count",
        "required": false,
        "schema": {
          "type": "integer"
        }
      },
      "LoLStatsSide": {
        "in": "query",
        "name": "side",
        "required": false,
        "schema": {
          "enum": [
            "blue",
            "red"
          ],
          "type": "string"
        }
      },
      "StatsFrom": {
        "description": "Filter out 'from' date",
        "in": "query",
        "name": "from",
        "required": false,
        "schema": {
          "example": "2017-07-21",
          "format": "date",
          "type": "string"
        }
      },
      "StatsTo": {
        "description": "Filter out 'to' date",
        "in": "query",
        "name": "to",
        "required": false,
        "schema": {
          "example": "2017-07-21",
          "format": "date",
          "type": "string"
        }
      },
      "StatsVideogameVersion": {
        "in": "query",
        "name": "videogame_version",
        "required": false,
        "schema": {
          "$ref": "#/components/schemas/VideogameVersionOrAll"
        }
      }
    },
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
      "LoLStatsForTeam": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/teams/126061/stats?from=2022-01-17&to=2022-07-01": {
                "description": "/lol/teams/126061/stats?from=2022-01-17&to=2022-07-01",
                "value": {
                  "acronym": "T1",
                  "dark_mode_image_url": null,
                  "id": 126061,
                  "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                  "last_games": [
                    {
                      "begin_at": "2022-07-01T12:02:56Z",
                      "complete": true,
                      "detailed_stats": true,
                      "end_at": "2022-07-01T12:46:32Z",
                      "finished": true,
                      "forfeit": false,
                      "id": 235730,
                      "length": 1795,
                      "match_id": 637573,
                      "players": [
                        {
                          "assists": 7,
                          "champion": {
                            "id": 3098,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/f832bf9dbd11be46cc18f7635eea5348.png",
                            "name": "Swain",
                            "slug": "Swain"
                          },
                          "creep_score": 258,
                          "cs_at_14": 132,
                          "cs_diff_at_14": -18,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235730,
                          "gold_earned": 10833,
                          "gold_percentage": 19.36,
                          "gold_spent": 10600,
                          "items": [
                            {
                              "id": 2642,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d3c7dce8ed50a8553198bdefbacac855.png",
                              "is_trinket": false,
                              "name": "Needlessly Large Rod"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2720,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d703d8cf515d6fef18fdbacd320248ad.png",
                              "is_trinket": false,
                              "name": "Imperial Mandate"
                            },
                            {
                              "id": 2776,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/000057177c6cd0f3895e67b2199dacb9.png",
                              "is_trinket": false,
                              "name": "Zhonya's Hourglass"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2924,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d4fde29e50e7ed8472b31f4a78134063.png",
                              "is_trinket": false,
                              "name": "Rylai's Crystal Scepter"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 20,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 0,
                            "turrets": 1,
                            "wards": 5
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 118849,
                            "dealt_percentage": 39.39,
                            "dealt_to_champions": 10206,
                            "dealt_to_champions_percentage": 41.56,
                            "taken": 10784
                          },
                          "masteries": [],
                          "minions_killed": 258,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 17965,
                            "dealt_percentage": 5.05,
                            "dealt_to_champions": 642,
                            "dealt_to_champions_percentage": 2.11,
                            "taken": 5799
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-05-07",
                            "first_name": "Lee",
                            "id": 585,
                            "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                            "last_name": "Sang-hyeok",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Faker",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "faker"
                          },
                          "player_id": 585,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 138325,
                            "dealt_percentage": 19.78,
                            "dealt_to_champions": 10848,
                            "dealt_to_champions_percentage": 17.03,
                            "taken": 17361
                          },
                          "total_heal": 6074,
                          "total_time_crowd_control_dealt": 262,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 1510,
                            "dealt_percentage": 3.65,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 777
                          },
                          "wards": {
                            "placed": 16,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 6
                          },
                          "wards_placed": 16
                        },
                        {
                          "assists": 1,
                          "champion": {
                            "id": 3031,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/e05b5fd8059a74ff2a93e5e470865b11.png",
                            "name": "Kalista",
                            "slug": "Kalista"
                          },
                          "creep_score": 291,
                          "cs_at_14": 133,
                          "cs_diff_at_14": 120,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235730,
                          "gold_earned": 11535,
                          "gold_percentage": 24.24,
                          "gold_spent": 11375,
                          "items": [
                            {
                              "id": 2459,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/a6e22f9da01ca771ca63126e1ff93ac6.png",
                              "is_trinket": false,
                              "name": "Recurve Bow"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2544,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/924cb9f122b90bf1ee29b9650c092524.png",
                              "is_trinket": false,
                              "name": "Guinsoo's Rageblade"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2699,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/0f33f102856e8d40f6d38ff057856e1d.png",
                              "is_trinket": false,
                              "name": "Immortal Shieldbow"
                            },
                            {
                              "id": 2763,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1a0dab15964871b507375c342d5536bc.png",
                              "is_trinket": false,
                              "name": "Runaan's Hurricane"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 28,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 1,
                            "wards": 16
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 233,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 14,
                          "magic_damage": {
                            "dealt": 4606,
                            "dealt_percentage": 1.67,
                            "dealt_to_champions": 731,
                            "dealt_to_champions_percentage": 2.26,
                            "taken": 4171
                          },
                          "masteries": [],
                          "minions_killed": 291,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 159617,
                            "dealt_percentage": 49.91,
                            "dealt_to_champions": 7957,
                            "dealt_to_champions_percentage": 52.62,
                            "taken": 7119
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-10-23",
                            "first_name": "Kim",
                            "id": 2169,
                            "image_url": "https://cdn.pandascore.co/images/player/image/2169/ezgif_3_4d5729796f.png",
                            "last_name": "Hyuk-kyu",
                            "modified_at": "2024-10-29T18:44:18Z",
                            "name": "Deft",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "deft"
                          },
                          "player_id": 2169,
                          "role": "adc",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 23,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/65eea722a1fc79fb6469e7246eb0afb8.png",
                              "name": "Cleanse"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 167632,
                            "dealt_percentage": 25.38,
                            "dealt_to_champions": 8800,
                            "dealt_to_champions_percentage": 16.15,
                            "taken": 11546
                          },
                          "total_heal": 105,
                          "total_time_crowd_control_dealt": 321,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 3408,
                            "dealt_percentage": 5.25,
                            "dealt_to_champions": 112,
                            "dealt_to_champions_percentage": 1.6,
                            "taken": 255
                          },
                          "wards": {
                            "placed": 16,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 7
                          },
                          "wards_placed": 16
                        },
                        {
                          "assists": 8,
                          "champion": {
                            "id": 3087,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/596326c80f939f6cafdb73d9e5917311.png",
                            "name": "Seraphine",
                            "slug": "Seraphine"
                          },
                          "creep_score": 266,
                          "cs_at_14": 106,
                          "cs_diff_at_14": 103,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": true,
                            "first_tower_kill": false
                          },
                          "game_id": 235730,
                          "gold_earned": 12014,
                          "gold_percentage": 21.47,
                          "gold_spent": 9200,
                          "items": [
                            {
                              "id": 2467,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/e914701535346c87ea1cfb1fb159631c.png",
                              "is_trinket": false,
                              "name": "Dark Seal"
                            },
                            {
                              "id": 2642,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d3c7dce8ed50a8553198bdefbacac855.png",
                              "is_trinket": false,
                              "name": "Needlessly Large Rod"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2871,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/8cef60e74adf20cb8372afd4aa49cde9.png",
                              "is_trinket": false,
                              "name": "Liandry's Anguish"
                            },
                            {
                              "id": 2919,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/47c001c40f4d6d169be155b0a74e08d5.png",
                              "is_trinket": false,
                              "name": "Seraph's Embrace"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 3,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 4,
                            "turrets": 1,
                            "wards": 2
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 4,
                          "largest_multi_kill": 1,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 159769,
                            "dealt_percentage": 52.96,
                            "dealt_to_champions": 10202,
                            "dealt_to_champions_percentage": 41.55,
                            "taken": 1763
                          },
                          "masteries": [],
                          "minions_killed": 266,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 12282,
                            "dealt_percentage": 3.45,
                            "dealt_to_champions": 721,
                            "dealt_to_champions_percentage": 2.38,
                            "taken": 4405
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-10-14",
                            "first_name": "Ryu",
                            "id": 8158,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                            "last_name": "Min-seok",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Keria",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "keria"
                          },
                          "player_id": 8158,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 183480,
                            "dealt_percentage": 26.24,
                            "dealt_to_champions": 11150,
                            "dealt_to_champions_percentage": 17.5,
                            "taken": 6287
                          },
                          "total_heal": 5494,
                          "total_time_crowd_control_dealt": 270,
                          "total_units_healed": 5,
                          "true_damage": {
                            "dealt": 11428,
                            "dealt_percentage": 27.61,
                            "dealt_to_champions": 226,
                            "dealt_to_champions_percentage": 2.57,
                            "taken": 117
                          },
                          "wards": {
                            "placed": 20,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 10
                          },
                          "wards_placed": 20
                        },
                        {
                          "assists": 1,
                          "champion": {
                            "id": 3018,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/a7483c3b14ed866fecd8726a1046187b.png",
                            "name": "Gwen",
                            "slug": "Gwen"
                          },
                          "creep_score": 229,
                          "cs_at_14": 107,
                          "cs_diff_at_14": -12,
                          "deaths": 5,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235730,
                          "gold_earned": 9257,
                          "gold_percentage": 19.45,
                          "gold_spent": 9225,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2534,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/73578d8f7a2a451b61696009016c134a.png",
                              "is_trinket": false,
                              "name": "Fiendish Codex"
                            },
                            {
                              "id": 2640,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/178aee5eaa5e7a70f6a05155b7dcf3e2.png",
                              "is_trinket": false,
                              "name": "Doran's Shield"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2907,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3f929f236ba0734da501690a3c38174.png",
                              "is_trinket": false,
                              "name": "Demonic Embrace"
                            },
                            {
                              "id": 3017,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/81cd1acbc7ee06bec32014055901b37e.png",
                              "is_trinket": false,
                              "name": "Riftmaker"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 12,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 0,
                            "turrets": 0,
                            "wards": 4
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 14,
                          "magic_damage": {
                            "dealt": 48098,
                            "dealt_percentage": 17.44,
                            "dealt_to_champions": 8454,
                            "dealt_to_champions_percentage": 26.12,
                            "taken": 5406
                          },
                          "masteries": [],
                          "minions_killed": 229,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 37521,
                            "dealt_percentage": 11.73,
                            "dealt_to_champions": 2255,
                            "dealt_to_champions_percentage": 14.91,
                            "taken": 15377
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-03-11",
                            "first_name": "Hwang",
                            "id": 8172,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8172/drx_kingen_2022_split_2.png",
                            "last_name": "Seong-hoon",
                            "modified_at": "2026-01-06T07:15:57Z",
                            "name": "Kingen",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "kingen"
                          },
                          "player_id": 8172,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 117555,
                            "dealt_percentage": 17.8,
                            "dealt_to_champions": 15364,
                            "dealt_to_champions_percentage": 28.2,
                            "taken": 26352
                          },
                          "total_heal": 2509,
                          "total_time_crowd_control_dealt": 35,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 31934,
                            "dealt_percentage": 49.15,
                            "dealt_to_champions": 4654,
                            "dealt_to_champions_percentage": 66.59,
                            "taken": 5568
                          },
                          "wards": {
                            "placed": 8,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 5
                          },
                          "wards_placed": 8
                        },
                        {
                          "assists": 2,
                          "champion": {
                            "id": 3078,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/317910590c455560440d40dd9bbdd368.png",
                            "name": "Renata Glasc",
                            "slug": "Renata"
                          },
                          "creep_score": 15,
                          "cs_at_14": 3,
                          "cs_diff_at_14": -103,
                          "deaths": 4,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235730,
                          "gold_earned": 6027,
                          "gold_percentage": 12.66,
                          "gold_spent": 5600,
                          "items": [
                            {
                              "id": 2472,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6cf6837b7cc656d332c883d0ebde2f67.png",
                              "is_trinket": false,
                              "name": "Refillable Potion"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2761,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/b4754269-dc0f-474a-a3b4-c181b7d6d26c.png",
                              "is_trinket": false,
                              "name": "Shurelya's Battlesong"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 0,
                            "turrets": 0,
                            "wards": 14
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 11,
                          "magic_damage": {
                            "dealt": 12300,
                            "dealt_percentage": 4.46,
                            "dealt_to_champions": 1932,
                            "dealt_to_champions_percentage": 5.97,
                            "taken": 6502
                          },
                          "masteries": [],
                          "minions_killed": 15,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 3792,
                            "dealt_percentage": 1.19,
                            "dealt_to_champions": 653,
                            "dealt_to_champions_percentage": 4.32,
                            "taken": 3938
                          },
                          "player": {
                            "active": true,
                            "age": 28,
                            "birthday": "1997-04-01",
                            "first_name": "Cho",
                            "id": 15425,
                            "image_url": "https://cdn.pandascore.co/images/player/image/15425/drx_bery_l_2022_split_2.png",
                            "last_name": "Geon-hee",
                            "modified_at": "2025-12-30T12:27:51Z",
                            "name": "BeryL",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "beryl"
                          },
                          "player_id": 15425,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 17120,
                            "dealt_percentage": 2.59,
                            "dealt_to_champions": 3612,
                            "dealt_to_champions_percentage": 6.63,
                            "taken": 11371
                          },
                          "total_heal": 853,
                          "total_time_crowd_control_dealt": 138,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 1027,
                            "dealt_percentage": 1.58,
                            "dealt_to_champions": 1027,
                            "dealt_to_champions_percentage": 14.69,
                            "taken": 930
                          },
                          "wards": {
                            "placed": 45,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 20
                          },
                          "wards_placed": 45
                        },
                        {
                          "assists": 12,
                          "champion": {
                            "id": 3147,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/8f448f569bc040fbeaf36de3805ed2eb.png",
                            "name": "Senna",
                            "slug": "Senna"
                          },
                          "creep_score": 47,
                          "cs_at_14": 13,
                          "cs_diff_at_14": -120,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": true,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": true
                          },
                          "game_id": 235730,
                          "gold_earned": 9332,
                          "gold_percentage": 16.67,
                          "gold_spent": 8000,
                          "items": [
                            {
                              "id": 2446,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/0421f84dc8dd53dcb0e9d5a525145979.png",
                              "is_trinket": false,
                              "name": "Cloak of Agility"
                            },
                            {
                              "id": 2489,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7c39a6acc5d50b697a09e78338c3d4a0.png",
                              "is_trinket": false,
                              "name": "Boots of Swiftness"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2806,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/f530d00c32c745acf57bf0521cf565f7.png",
                              "is_trinket": false,
                              "name": "Black Mist Scythe"
                            },
                            {
                              "id": 2912,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/eaef5f4c2f6f2d5fcf13f287c321e59b.png",
                              "is_trinket": false,
                              "name": "Eclipse"
                            },
                            {
                              "id": 2963,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/b024e8ca8cf9873201744933ec14c30c.png",
                              "is_trinket": false,
                              "name": "Umbral Glaive"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 2,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 1,
                            "wards": 27
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 420,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 12,
                          "magic_damage": {
                            "dealt": 56,
                            "dealt_percentage": 0.02,
                            "dealt_to_champions": 56,
                            "dealt_to_champions_percentage": 0.23,
                            "taken": 3942
                          },
                          "masteries": [],
                          "minions_killed": 47,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 48598,
                            "dealt_percentage": 13.65,
                            "dealt_to_champions": 10487,
                            "dealt_to_champions_percentage": 34.55,
                            "taken": 2664
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-02-06",
                            "first_name": "Lee",
                            "id": 19285,
                            "image_url": "https://cdn.pandascore.co/images/player/image/19285/t1_gumayusi_2023_split_2.png",
                            "last_name": "Min-hyeon",
                            "modified_at": "2026-01-06T07:15:49Z",
                            "name": "Gumayusi",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "gumayusi"
                          },
                          "player_id": 19285,
                          "role": "adc",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 27,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/37e058ce96cf92adf6831ad5946956f4.png",
                              "name": "Exhaust"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 48994,
                            "dealt_percentage": 7.01,
                            "dealt_to_champions": 10775,
                            "dealt_to_champions_percentage": 16.92,
                            "taken": 6801
                          },
                          "total_heal": 7421,
                          "total_time_crowd_control_dealt": 204,
                          "total_units_healed": 5,
                          "true_damage": {
                            "dealt": 338,
                            "dealt_percentage": 0.82,
                            "dealt_to_champions": 231,
                            "dealt_to_champions_percentage": 2.63,
                            "taken": 194
                          },
                          "wards": {
                            "placed": 33,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 8
                          },
                          "wards_placed": 33
                        },
                        {
                          "assists": 1,
                          "champion": {
                            "id": 3070,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/4d7a4c3082977a3a10be591b1110bfc6.png",
                            "name": "Poppy",
                            "slug": "Poppy"
                          },
                          "creep_score": 173,
                          "cs_at_14": 97,
                          "cs_diff_at_14": 7,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235730,
                          "gold_earned": 8627,
                          "gold_percentage": 18.13,
                          "gold_spent": 8350,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2881,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1e0b1c90b92e68856c4c8623b98cc24f.png",
                              "is_trinket": false,
                              "name": "Dead Man's Plate"
                            },
                            {
                              "id": 3020,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/49ca044dd30a7b6495d9b99f699e20ec.png",
                              "is_trinket": false,
                              "name": "Turbo Chemtank"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 155,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 0,
                            "turrets": 1,
                            "wards": 14
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 13,
                          "magic_damage": {
                            "dealt": 32438,
                            "dealt_percentage": 11.76,
                            "dealt_to_champions": 994,
                            "dealt_to_champions_percentage": 3.07,
                            "taken": 6131
                          },
                          "masteries": [],
                          "minions_killed": 173,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 100052,
                            "dealt_percentage": 31.28,
                            "dealt_to_champions": 3954,
                            "dealt_to_champions_percentage": 26.15,
                            "taken": 12172
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-03-21",
                            "first_name": "Hong",
                            "id": 24996,
                            "image_url": "https://cdn.pandascore.co/images/player/image/24996/tl_pyosik_2023_split_1.png",
                            "last_name": "Chang-hyeon",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "Pyosik",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "pyosik"
                          },
                          "player_id": 24996,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 147961,
                            "dealt_percentage": 22.4,
                            "dealt_to_champions": 5453,
                            "dealt_to_champions_percentage": 10.01,
                            "taken": 19884
                          },
                          "total_heal": 6491,
                          "total_time_crowd_control_dealt": 752,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 15469,
                            "dealt_percentage": 23.81,
                            "dealt_to_champions": 504,
                            "dealt_to_champions_percentage": 7.21,
                            "taken": 1580
                          },
                          "wards": {
                            "placed": 15,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 16
                          },
                          "wards_placed": 15
                        },
                        {
                          "assists": 0,
                          "champion": {
                            "id": 3121,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/1a602e7dc475be3ca9ccba41689c71d3.png",
                            "name": "Viktor",
                            "slug": "Viktor"
                          },
                          "creep_score": 316,
                          "cs_at_14": 150,
                          "cs_diff_at_14": 18,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235730,
                          "gold_earned": 12146,
                          "gold_percentage": 25.52,
                          "gold_spent": 12195,
                          "items": [
                            {
                              "id": 2460,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/0f07d995a4de9dc12ffaf8c403658755.png",
                              "is_trinket": false,
                              "name": "Amplifying Tome"
                            },
                            {
                              "id": 2480,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/49631901cd0f2419b756e4118109e312.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2871,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/8cef60e74adf20cb8372afd4aa49cde9.png",
                              "is_trinket": false,
                              "name": "Liandry's Anguish"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2907,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3f929f236ba0734da501690a3c38174.png",
                              "is_trinket": false,
                              "name": "Demonic Embrace"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 20,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 0,
                            "wards": 4
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 178287,
                            "dealt_percentage": 64.66,
                            "dealt_to_champions": 20251,
                            "dealt_to_champions_percentage": 62.58,
                            "taken": 4649
                          },
                          "masteries": [],
                          "minions_killed": 316,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 18847,
                            "dealt_percentage": 5.89,
                            "dealt_to_champions": 304,
                            "dealt_to_champions_percentage": 2.01,
                            "taken": 6175
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-11-28",
                            "first_name": "Kim",
                            "id": 25391,
                            "image_url": "https://cdn.pandascore.co/images/player/image/25391/drx_zeka_2022_split_2.png",
                            "last_name": "Geon-woo",
                            "modified_at": "2026-01-06T07:15:50Z",
                            "name": "Zeka",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "zeka"
                          },
                          "player_id": 25391,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 210267,
                            "dealt_percentage": 31.83,
                            "dealt_to_champions": 21248,
                            "dealt_to_champions_percentage": 39,
                            "taken": 11881
                          },
                          "total_heal": 485,
                          "total_time_crowd_control_dealt": 190,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 13132,
                            "dealt_percentage": 20.21,
                            "dealt_to_champions": 692,
                            "dealt_to_champions_percentage": 9.9,
                            "taken": 1056
                          },
                          "wards": {
                            "placed": 18,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 8
                          },
                          "wards_placed": 18
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 3010,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/021d3dbf409641c5de3ec1aa8c9d2eae.png",
                            "name": "Fiora",
                            "slug": "Fiora"
                          },
                          "creep_score": 266,
                          "cs_at_14": 119,
                          "cs_diff_at_14": 12,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235730,
                          "gold_earned": 12517,
                          "gold_percentage": 22.36,
                          "gold_spent": 10550,
                          "items": [
                            {
                              "id": 2537,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                              "is_trinket": false,
                              "name": "Mercury's Treads"
                            },
                            {
                              "id": 2545,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6b020a14738ad8a55ba4188c2b1b66fb.png",
                              "is_trinket": false,
                              "name": "Caulfield's Warhammer"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2928,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6a940e698e30b4298a0e176358d10a66.png",
                              "is_trinket": false,
                              "name": "Ravenous Hydra"
                            },
                            {
                              "id": 2935,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/97032f4cae42f011b132d0bca2438e8b.png",
                              "is_trinket": false,
                              "name": "Goredrinker"
                            },
                            {
                              "id": 3010,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6d6044334cc5fca47e413b13d2126a3a.png",
                              "is_trinket": false,
                              "name": "Executioner's Calling"
                            }
                          ],
                          "kills": 5,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 12,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 5,
                            "turrets": 3,
                            "wards": 5
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 582,
                          "largest_killing_spree": 5,
                          "largest_multi_kill": 2,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 2855,
                            "dealt_percentage": 0.95,
                            "dealt_to_champions": 2195,
                            "dealt_to_champions_percentage": 8.94,
                            "taken": 11057
                          },
                          "masteries": [],
                          "minions_killed": 266,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 138441,
                            "dealt_percentage": 38.88,
                            "dealt_to_champions": 10093,
                            "dealt_to_champions_percentage": 33.25,
                            "taken": 15221
                          },
                          "player": {
                            "active": true,
                            "age": 21,
                            "birthday": "2004-01-31",
                            "first_name": "Choi",
                            "id": 31391,
                            "image_url": "https://cdn.pandascore.co/images/player/image/31391/t1_zeus_2023_split_2.png",
                            "last_name": "Woo-je",
                            "modified_at": "2026-01-06T07:15:50Z",
                            "name": "Zeus",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "zeus-choi-woo-je"
                          },
                          "player_id": 31391,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 29,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/58955cb861c3b51375948a05e260996a.png",
                              "name": "Ghost"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 152597,
                            "dealt_percentage": 21.82,
                            "dealt_to_champions": 19599,
                            "dealt_to_champions_percentage": 30.77,
                            "taken": 31757
                          },
                          "total_heal": 9307,
                          "total_time_crowd_control_dealt": 112,
                          "total_units_healed": 8,
                          "true_damage": {
                            "dealt": 11301,
                            "dealt_percentage": 27.3,
                            "dealt_to_champions": 7310,
                            "dealt_to_champions_percentage": 83.26,
                            "taken": 5477
                          },
                          "wards": {
                            "placed": 8,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 4
                          },
                          "wards_placed": 8
                        },
                        {
                          "assists": 9,
                          "champion": {
                            "id": 3120,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/cbc53ec5b2ef342a710ba2c56ca13915.png",
                            "name": "Viego",
                            "slug": "Viego"
                          },
                          "creep_score": 188,
                          "cs_at_14": 90,
                          "cs_diff_at_14": -7,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": true,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235730,
                          "gold_earned": 11271,
                          "gold_percentage": 20.14,
                          "gold_spent": 9625,
                          "items": [
                            {
                              "id": 2480,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/49631901cd0f2419b756e4118109e312.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            },
                            {
                              "id": 2537,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                              "is_trinket": false,
                              "name": "Mercury's Treads"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2688,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c38d52b6bb9b984bf353c56585dae43d.png",
                              "is_trinket": false,
                              "name": "Force of Nature"
                            },
                            {
                              "id": 2937,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/0085138b38b1f85411988b1db668bc94.png",
                              "is_trinket": false,
                              "name": "Divine Sunderer"
                            },
                            {
                              "id": 3010,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6d6044334cc5fca47e413b13d2126a3a.png",
                              "is_trinket": false,
                              "name": "Executioner's Calling"
                            }
                          ],
                          "kills": 5,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 156,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 5,
                            "turrets": 1,
                            "wards": 11
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 5,
                          "largest_multi_kill": 2,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 20176,
                            "dealt_percentage": 6.69,
                            "dealt_to_champions": 1897,
                            "dealt_to_champions_percentage": 7.73,
                            "taken": 6836
                          },
                          "masteries": [],
                          "minions_killed": 188,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 138796,
                            "dealt_percentage": 38.98,
                            "dealt_to_champions": 8414,
                            "dealt_to_champions_percentage": 27.72,
                            "taken": 21530
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-12-24",
                            "first_name": "Moon",
                            "id": 31392,
                            "image_url": "https://cdn.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                            "last_name": "Hyeon-joon",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Oner",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "oner"
                          },
                          "player_id": 31392,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 175792,
                            "dealt_percentage": 25.14,
                            "dealt_to_champions": 11325,
                            "dealt_to_champions_percentage": 17.78,
                            "taken": 29181
                          },
                          "total_heal": 16892,
                          "total_time_crowd_control_dealt": 213,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 16819,
                            "dealt_percentage": 40.63,
                            "dealt_to_champions": 1013,
                            "dealt_to_champions_percentage": 11.54,
                            "taken": 814
                          },
                          "wards": {
                            "placed": 11,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 13
                          },
                          "wards_placed": 11
                        }
                      ],
                      "position": 2,
                      "status": "finished",
                      "teams": [
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3068,
                            3099,
                            3056,
                            3067,
                            2985
                          ],
                          "baron_kills": 0,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 1,
                          "color": "blue",
                          "dragon_kills": 4,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": false,
                          "first_blood": true,
                          "first_dragon": false,
                          "first_herald": false,
                          "first_inhibitor": true,
                          "first_tower": true,
                          "first_voidgrub": null,
                          "gold_earned": 55967,
                          "herald_kills": 0,
                          "hextech_drake_kills": 3,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 1,
                          "kills": 16,
                          "mountain_drake_kills": 0,
                          "ocean_drake_kills": 0,
                          "player_ids": [
                            585,
                            8158,
                            19285,
                            31391,
                            31392
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "tower_kills": 7,
                          "voidgrub_kills": null
                        },
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3015,
                            3048,
                            3013,
                            3134,
                            3000
                          ],
                          "baron_kills": 0,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 0,
                          "color": "red",
                          "dragon_kills": 1,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": false,
                          "first_blood": false,
                          "first_dragon": true,
                          "first_herald": true,
                          "first_inhibitor": false,
                          "first_tower": false,
                          "first_voidgrub": null,
                          "gold_earned": 47592,
                          "herald_kills": 2,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 0,
                          "kills": 2,
                          "mountain_drake_kills": 1,
                          "ocean_drake_kills": 0,
                          "player_ids": [
                            2169,
                            8172,
                            15425,
                            24996,
                            25391
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "tower_kills": 2,
                          "voidgrub_kills": null
                        }
                      ],
                      "winner": {
                        "id": 126061,
                        "type": "Team"
                      },
                      "winner_type": "Team"
                    },
                    {
                      "begin_at": "2022-07-01T11:01:54Z",
                      "complete": true,
                      "detailed_stats": true,
                      "end_at": "2022-07-01T11:48:42Z",
                      "finished": true,
                      "forfeit": false,
                      "id": 235729,
                      "length": 2340,
                      "match_id": 637573,
                      "players": [
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3000,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/333a3cf69198e947cd5eca7d47d56726.png",
                            "name": "Corki",
                            "slug": "Corki"
                          },
                          "creep_score": 355,
                          "cs_at_14": 118,
                          "cs_diff_at_14": -18,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235729,
                          "gold_earned": 17455,
                          "gold_percentage": 23.95,
                          "gold_spent": 16800,
                          "items": [
                            {
                              "id": 2493,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6828cf3bd100ca07d1da20e61a6547cb.png",
                              "is_trinket": false,
                              "name": "Guardian Angel"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2811,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/28719589de63ed2332d29dd334b368e0.png",
                              "is_trinket": false,
                              "name": "Muramana"
                            },
                            {
                              "id": 2872,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/28a5336738db9b68b288d7796243eb33.png",
                              "is_trinket": false,
                              "name": "Luden's Tempest"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2933,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/9eb16adb98fcdc9c9ae35eabe19c322f.png",
                              "is_trinket": false,
                              "name": "Maw of Malmortius"
                            }
                          ],
                          "kills": 6,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 49,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 6,
                            "turrets": 0,
                            "wards": 9
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 4,
                          "largest_multi_kill": 2,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 222821,
                            "dealt_percentage": 43.98,
                            "dealt_to_champions": 25287,
                            "dealt_to_champions_percentage": 55.97,
                            "taken": 6746
                          },
                          "masteries": [],
                          "minions_killed": 355,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 28004,
                            "dealt_percentage": 7.62,
                            "dealt_to_champions": 4379,
                            "dealt_to_champions_percentage": 11.11,
                            "taken": 9344
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-05-07",
                            "first_name": "Lee",
                            "id": 585,
                            "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                            "last_name": "Sang-hyeok",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Faker",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "faker"
                          },
                          "player_id": 585,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 253979,
                            "dealt_percentage": 26.3,
                            "dealt_to_champions": 31174,
                            "dealt_to_champions_percentage": 33.94,
                            "taken": 17908
                          },
                          "total_heal": 2892,
                          "total_time_crowd_control_dealt": 50,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 3153,
                            "dealt_percentage": 3.45,
                            "dealt_to_champions": 1508,
                            "dealt_to_champions_percentage": 20.78,
                            "taken": 1818
                          },
                          "wards": {
                            "placed": 23,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 10
                          },
                          "wards_placed": 23
                        },
                        {
                          "assists": 4,
                          "champion": {
                            "id": 3031,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/e05b5fd8059a74ff2a93e5e470865b11.png",
                            "name": "Kalista",
                            "slug": "Kalista"
                          },
                          "creep_score": 347,
                          "cs_at_14": 135,
                          "cs_diff_at_14": 122,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235729,
                          "gold_earned": 15647,
                          "gold_percentage": 23.63,
                          "gold_spent": 14800,
                          "items": [
                            {
                              "id": 2493,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6828cf3bd100ca07d1da20e61a6547cb.png",
                              "is_trinket": false,
                              "name": "Guardian Angel"
                            },
                            {
                              "id": 2544,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/924cb9f122b90bf1ee29b9650c092524.png",
                              "is_trinket": false,
                              "name": "Guinsoo's Rageblade"
                            },
                            {
                              "id": 2639,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7d33d9c83789bb40d7710612438109e0.png",
                              "is_trinket": false,
                              "name": "Vampiric Scepter"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2699,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/0f33f102856e8d40f6d38ff057856e1d.png",
                              "is_trinket": false,
                              "name": "Immortal Shieldbow"
                            },
                            {
                              "id": 2930,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/5bc313a2ec67cebd731e4cf0549cb077.png",
                              "is_trinket": false,
                              "name": "Wit's End"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 35,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 4,
                            "turrets": 0,
                            "wards": 12
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 238,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 2,
                          "level": 17,
                          "magic_damage": {
                            "dealt": 14273,
                            "dealt_percentage": 5.37,
                            "dealt_to_champions": 3287,
                            "dealt_to_champions_percentage": 11.41,
                            "taken": 12081
                          },
                          "masteries": [],
                          "minions_killed": 347,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 213351,
                            "dealt_percentage": 37.58,
                            "dealt_to_champions": 12929,
                            "dealt_to_champions_percentage": 32.62,
                            "taken": 10298
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-10-23",
                            "first_name": "Kim",
                            "id": 2169,
                            "image_url": "https://cdn.pandascore.co/images/player/image/2169/ezgif_3_4d5729796f.png",
                            "last_name": "Hyuk-kyu",
                            "modified_at": "2024-10-29T18:44:18Z",
                            "name": "Deft",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "deft"
                          },
                          "player_id": 2169,
                          "role": "adc",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 30,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/62cc94a564835cd3abd80d74346c35da.png",
                              "name": "Heal"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 228998,
                            "dealt_percentage": 23.92,
                            "dealt_to_champions": 16485,
                            "dealt_to_champions_percentage": 22.09,
                            "taken": 23479
                          },
                          "total_heal": 3733,
                          "total_time_crowd_control_dealt": 379,
                          "total_units_healed": 3,
                          "true_damage": {
                            "dealt": 1373,
                            "dealt_percentage": 1.11,
                            "dealt_to_champions": 268,
                            "dealt_to_champions_percentage": 4.33,
                            "taken": 1100
                          },
                          "wards": {
                            "placed": 23,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 10
                          },
                          "wards_placed": 23
                        },
                        {
                          "assists": 11,
                          "champion": {
                            "id": 3101,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/57b819d64ef4ee6747946c7a4d53132f.png",
                            "name": "Tahm Kench",
                            "slug": "TahmKench"
                          },
                          "creep_score": 253,
                          "cs_at_14": 113,
                          "cs_diff_at_14": 91,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235729,
                          "gold_earned": 12369,
                          "gold_percentage": 16.97,
                          "gold_spent": 11050,
                          "items": [
                            {
                              "id": 2481,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/84b0db5c9726c8bd47c9c8c088f6e8fb.png",
                              "is_trinket": false,
                              "name": "Broken Stopwatch"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2518,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d88172730ed0ae85cec7bebc1e0184cb.png",
                              "is_trinket": false,
                              "name": "Thornmail"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2830,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/4a236638d83dc2546184646200a5042a.png",
                              "is_trinket": false,
                              "name": "Frozen Heart"
                            },
                            {
                              "id": 3019,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/5c65145d1a8bab82316337cd7e27cd6c.png",
                              "is_trinket": false,
                              "name": "Frostfire Gauntlet"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 4,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 0,
                            "turrets": 0,
                            "wards": 6
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 17,
                          "magic_damage": {
                            "dealt": 90474,
                            "dealt_percentage": 17.86,
                            "dealt_to_champions": 3649,
                            "dealt_to_champions_percentage": 8.08,
                            "taken": 7485
                          },
                          "masteries": [],
                          "minions_killed": 253,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 27586,
                            "dealt_percentage": 7.5,
                            "dealt_to_champions": 402,
                            "dealt_to_champions_percentage": 1.02,
                            "taken": 9856
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-10-14",
                            "first_name": "Ryu",
                            "id": 8158,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                            "last_name": "Min-seok",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Keria",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "keria"
                          },
                          "player_id": 8158,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 118060,
                            "dealt_percentage": 12.23,
                            "dealt_to_champions": 4052,
                            "dealt_to_champions_percentage": 4.41,
                            "taken": 18661
                          },
                          "total_heal": 5675,
                          "total_time_crowd_control_dealt": 1770,
                          "total_units_healed": 5,
                          "true_damage": {
                            "dealt": 0,
                            "dealt_percentage": 0,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 1319
                          },
                          "wards": {
                            "placed": 17,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 10
                          },
                          "wards_placed": 17
                        },
                        {
                          "assists": 2,
                          "champion": {
                            "id": 3015,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/e9c553799df2db297afcb8bcfc715daf.png",
                            "name": "Gnar",
                            "slug": "Gnar"
                          },
                          "creep_score": 271,
                          "cs_at_14": 117,
                          "cs_diff_at_14": -9,
                          "deaths": 6,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235729,
                          "gold_earned": 14118,
                          "gold_percentage": 21.32,
                          "gold_spent": 14358,
                          "items": [
                            {
                              "id": 2465,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/167abf5d0dc59292a78b79ceadffcc99.png",
                              "is_trinket": false,
                              "name": "Negatron Cloak"
                            },
                            {
                              "id": 2518,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d88172730ed0ae85cec7bebc1e0184cb.png",
                              "is_trinket": false,
                              "name": "Thornmail"
                            },
                            {
                              "id": 2537,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                              "is_trinket": false,
                              "name": "Mercury's Treads"
                            },
                            {
                              "id": 2659,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/afe5e3df08a76a4c10753ecd5da4273d.png",
                              "is_trinket": false,
                              "name": "Winged Moonplate"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2927,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/a3d78560d3945a73d66da14f28d6b759.png",
                              "is_trinket": false,
                              "name": "Black Cleaver"
                            },
                            {
                              "id": 2929,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/5b92dcbb3d964c0ad39b320d55601c9a.png",
                              "is_trinket": false,
                              "name": "Trinity Force"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 16,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 2,
                            "wards": 13
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 15,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 17,
                          "magic_damage": {
                            "dealt": 22640,
                            "dealt_percentage": 8.52,
                            "dealt_to_champions": 3929,
                            "dealt_to_champions_percentage": 13.64,
                            "taken": 14066
                          },
                          "masteries": [],
                          "minions_killed": 271,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 167116,
                            "dealt_percentage": 29.44,
                            "dealt_to_champions": 18966,
                            "dealt_to_champions_percentage": 47.86,
                            "taken": 16968
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-03-11",
                            "first_name": "Hwang",
                            "id": 8172,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8172/drx_kingen_2022_split_2.png",
                            "last_name": "Seong-hoon",
                            "modified_at": "2026-01-06T07:15:57Z",
                            "name": "Kingen",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "kingen"
                          },
                          "player_id": 8172,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 201795,
                            "dealt_percentage": 21.07,
                            "dealt_to_champions": 23330,
                            "dealt_to_champions_percentage": 31.26,
                            "taken": 35044
                          },
                          "total_heal": 4541,
                          "total_time_crowd_control_dealt": 553,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 12038,
                            "dealt_percentage": 9.7,
                            "dealt_to_champions": 435,
                            "dealt_to_champions_percentage": 7.03,
                            "taken": 4010
                          },
                          "wards": {
                            "placed": 14,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 11
                          },
                          "wards_placed": 14
                        },
                        {
                          "assists": 7,
                          "champion": {
                            "id": 2985,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/51d804c0d88232b558e0117f5fbb8df5.png",
                            "name": "Amumu",
                            "slug": "Amumu"
                          },
                          "creep_score": 46,
                          "cs_at_14": 22,
                          "cs_diff_at_14": -91,
                          "deaths": 4,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": true,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235729,
                          "gold_earned": 8893,
                          "gold_percentage": 13.43,
                          "gold_spent": 8350,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2688,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c38d52b6bb9b984bf353c56585dae43d.png",
                              "is_trinket": false,
                              "name": "Force of Nature"
                            },
                            {
                              "id": 2804,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d05cf3b9331e5b13d9e4b73b4b1ff22a.png",
                              "is_trinket": false,
                              "name": "Bulwark of the Mountain"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2902,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7c53fbb2a912cc56797a86bfe1dc596f.png",
                              "is_trinket": false,
                              "name": "Locket of the Iron Solari"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 0,
                            "wards": 10
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 14,
                          "magic_damage": {
                            "dealt": 14253,
                            "dealt_percentage": 5.36,
                            "dealt_to_champions": 3240,
                            "dealt_to_champions_percentage": 11.25,
                            "taken": 6846
                          },
                          "masteries": [],
                          "minions_killed": 46,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 7044,
                            "dealt_percentage": 1.24,
                            "dealt_to_champions": 679,
                            "dealt_to_champions_percentage": 1.71,
                            "taken": 9987
                          },
                          "player": {
                            "active": true,
                            "age": 28,
                            "birthday": "1997-04-01",
                            "first_name": "Cho",
                            "id": 15425,
                            "image_url": "https://cdn.pandascore.co/images/player/image/15425/drx_bery_l_2022_split_2.png",
                            "last_name": "Geon-hee",
                            "modified_at": "2025-12-30T12:27:51Z",
                            "name": "BeryL",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "beryl"
                          },
                          "player_id": 15425,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 29394,
                            "dealt_percentage": 3.07,
                            "dealt_to_champions": 4853,
                            "dealt_to_champions_percentage": 6.5,
                            "taken": 17387
                          },
                          "total_heal": 1201,
                          "total_time_crowd_control_dealt": 83,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 8096,
                            "dealt_percentage": 6.52,
                            "dealt_to_champions": 933,
                            "dealt_to_champions_percentage": 15.09,
                            "taken": 553
                          },
                          "wards": {
                            "placed": 63,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 18
                          },
                          "wards_placed": 63
                        },
                        {
                          "assists": 8,
                          "champion": {
                            "id": 3147,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/8f448f569bc040fbeaf36de3805ed2eb.png",
                            "name": "Senna",
                            "slug": "Senna"
                          },
                          "creep_score": 58,
                          "cs_at_14": 13,
                          "cs_diff_at_14": -122,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235729,
                          "gold_earned": 11245,
                          "gold_percentage": 15.43,
                          "gold_spent": 9125,
                          "items": [
                            {
                              "id": 2489,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7c39a6acc5d50b697a09e78338c3d4a0.png",
                              "is_trinket": false,
                              "name": "Boots of Swiftness"
                            },
                            {
                              "id": 2652,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/0e05c6ca936978b4f09ade82914b7e39.png",
                              "is_trinket": false,
                              "name": "Last Whisper"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2806,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/f530d00c32c745acf57bf0521cf565f7.png",
                              "is_trinket": false,
                              "name": "Black Mist Scythe"
                            },
                            {
                              "id": 2912,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/eaef5f4c2f6f2d5fcf13f287c321e59b.png",
                              "is_trinket": false,
                              "name": "Eclipse"
                            },
                            {
                              "id": 2963,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/b024e8ca8cf9873201744933ec14c30c.png",
                              "is_trinket": false,
                              "name": "Umbral Glaive"
                            }
                          ],
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 3,
                            "turrets": 3,
                            "wards": 30
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 623,
                          "largest_killing_spree": 3,
                          "largest_multi_kill": 2,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 0,
                            "dealt_percentage": 0,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 3522
                          },
                          "masteries": [],
                          "minions_killed": 58,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 86705,
                            "dealt_percentage": 23.58,
                            "dealt_to_champions": 21779,
                            "dealt_to_champions_percentage": 55.25,
                            "taken": 5364
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-02-06",
                            "first_name": "Lee",
                            "id": 19285,
                            "image_url": "https://cdn.pandascore.co/images/player/image/19285/t1_gumayusi_2023_split_2.png",
                            "last_name": "Min-hyeon",
                            "modified_at": "2026-01-06T07:15:49Z",
                            "name": "Gumayusi",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "gumayusi"
                          },
                          "player_id": 19285,
                          "role": "adc",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 27,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/37e058ce96cf92adf6831ad5946956f4.png",
                              "name": "Exhaust"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 86773,
                            "dealt_percentage": 8.99,
                            "dealt_to_champions": 21779,
                            "dealt_to_champions_percentage": 23.71,
                            "taken": 9424
                          },
                          "total_heal": 8464,
                          "total_time_crowd_control_dealt": 258,
                          "total_units_healed": 5,
                          "true_damage": {
                            "dealt": 68,
                            "dealt_percentage": 0.07,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 537
                          },
                          "wards": {
                            "placed": 54,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 11
                          },
                          "wards_placed": 54
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3019,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/17e6955935acb7f57110f0af92514b1c.png",
                            "name": "Hecarim",
                            "slug": "Hecarim"
                          },
                          "creep_score": 234,
                          "cs_at_14": 107,
                          "cs_diff_at_14": 0,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": true
                          },
                          "game_id": 235729,
                          "gold_earned": 12184,
                          "gold_percentage": 18.4,
                          "gold_spent": 11775,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2688,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c38d52b6bb9b984bf353c56585dae43d.png",
                              "is_trinket": false,
                              "name": "Force of Nature"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2881,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1e0b1c90b92e68856c4c8623b98cc24f.png",
                              "is_trinket": false,
                              "name": "Dead Man's Plate"
                            },
                            {
                              "id": 3020,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/49ca044dd30a7b6495d9b99f699e20ec.png",
                              "is_trinket": false,
                              "name": "Turbo Chemtank"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 214,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 1,
                            "wards": 11
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 62142,
                            "dealt_percentage": 23.38,
                            "dealt_to_champions": 1702,
                            "dealt_to_champions_percentage": 5.91,
                            "taken": 10153
                          },
                          "masteries": [],
                          "minions_killed": 234,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 146503,
                            "dealt_percentage": 25.81,
                            "dealt_to_champions": 5339,
                            "dealt_to_champions_percentage": 13.47,
                            "taken": 26750
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-03-21",
                            "first_name": "Hong",
                            "id": 24996,
                            "image_url": "https://cdn.pandascore.co/images/player/image/24996/tl_pyosik_2023_split_1.png",
                            "last_name": "Chang-hyeon",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "Pyosik",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "pyosik"
                          },
                          "player_id": 24996,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 29,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/58955cb861c3b51375948a05e260996a.png",
                              "name": "Ghost"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 226087,
                            "dealt_percentage": 23.61,
                            "dealt_to_champions": 7938,
                            "dealt_to_champions_percentage": 10.64,
                            "taken": 37634
                          },
                          "total_heal": 17705,
                          "total_time_crowd_control_dealt": 220,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 17441,
                            "dealt_percentage": 14.05,
                            "dealt_to_champions": 897,
                            "dealt_to_champions_percentage": 14.51,
                            "taken": 731
                          },
                          "wards": {
                            "placed": 22,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 23
                          },
                          "wards_placed": 22
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 2981,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/4979c17972899770e5199844b846875a.png",
                            "name": "Ahri",
                            "slug": "Ahri"
                          },
                          "creep_score": 381,
                          "cs_at_14": 136,
                          "cs_diff_at_14": 18,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235729,
                          "gold_earned": 15377,
                          "gold_percentage": 23.22,
                          "gold_spent": 15260,
                          "items": [
                            {
                              "id": 2480,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/49631901cd0f2419b756e4118109e312.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2774,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/19d538db18a40b62822d7ca7ab1de27a.png",
                              "is_trinket": false,
                              "name": "Banshee's Veil"
                            },
                            {
                              "id": 2814,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                              "is_trinket": false,
                              "name": "Rabadon's Deathcap"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2910,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/a8377226b797197fdb941b2fad4123cb.png",
                              "is_trinket": false,
                              "name": "Everfrost"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 10,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 0,
                            "turrets": 1,
                            "wards": 17
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 152444,
                            "dealt_percentage": 57.36,
                            "dealt_to_champions": 16647,
                            "dealt_to_champions_percentage": 57.79,
                            "taken": 7882
                          },
                          "masteries": [],
                          "minions_killed": 381,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 33678,
                            "dealt_percentage": 5.93,
                            "dealt_to_champions": 1719,
                            "dealt_to_champions_percentage": 4.34,
                            "taken": 10510
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-11-28",
                            "first_name": "Kim",
                            "id": 25391,
                            "image_url": "https://cdn.pandascore.co/images/player/image/25391/drx_zeka_2022_split_2.png",
                            "last_name": "Geon-woo",
                            "modified_at": "2026-01-06T07:15:50Z",
                            "name": "Zeka",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "zeka"
                          },
                          "player_id": 25391,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 271275,
                            "dealt_percentage": 28.33,
                            "dealt_to_champions": 22019,
                            "dealt_to_champions_percentage": 29.51,
                            "taken": 19255
                          },
                          "total_heal": 7337,
                          "total_time_crowd_control_dealt": 144,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 85153,
                            "dealt_percentage": 68.62,
                            "dealt_to_champions": 3651,
                            "dealt_to_champions_percentage": 59.04,
                            "taken": 863
                          },
                          "wards": {
                            "placed": 26,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 4
                          },
                          "wards_placed": 26
                        },
                        {
                          "assists": 9,
                          "champion": {
                            "id": 3018,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/a7483c3b14ed866fecd8726a1046187b.png",
                            "name": "Gwen",
                            "slug": "Gwen"
                          },
                          "creep_score": 349,
                          "cs_at_14": 126,
                          "cs_diff_at_14": 9,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235729,
                          "gold_earned": 16220,
                          "gold_percentage": 22.25,
                          "gold_spent": 15200,
                          "items": [
                            {
                              "id": 2540,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/e0bb551fce03c63d9385356960cbfce0.png",
                              "is_trinket": false,
                              "name": "Nashor's Tooth"
                            },
                            {
                              "id": 2642,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d3c7dce8ed50a8553198bdefbacac855.png",
                              "is_trinket": false,
                              "name": "Needlessly Large Rod"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2776,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/000057177c6cd0f3895e67b2199dacb9.png",
                              "is_trinket": false,
                              "name": "Zhonya's Hourglass"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2907,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3f929f236ba0734da501690a3c38174.png",
                              "is_trinket": false,
                              "name": "Demonic Embrace"
                            },
                            {
                              "id": 3017,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/81cd1acbc7ee06bec32014055901b37e.png",
                              "is_trinket": false,
                              "name": "Riftmaker"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 19,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 4,
                            "turrets": 1,
                            "wards": 14
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 120996,
                            "dealt_percentage": 23.88,
                            "dealt_to_champions": 14364,
                            "dealt_to_champions_percentage": 31.79,
                            "taken": 6934
                          },
                          "masteries": [],
                          "minions_killed": 349,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 56622,
                            "dealt_percentage": 15.4,
                            "dealt_to_champions": 2524,
                            "dealt_to_champions_percentage": 6.4,
                            "taken": 22880
                          },
                          "player": {
                            "active": true,
                            "age": 21,
                            "birthday": "2004-01-31",
                            "first_name": "Choi",
                            "id": 31391,
                            "image_url": "https://cdn.pandascore.co/images/player/image/31391/t1_zeus_2023_split_2.png",
                            "last_name": "Woo-je",
                            "modified_at": "2026-01-06T07:15:50Z",
                            "name": "Zeus",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "zeus-choi-woo-je"
                          },
                          "player_id": 31391,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 29,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/58955cb861c3b51375948a05e260996a.png",
                              "name": "Ghost"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 244843,
                            "dealt_percentage": 25.36,
                            "dealt_to_champions": 22267,
                            "dealt_to_champions_percentage": 24.24,
                            "taken": 31470
                          },
                          "total_heal": 4073,
                          "total_time_crowd_control_dealt": 112,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 67224,
                            "dealt_percentage": 73.65,
                            "dealt_to_champions": 5378,
                            "dealt_to_champions_percentage": 74.11,
                            "taken": 1655
                          },
                          "wards": {
                            "placed": 14,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 8
                          },
                          "wards_placed": 14
                        },
                        {
                          "assists": 7,
                          "champion": {
                            "id": 3142,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/1b4a743524b01e0885b8a6e84d5a8663.png",
                            "name": "Lee Sin",
                            "slug": "LeeSin"
                          },
                          "creep_score": 276,
                          "cs_at_14": 107,
                          "cs_diff_at_14": 0,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235729,
                          "gold_earned": 15596,
                          "gold_percentage": 21.4,
                          "gold_spent": 14375,
                          "items": [
                            {
                              "id": 2493,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6828cf3bd100ca07d1da20e61a6547cb.png",
                              "is_trinket": false,
                              "name": "Guardian Angel"
                            },
                            {
                              "id": 2537,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                              "is_trinket": false,
                              "name": "Mercury's Treads"
                            },
                            {
                              "id": 2677,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d764e2dad4b185bbbbc86ca2998d5313.png",
                              "is_trinket": true,
                              "name": "Stealth Ward"
                            },
                            {
                              "id": 2927,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/a3d78560d3945a73d66da14f28d6b759.png",
                              "is_trinket": false,
                              "name": "Black Cleaver"
                            },
                            {
                              "id": 2932,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3b53081565041e3e40a806f68cb7a360.png",
                              "is_trinket": false,
                              "name": "Hexdrinker"
                            },
                            {
                              "id": 2935,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/97032f4cae42f011b132d0bca2438e8b.png",
                              "is_trinket": false,
                              "name": "Goredrinker"
                            }
                          ],
                          "kills": 5,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 204,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 5,
                            "turrets": 3,
                            "wards": 8
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 5,
                          "largest_multi_kill": 1,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 72335,
                            "dealt_percentage": 14.28,
                            "dealt_to_champions": 1877,
                            "dealt_to_champions_percentage": 4.15,
                            "taken": 6976
                          },
                          "masteries": [],
                          "minions_killed": 276,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 168828,
                            "dealt_percentage": 45.91,
                            "dealt_to_champions": 10334,
                            "dealt_to_champions_percentage": 26.22,
                            "taken": 24856
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-12-24",
                            "first_name": "Moon",
                            "id": 31392,
                            "image_url": "https://cdn.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                            "last_name": "Hyeon-joon",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Oner",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "oner"
                          },
                          "player_id": 31392,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 261990,
                            "dealt_percentage": 27.13,
                            "dealt_to_champions": 12583,
                            "dealt_to_champions_percentage": 13.7,
                            "taken": 32688
                          },
                          "total_heal": 9725,
                          "total_time_crowd_control_dealt": 779,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 20825,
                            "dealt_percentage": 22.82,
                            "dealt_to_champions": 371,
                            "dealt_to_champions_percentage": 5.11,
                            "taken": 855
                          },
                          "wards": {
                            "placed": 21,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 9
                          },
                          "wards_placed": 21
                        }
                      ],
                      "position": 1,
                      "status": "finished",
                      "teams": [
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3068,
                            3066,
                            2982,
                            3141,
                            3056
                          ],
                          "baron_kills": 1,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 1,
                          "color": "blue",
                          "dragon_kills": 3,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": false,
                          "first_blood": false,
                          "first_dragon": false,
                          "first_herald": true,
                          "first_inhibitor": true,
                          "first_tower": false,
                          "first_voidgrub": null,
                          "gold_earned": 72885,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 2,
                          "inhibitor_kills": 2,
                          "kills": 18,
                          "mountain_drake_kills": 0,
                          "ocean_drake_kills": 0,
                          "player_ids": [
                            585,
                            8158,
                            19285,
                            31391,
                            31392
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "tower_kills": 8,
                          "voidgrub_kills": null
                        },
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3070,
                            3048,
                            3120,
                            3134,
                            3013
                          ],
                          "baron_kills": 1,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 0,
                          "color": "red",
                          "dragon_kills": 3,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": true,
                          "first_blood": true,
                          "first_dragon": true,
                          "first_herald": false,
                          "first_inhibitor": false,
                          "first_tower": true,
                          "first_voidgrub": null,
                          "gold_earned": 66219,
                          "herald_kills": 1,
                          "hextech_drake_kills": 1,
                          "infernal_drake_kills": 2,
                          "inhibitor_kills": 0,
                          "kills": 10,
                          "mountain_drake_kills": 0,
                          "ocean_drake_kills": 0,
                          "player_ids": [
                            2169,
                            8172,
                            15425,
                            24996,
                            25391
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:54Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "tower_kills": 4,
                          "voidgrub_kills": null
                        }
                      ],
                      "winner": {
                        "id": 126061,
                        "type": "Team"
                      },
                      "winner_type": "Team"
                    },
                    {
                      "begin_at": "2022-06-29T13:32:05Z",
                      "complete": true,
                      "detailed_stats": true,
                      "end_at": "2022-06-29T14:17:59Z",
                      "finished": true,
                      "forfeit": false,
                      "id": 235719,
                      "length": 2331,
                      "match_id": 637569,
                      "players": [
                        {
                          "assists": 7,
                          "champion": {
                            "id": 3047,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/6419f4dd0a0829176487b76ac1c451da.png",
                            "name": "Lissandra",
                            "slug": "Lissandra"
                          },
                          "creep_score": 328,
                          "cs_at_14": 138,
                          "cs_diff_at_14": 11,
                          "deaths": 5,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": true
                          },
                          "game_id": 235719,
                          "gold_earned": 15341,
                          "gold_percentage": 21.59,
                          "gold_spent": 14780,
                          "items": [
                            {
                              "id": 2651,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2776,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/000057177c6cd0f3895e67b2199dacb9.png",
                              "is_trinket": false,
                              "name": "Zhonya's Hourglass"
                            },
                            {
                              "id": 2814,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                              "is_trinket": false,
                              "name": "Rabadon's Deathcap"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2910,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/a8377226b797197fdb941b2fad4123cb.png",
                              "is_trinket": false,
                              "name": "Everfrost"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 20,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 2,
                            "wards": 11
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 17,
                          "magic_damage": {
                            "dealt": 199993,
                            "dealt_percentage": 69.45,
                            "dealt_to_champions": 15962,
                            "dealt_to_champions_percentage": 53.63,
                            "taken": 6843
                          },
                          "masteries": [],
                          "minions_killed": 328,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 16424,
                            "dealt_percentage": 2.19,
                            "dealt_to_champions": 1780,
                            "dealt_to_champions_percentage": 5.5,
                            "taken": 10521
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-05-07",
                            "first_name": "Lee",
                            "id": 585,
                            "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                            "last_name": "Sang-hyeok",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Faker",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "faker"
                          },
                          "player_id": 585,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 218622,
                            "dealt_percentage": 19.65,
                            "dealt_to_champions": 18467,
                            "dealt_to_champions_percentage": 27.33,
                            "taken": 17554
                          },
                          "total_heal": 1589,
                          "total_time_crowd_control_dealt": 267,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 2204,
                            "dealt_percentage": 2.97,
                            "dealt_to_champions": 724,
                            "dealt_to_champions_percentage": 13.24,
                            "taken": 188
                          },
                          "wards": {
                            "placed": 17,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 13
                          },
                          "wards_placed": 17
                        },
                        {
                          "assists": 14,
                          "champion": {
                            "id": 2989,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/4c292dfc73999728a4e0d2d339587781.png",
                            "name": "Ashe",
                            "slug": "Ashe"
                          },
                          "creep_score": 48,
                          "cs_at_14": 18,
                          "cs_diff_at_14": -132,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": true,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235719,
                          "gold_earned": 9991,
                          "gold_percentage": 13.55,
                          "gold_spent": 8075,
                          "items": [
                            {
                              "id": 2660,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c5709a137fafe955c32ae4511fb78d99.png",
                              "is_trinket": false,
                              "name": "Tear of the Goddess"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2806,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/f530d00c32c745acf57bf0521cf565f7.png",
                              "is_trinket": false,
                              "name": "Black Mist Scythe"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2990,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/034877c4-2e7d-478d-9788-d61fad99f677.png",
                              "is_trinket": false,
                              "name": "Seat of Command"
                            },
                            {
                              "id": 3018,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6e620845d16abd235e4e5703ed8221b6.png",
                              "is_trinket": false,
                              "name": "Chempunk Chainsword"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 5,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 1,
                            "wards": 18
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 127,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 5094,
                            "dealt_percentage": 1.21,
                            "dealt_to_champions": 4014,
                            "dealt_to_champions_percentage": 12.85,
                            "taken": 3306
                          },
                          "masteries": [],
                          "minions_killed": 48,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 44825,
                            "dealt_percentage": 8.38,
                            "dealt_to_champions": 8273,
                            "dealt_to_champions_percentage": 18.54,
                            "taken": 2936
                          },
                          "player": {
                            "active": true,
                            "age": 27,
                            "birthday": "1998-03-15",
                            "first_name": "Park",
                            "id": 1456,
                            "image_url": "https://cdn.pandascore.co/images/player/image/1456/t1_teddy_2021_split_2.png",
                            "last_name": "Jin-seong",
                            "modified_at": "2026-01-06T07:15:57Z",
                            "name": "Teddy",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "teddy"
                          },
                          "player_id": 1456,
                          "role": "adc",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 30,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/62cc94a564835cd3abd80d74346c35da.png",
                              "name": "Heal"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 51820,
                            "dealt_percentage": 5.2,
                            "dealt_to_champions": 12762,
                            "dealt_to_champions_percentage": 16.5,
                            "taken": 6446
                          },
                          "total_heal": 1630,
                          "total_time_crowd_control_dealt": 458,
                          "total_units_healed": 3,
                          "true_damage": {
                            "dealt": 1899,
                            "dealt_percentage": 4.67,
                            "dealt_to_champions": 474,
                            "dealt_to_champions_percentage": 32.4,
                            "taken": 204
                          },
                          "wards": {
                            "placed": 104,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 15
                          },
                          "wards_placed": 104
                        },
                        {
                          "assists": 9,
                          "champion": {
                            "id": 3015,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/e9c553799df2db297afcb8bcfc715daf.png",
                            "name": "Gnar",
                            "slug": "Gnar"
                          },
                          "creep_score": 369,
                          "cs_at_14": 113,
                          "cs_diff_at_14": -2,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235719,
                          "gold_earned": 19698,
                          "gold_percentage": 26.72,
                          "gold_spent": 18608,
                          "items": [
                            {
                              "id": 2493,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6828cf3bd100ca07d1da20e61a6547cb.png",
                              "is_trinket": false,
                              "name": "Guardian Angel"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2926,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/9e7450aaa9bd2694e330a2d84b974eba.png",
                              "is_trinket": false,
                              "name": "Sterak's Gage"
                            },
                            {
                              "id": 2927,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/a3d78560d3945a73d66da14f28d6b759.png",
                              "is_trinket": false,
                              "name": "Black Cleaver"
                            },
                            {
                              "id": 2986,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/706c8c0e-5ced-4d61-9047-be4808b1fe3b.png",
                              "is_trinket": false,
                              "name": "Infinity Force"
                            },
                            {
                              "id": 3011,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/316a78d2b6de41b09316db6e64e44147.png",
                              "is_trinket": false,
                              "name": "Randuin's Omen"
                            }
                          ],
                          "kills": 7,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 42,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 7,
                            "turrets": 6,
                            "wards": 10
                          },
                          "kills_series": {
                            "double_kills": 2,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 1
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 7,
                          "largest_multi_kill": 3,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 34122,
                            "dealt_percentage": 8.09,
                            "dealt_to_champions": 6078,
                            "dealt_to_champions_percentage": 19.45,
                            "taken": 6509
                          },
                          "masteries": [],
                          "minions_killed": 369,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 265381,
                            "dealt_percentage": 49.62,
                            "dealt_to_champions": 21214,
                            "dealt_to_champions_percentage": 47.54,
                            "taken": 14662
                          },
                          "player": {
                            "active": true,
                            "age": 26,
                            "birthday": "1999-05-28",
                            "first_name": "Kim",
                            "id": 3524,
                            "image_url": "https://cdn.pandascore.co/images/player/image/3524/kt_kiin_2023_split_2.png",
                            "last_name": "Gi-in ",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Kiin",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "kiin"
                          },
                          "player_id": 3524,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 302879,
                            "dealt_percentage": 30.37,
                            "dealt_to_champions": 27448,
                            "dealt_to_champions_percentage": 35.49,
                            "taken": 22423
                          },
                          "total_heal": 4025,
                          "total_time_crowd_control_dealt": 567,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 3376,
                            "dealt_percentage": 8.3,
                            "dealt_to_champions": 156,
                            "dealt_to_champions_percentage": 10.66,
                            "taken": 1252
                          },
                          "wards": {
                            "placed": 10,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 5
                          },
                          "wards_placed": 10
                        },
                        {
                          "assists": 12,
                          "champion": {
                            "id": 3087,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/596326c80f939f6cafdb73d9e5917311.png",
                            "name": "Seraphine",
                            "slug": "Seraphine"
                          },
                          "creep_score": 339,
                          "cs_at_14": 111,
                          "cs_diff_at_14": 93,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235719,
                          "gold_earned": 16025,
                          "gold_percentage": 21.74,
                          "gold_spent": 14400,
                          "items": [
                            {
                              "id": 2499,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/95f8b2323890310c5d277d71551bc0e6.png",
                              "is_trinket": false,
                              "name": "Mejai's Soulstealer"
                            },
                            {
                              "id": 2549,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6fc977de9de7a8f21f098fa1cbbcdd9a.png",
                              "is_trinket": false,
                              "name": "Quicksilver Sash"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2919,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/47c001c40f4d6d169be155b0a74e08d5.png",
                              "is_trinket": false,
                              "name": "Seraph's Embrace"
                            },
                            {
                              "id": 2924,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d4fde29e50e7ed8472b31f4a78134063.png",
                              "is_trinket": false,
                              "name": "Rylai's Crystal Scepter"
                            },
                            {
                              "id": 2980,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/2ec98646-c7ac-427d-944c-a67365d42775.png",
                              "is_trinket": false,
                              "name": "Liandry's Lament"
                            }
                          ],
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 12,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 3,
                            "turrets": 0,
                            "wards": 12
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 17,
                          "magic_damage": {
                            "dealt": 242892,
                            "dealt_percentage": 57.58,
                            "dealt_to_champions": 12654,
                            "dealt_to_champions_percentage": 40.5,
                            "taken": 6031
                          },
                          "masteries": [],
                          "minions_killed": 339,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 17025,
                            "dealt_percentage": 3.18,
                            "dealt_to_champions": 1094,
                            "dealt_to_champions_percentage": 2.45,
                            "taken": 5838
                          },
                          "player": {
                            "active": false,
                            "age": 26,
                            "birthday": "1999-07-06",
                            "first_name": "Ryu",
                            "id": 8142,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8142/t1.c_hoit_2021_split_2.png",
                            "last_name": "Ho-seong",
                            "modified_at": "2025-12-30T20:38:46Z",
                            "name": "Hoit",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "hoit"
                          },
                          "player_id": 8142,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 262687,
                            "dealt_percentage": 26.34,
                            "dealt_to_champions": 13848,
                            "dealt_to_champions_percentage": 17.91,
                            "taken": 12322
                          },
                          "total_heal": 5888,
                          "total_time_crowd_control_dealt": 385,
                          "total_units_healed": 7,
                          "true_damage": {
                            "dealt": 2770,
                            "dealt_percentage": 6.81,
                            "dealt_to_champions": 100,
                            "dealt_to_champions_percentage": 6.84,
                            "taken": 453
                          },
                          "wards": {
                            "placed": 28,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 12
                          },
                          "wards_placed": 28
                        },
                        {
                          "assists": 4,
                          "champion": {
                            "id": 3101,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/57b819d64ef4ee6747946c7a4d53132f.png",
                            "name": "Tahm Kench",
                            "slug": "TahmKench"
                          },
                          "creep_score": 39,
                          "cs_at_14": 18,
                          "cs_diff_at_14": -93,
                          "deaths": 4,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235719,
                          "gold_earned": 8187,
                          "gold_percentage": 11.52,
                          "gold_spent": 8460,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2512,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1e29f7f8a099017ed7b1a6333a9357b1.png",
                              "is_trinket": false,
                              "name": "Kindlegem"
                            },
                            {
                              "id": 2537,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                              "is_trinket": false,
                              "name": "Mercury's Treads"
                            },
                            {
                              "id": 2549,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6fc977de9de7a8f21f098fa1cbbcdd9a.png",
                              "is_trinket": false,
                              "name": "Quicksilver Sash"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2804,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d05cf3b9331e5b13d9e4b73b4b1ff22a.png",
                              "is_trinket": false,
                              "name": "Bulwark of the Mountain"
                            },
                            {
                              "id": 2902,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7c53fbb2a912cc56797a86bfe1dc596f.png",
                              "is_trinket": false,
                              "name": "Locket of the Iron Solari"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 0,
                            "wards": 10
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 13,
                          "magic_damage": {
                            "dealt": 14450,
                            "dealt_percentage": 5.02,
                            "dealt_to_champions": 3576,
                            "dealt_to_champions_percentage": 12.01,
                            "taken": 5290
                          },
                          "masteries": [],
                          "minions_killed": 39,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 2649,
                            "dealt_percentage": 0.35,
                            "dealt_to_champions": 147,
                            "dealt_to_champions_percentage": 0.45,
                            "taken": 13362
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-10-14",
                            "first_name": "Ryu",
                            "id": 8158,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                            "last_name": "Min-seok",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Keria",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "keria"
                          },
                          "player_id": 8158,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 26930,
                            "dealt_percentage": 2.42,
                            "dealt_to_champions": 4858,
                            "dealt_to_champions_percentage": 7.19,
                            "taken": 19053
                          },
                          "total_heal": 4233,
                          "total_time_crowd_control_dealt": 98,
                          "total_units_healed": 3,
                          "true_damage": {
                            "dealt": 9831,
                            "dealt_percentage": 13.27,
                            "dealt_to_champions": 1134,
                            "dealt_to_champions_percentage": 20.74,
                            "taken": 400
                          },
                          "wards": {
                            "placed": 82,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 22
                          },
                          "wards_placed": 82
                        },
                        {
                          "assists": 10,
                          "champion": {
                            "id": 3068,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/c85a85ae33a47512d18da2cf10d65a90.png",
                            "name": "Ornn",
                            "slug": "Ornn"
                          },
                          "creep_score": 317,
                          "cs_at_14": 127,
                          "cs_diff_at_14": -11,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235719,
                          "gold_earned": 14239,
                          "gold_percentage": 19.32,
                          "gold_spent": 12075,
                          "items": [
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2518,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d88172730ed0ae85cec7bebc1e0184cb.png",
                              "is_trinket": false,
                              "name": "Thornmail"
                            },
                            {
                              "id": 2660,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c5709a137fafe955c32ae4511fb78d99.png",
                              "is_trinket": false,
                              "name": "Tear of the Goddess"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2830,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/4a236638d83dc2546184646200a5042a.png",
                              "is_trinket": false,
                              "name": "Frozen Heart"
                            },
                            {
                              "id": 2895,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c15bf1590aa48b474c160fd41fb15b8d.png",
                              "is_trinket": false,
                              "name": "Aegis of the Legion"
                            },
                            {
                              "id": 3023,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/88ccb778-dc32-46ff-85d2-65f2f7c5158a.png",
                              "is_trinket": false,
                              "name": "Rimeforged Grasp"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 5,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 1,
                            "wards": 11
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 41,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 109732,
                            "dealt_percentage": 26.01,
                            "dealt_to_champions": 6197,
                            "dealt_to_champions_percentage": 19.83,
                            "taken": 7595
                          },
                          "masteries": [],
                          "minions_killed": 317,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 101196,
                            "dealt_percentage": 18.92,
                            "dealt_to_champions": 3005,
                            "dealt_to_champions_percentage": 6.73,
                            "taken": 12151
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-08-22",
                            "first_name": "Yoo",
                            "id": 8924,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8924/kdf_fate_2022_split_2.png",
                            "last_name": "Su-hyeok",
                            "modified_at": "2025-08-15T13:43:55Z",
                            "name": "FATE",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "fate"
                          },
                          "player_id": 8924,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 220223,
                            "dealt_percentage": 22.08,
                            "dealt_to_champions": 9446,
                            "dealt_to_champions_percentage": 12.21,
                            "taken": 20847
                          },
                          "total_heal": 2858,
                          "total_time_crowd_control_dealt": 2153,
                          "total_units_healed": 2,
                          "true_damage": {
                            "dealt": 9294,
                            "dealt_percentage": 22.84,
                            "dealt_to_champions": 244,
                            "dealt_to_champions_percentage": 16.68,
                            "taken": 1101
                          },
                          "wards": {
                            "placed": 13,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 11
                          },
                          "wards_placed": 13
                        },
                        {
                          "assists": 11,
                          "champion": {
                            "id": 3056,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/842947265b0e075804b15ae06011afda.png",
                            "name": "Wukong",
                            "slug": "MonkeyKing"
                          },
                          "creep_score": 173,
                          "cs_at_14": 87,
                          "cs_diff_at_14": -10,
                          "deaths": 4,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235719,
                          "gold_earned": 13763,
                          "gold_percentage": 18.67,
                          "gold_spent": 11010,
                          "items": [
                            {
                              "id": 2465,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/167abf5d0dc59292a78b79ceadffcc99.png",
                              "is_trinket": false,
                              "name": "Negatron Cloak"
                            },
                            {
                              "id": 2493,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6828cf3bd100ca07d1da20e61a6547cb.png",
                              "is_trinket": false,
                              "name": "Guardian Angel"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2512,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1e29f7f8a099017ed7b1a6333a9357b1.png",
                              "is_trinket": false,
                              "name": "Kindlegem"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2985,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6feebaf2-10f6-4230-a6cb-da2a2a8cfb53.png",
                              "is_trinket": false,
                              "name": "Deicide"
                            }
                          ],
                          "kills": 5,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 142,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 5,
                            "turrets": 1,
                            "wards": 17
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 3,
                          "largest_multi_kill": 2,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 29999,
                            "dealt_percentage": 7.11,
                            "dealt_to_champions": 2302,
                            "dealt_to_champions_percentage": 7.37,
                            "taken": 9365
                          },
                          "masteries": [],
                          "minions_killed": 173,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 106391,
                            "dealt_percentage": 19.89,
                            "dealt_to_champions": 11038,
                            "dealt_to_champions_percentage": 24.74,
                            "taken": 20502
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-05-25",
                            "first_name": "Choi",
                            "id": 19283,
                            "image_url": "https://cdn.pandascore.co/images/player/image/19283/kdf_ellim_2022_split_2.png",
                            "last_name": "El-lim",
                            "modified_at": "2025-07-21T15:03:38Z",
                            "name": "Ellim",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "ellim"
                          },
                          "player_id": 19283,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 159747,
                            "dealt_percentage": 16.02,
                            "dealt_to_champions": 13830,
                            "dealt_to_champions_percentage": 17.88,
                            "taken": 32327
                          },
                          "total_heal": 12222,
                          "total_time_crowd_control_dealt": 100,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 23355,
                            "dealt_percentage": 57.39,
                            "dealt_to_champions": 489,
                            "dealt_to_champions_percentage": 33.42,
                            "taken": 2459
                          },
                          "wards": {
                            "placed": 19,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 18
                          },
                          "wards_placed": 19
                        },
                        {
                          "assists": 7,
                          "champion": {
                            "id": 3029,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/995ee5a952c1b157f6f40a5d893b7332.png",
                            "name": "Jinx",
                            "slug": "Jinx"
                          },
                          "creep_score": 486,
                          "cs_at_14": 150,
                          "cs_diff_at_14": 132,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235719,
                          "gold_earned": 17782,
                          "gold_percentage": 25.03,
                          "gold_spent": 17625,
                          "items": [
                            {
                              "id": 2494,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/fcd28e708879aa54037da3539604b1c4.png",
                              "is_trinket": false,
                              "name": "Infinity Edge"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2698,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1cc8c818e8f80cb70ec9a2e324c95632.png",
                              "is_trinket": false,
                              "name": "Kraken Slayer"
                            },
                            {
                              "id": 2714,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/2e9e74676892b4fbaf86c33e959bf373.png",
                              "is_trinket": false,
                              "name": "Rapid Firecannon"
                            },
                            {
                              "id": 2820,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/82133cdb92c1ca86e27b1e021faa84e9.png",
                              "is_trinket": false,
                              "name": "Lord Dominik's Regards"
                            },
                            {
                              "id": 2866,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/9fe203b01a6b9ae1849a8d0d65d4b48b.png",
                              "is_trinket": false,
                              "name": "Bloodthirster"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 68,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 1,
                            "wards": 29
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 803,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 7243,
                            "dealt_percentage": 2.52,
                            "dealt_to_champions": 1937,
                            "dealt_to_champions_percentage": 6.51,
                            "taken": 5574
                          },
                          "masteries": [],
                          "minions_killed": 486,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 350582,
                            "dealt_percentage": 46.72,
                            "dealt_to_champions": 14452,
                            "dealt_to_champions_percentage": 44.68,
                            "taken": 7856
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-02-06",
                            "first_name": "Lee",
                            "id": 19285,
                            "image_url": "https://cdn.pandascore.co/images/player/image/19285/t1_gumayusi_2023_split_2.png",
                            "last_name": "Min-hyeon",
                            "modified_at": "2026-01-06T07:15:49Z",
                            "name": "Gumayusi",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "gumayusi"
                          },
                          "player_id": 19285,
                          "role": "adc",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 23,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/65eea722a1fc79fb6469e7246eb0afb8.png",
                              "name": "Cleanse"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 380094,
                            "dealt_percentage": 34.17,
                            "dealt_to_champions": 17456,
                            "dealt_to_champions_percentage": 25.83,
                            "taken": 13617
                          },
                          "total_heal": 2501,
                          "total_time_crowd_control_dealt": 186,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 22267,
                            "dealt_percentage": 30.05,
                            "dealt_to_champions": 1066,
                            "dealt_to_champions_percentage": 19.5,
                            "taken": 186
                          },
                          "wards": {
                            "placed": 15,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 7
                          },
                          "wards_placed": 15
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3013,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/a883aa766debde85880d23396be80b0b.png",
                            "name": "Gangplank",
                            "slug": "Gangplank"
                          },
                          "creep_score": 318,
                          "cs_at_14": 115,
                          "cs_diff_at_14": 2,
                          "deaths": 5,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235719,
                          "gold_earned": 16958,
                          "gold_percentage": 23.87,
                          "gold_spent": 15208,
                          "items": [
                            {
                              "id": 2480,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/49631901cd0f2419b756e4118109e312.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2825,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3a6f184fabcf0b060a35cfe67ac8a530.png",
                              "is_trinket": false,
                              "name": "Serylda's Grudge"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2928,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6a940e698e30b4298a0e176358d10a66.png",
                              "is_trinket": false,
                              "name": "Ravenous Hydra"
                            },
                            {
                              "id": 2929,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/5b92dcbb3d964c0ad39b320d55601c9a.png",
                              "is_trinket": false,
                              "name": "Trinity Force"
                            },
                            {
                              "id": 3018,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6e620845d16abd235e4e5703ed8221b6.png",
                              "is_trinket": false,
                              "name": "Chempunk Chainsword"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 20,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 3,
                            "wards": 6
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 17,
                          "magic_damage": {
                            "dealt": 11817,
                            "dealt_percentage": 4.1,
                            "dealt_to_champions": 6547,
                            "dealt_to_champions_percentage": 22,
                            "taken": 6679
                          },
                          "masteries": [],
                          "minions_killed": 318,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 231693,
                            "dealt_percentage": 30.87,
                            "dealt_to_champions": 10170,
                            "dealt_to_champions_percentage": 31.44,
                            "taken": 19048
                          },
                          "player": {
                            "active": true,
                            "age": 21,
                            "birthday": "2004-01-31",
                            "first_name": "Choi",
                            "id": 31391,
                            "image_url": "https://cdn.pandascore.co/images/player/image/31391/t1_zeus_2023_split_2.png",
                            "last_name": "Woo-je",
                            "modified_at": "2026-01-06T07:15:50Z",
                            "name": "Zeus",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "zeus-choi-woo-je"
                          },
                          "player_id": 31391,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 266180,
                            "dealt_percentage": 23.93,
                            "dealt_to_champions": 18849,
                            "dealt_to_champions_percentage": 27.89,
                            "taken": 25904
                          },
                          "total_heal": 6106,
                          "total_time_crowd_control_dealt": 407,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 22668,
                            "dealt_percentage": 30.59,
                            "dealt_to_champions": 2131,
                            "dealt_to_champions_percentage": 38.97,
                            "taken": 176
                          },
                          "wards": {
                            "placed": 9,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 3
                          },
                          "wards_placed": 9
                        },
                        {
                          "assists": 4,
                          "champion": {
                            "id": 3142,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/1b4a743524b01e0885b8a6e84d5a8663.png",
                            "name": "Lee Sin",
                            "slug": "LeeSin"
                          },
                          "creep_score": 225,
                          "cs_at_14": 97,
                          "cs_diff_at_14": 10,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": true,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235719,
                          "gold_earned": 12779,
                          "gold_percentage": 17.99,
                          "gold_spent": 12850,
                          "items": [
                            {
                              "id": 2451,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7c23780ddc70d6db6bdbaff941acf146.png",
                              "is_trinket": false,
                              "name": "Chain Vest"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2677,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d764e2dad4b185bbbbc86ca2998d5313.png",
                              "is_trinket": true,
                              "name": "Stealth Ward"
                            },
                            {
                              "id": 2926,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/9e7450aaa9bd2694e330a2d84b974eba.png",
                              "is_trinket": false,
                              "name": "Sterak's Gage"
                            },
                            {
                              "id": 2927,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/a3d78560d3945a73d66da14f28d6b759.png",
                              "is_trinket": false,
                              "name": "Black Cleaver"
                            },
                            {
                              "id": 2935,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/97032f4cae42f011b132d0bca2438e8b.png",
                              "is_trinket": false,
                              "name": "Goredrinker"
                            }
                          ],
                          "kills": 5,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 173,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 5,
                            "turrets": 0,
                            "wards": 17
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 5,
                          "largest_multi_kill": 2,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 54447,
                            "dealt_percentage": 18.91,
                            "dealt_to_champions": 1741,
                            "dealt_to_champions_percentage": 5.85,
                            "taken": 9523
                          },
                          "masteries": [],
                          "minions_killed": 225,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 149111,
                            "dealt_percentage": 19.87,
                            "dealt_to_champions": 5796,
                            "dealt_to_champions_percentage": 17.92,
                            "taken": 19966
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-12-24",
                            "first_name": "Moon",
                            "id": 31392,
                            "image_url": "https://cdn.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                            "last_name": "Hyeon-joon",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Oner",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "oner"
                          },
                          "player_id": 31392,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 220684,
                            "dealt_percentage": 19.84,
                            "dealt_to_champions": 7950,
                            "dealt_to_champions_percentage": 11.76,
                            "taken": 30001
                          },
                          "total_heal": 8517,
                          "total_time_crowd_control_dealt": 637,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 17125,
                            "dealt_percentage": 23.11,
                            "dealt_to_champions": 413,
                            "dealt_to_champions_percentage": 7.55,
                            "taken": 512
                          },
                          "wards": {
                            "placed": 17,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 8
                          },
                          "wards_placed": 17
                        }
                      ],
                      "position": 3,
                      "status": "finished",
                      "teams": [
                        {
                          "atakhan_kills": null,
                          "bans": [
                            2981,
                            3008,
                            3147,
                            3098,
                            3031
                          ],
                          "baron_kills": 0,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 0,
                          "color": "blue",
                          "dragon_kills": 2,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": false,
                          "first_blood": true,
                          "first_dragon": true,
                          "first_herald": false,
                          "first_inhibitor": false,
                          "first_tower": true,
                          "first_voidgrub": null,
                          "gold_earned": 71047,
                          "herald_kills": 0,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 0,
                          "kills": 10,
                          "mountain_drake_kills": 1,
                          "ocean_drake_kills": 1,
                          "player_ids": [
                            585,
                            8158,
                            19285,
                            31391,
                            31392
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "tower_kills": 6,
                          "voidgrub_kills": null
                        },
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3120,
                            3000,
                            3099,
                            3134,
                            3048
                          ],
                          "baron_kills": 1,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 4,
                          "color": "red",
                          "dragon_kills": 4,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": true,
                          "first_blood": false,
                          "first_dragon": false,
                          "first_herald": true,
                          "first_inhibitor": true,
                          "first_tower": false,
                          "first_voidgrub": null,
                          "gold_earned": 73716,
                          "herald_kills": 2,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 1,
                          "kills": 19,
                          "mountain_drake_kills": 0,
                          "ocean_drake_kills": 0,
                          "player_ids": [
                            1456,
                            3524,
                            8142,
                            8924,
                            19283
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "tower_kills": 9,
                          "voidgrub_kills": null
                        }
                      ],
                      "winner": {
                        "id": 130063,
                        "type": "Team"
                      },
                      "winner_type": "Team"
                    },
                    {
                      "begin_at": "2022-06-29T12:37:26Z",
                      "complete": true,
                      "detailed_stats": true,
                      "end_at": "2022-06-29T13:15:37Z",
                      "finished": true,
                      "forfeit": false,
                      "id": 235718,
                      "length": 1876,
                      "match_id": 637569,
                      "players": [
                        {
                          "assists": 0,
                          "champion": {
                            "id": 2991,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/baf32ee97457437ea20c42ba23003e0c.png",
                            "name": "Azir",
                            "slug": "Azir"
                          },
                          "creep_score": 276,
                          "cs_at_14": 124,
                          "cs_diff_at_14": 21,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235718,
                          "gold_earned": 12239,
                          "gold_percentage": 23.26,
                          "gold_spent": 12325,
                          "items": [
                            {
                              "id": 2467,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/e914701535346c87ea1cfb1fb159631c.png",
                              "is_trinket": false,
                              "name": "Dark Seal"
                            },
                            {
                              "id": 2642,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d3c7dce8ed50a8553198bdefbacac855.png",
                              "is_trinket": false,
                              "name": "Needlessly Large Rod"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2871,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/8cef60e74adf20cb8372afd4aa49cde9.png",
                              "is_trinket": false,
                              "name": "Liandry's Anguish"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2924,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d4fde29e50e7ed8472b31f4a78134063.png",
                              "is_trinket": false,
                              "name": "Rylai's Crystal Scepter"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 16,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 1,
                            "wards": 7
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 144610,
                            "dealt_percentage": 52.69,
                            "dealt_to_champions": 19010,
                            "dealt_to_champions_percentage": 69.52,
                            "taken": 4467
                          },
                          "masteries": [],
                          "minions_killed": 276,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 8108,
                            "dealt_percentage": 2.23,
                            "dealt_to_champions": 210,
                            "dealt_to_champions_percentage": 1.75,
                            "taken": 8867
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-05-07",
                            "first_name": "Lee",
                            "id": 585,
                            "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                            "last_name": "Sang-hyeok",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Faker",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "faker"
                          },
                          "player_id": 585,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 153491,
                            "dealt_percentage": 21.99,
                            "dealt_to_champions": 19993,
                            "dealt_to_champions_percentage": 46.07,
                            "taken": 13754
                          },
                          "total_heal": 17,
                          "total_time_crowd_control_dealt": 392,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 771,
                            "dealt_percentage": 1.27,
                            "dealt_to_champions": 771,
                            "dealt_to_champions_percentage": 18.91,
                            "taken": 420
                          },
                          "wards": {
                            "placed": 14,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 9
                          },
                          "wards_placed": 14
                        },
                        {
                          "assists": 10,
                          "champion": {
                            "id": 3147,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/8f448f569bc040fbeaf36de3805ed2eb.png",
                            "name": "Senna",
                            "slug": "Senna"
                          },
                          "creep_score": 62,
                          "cs_at_14": 15,
                          "cs_diff_at_14": -109,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235718,
                          "gold_earned": 9665,
                          "gold_percentage": 16.86,
                          "gold_spent": 8075,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2489,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7c39a6acc5d50b697a09e78338c3d4a0.png",
                              "is_trinket": false,
                              "name": "Boots of Swiftness"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2806,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/f530d00c32c745acf57bf0521cf565f7.png",
                              "is_trinket": false,
                              "name": "Black Mist Scythe"
                            },
                            {
                              "id": 2912,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/eaef5f4c2f6f2d5fcf13f287c321e59b.png",
                              "is_trinket": false,
                              "name": "Eclipse"
                            },
                            {
                              "id": 2963,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/b024e8ca8cf9873201744933ec14c30c.png",
                              "is_trinket": false,
                              "name": "Umbral Glaive"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 4,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 0,
                            "wards": 35
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 440,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 13,
                          "magic_damage": {
                            "dealt": 162,
                            "dealt_percentage": 0.06,
                            "dealt_to_champions": 162,
                            "dealt_to_champions_percentage": 0.67,
                            "taken": 2071
                          },
                          "masteries": [],
                          "minions_killed": 62,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 48789,
                            "dealt_percentage": 12.39,
                            "dealt_to_champions": 10710,
                            "dealt_to_champions_percentage": 33.34,
                            "taken": 4509
                          },
                          "player": {
                            "active": true,
                            "age": 27,
                            "birthday": "1998-03-15",
                            "first_name": "Park",
                            "id": 1456,
                            "image_url": "https://cdn.pandascore.co/images/player/image/1456/t1_teddy_2021_split_2.png",
                            "last_name": "Jin-seong",
                            "modified_at": "2026-01-06T07:15:57Z",
                            "name": "Teddy",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "teddy"
                          },
                          "player_id": 1456,
                          "role": "adc",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 27,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/37e058ce96cf92adf6831ad5946956f4.png",
                              "name": "Exhaust"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 54545,
                            "dealt_percentage": 7.74,
                            "dealt_to_champions": 10872,
                            "dealt_to_champions_percentage": 18.43,
                            "taken": 6709
                          },
                          "total_heal": 8814,
                          "total_time_crowd_control_dealt": 201,
                          "total_units_healed": 5,
                          "true_damage": {
                            "dealt": 5593,
                            "dealt_percentage": 11.03,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 128
                          },
                          "wards": {
                            "placed": 57,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 17
                          },
                          "wards_placed": 57
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 3013,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/a883aa766debde85880d23396be80b0b.png",
                            "name": "Gangplank",
                            "slug": "Gangplank"
                          },
                          "creep_score": 285,
                          "cs_at_14": 114,
                          "cs_diff_at_14": -2,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235718,
                          "gold_earned": 14076,
                          "gold_percentage": 24.56,
                          "gold_spent": 10858,
                          "items": [
                            {
                              "id": 2473,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7e869611bdd37522a83fb50079aadafb.png",
                              "is_trinket": false,
                              "name": "Corrupting Potion"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2793,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3e1d3f42c8ef52ed8cc0338eb7873bb4.png",
                              "is_trinket": false,
                              "name": "Mortal Reminder"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2929,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/5b92dcbb3d964c0ad39b320d55601c9a.png",
                              "is_trinket": false,
                              "name": "Trinity Force"
                            },
                            {
                              "id": 2933,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/9eb16adb98fcdc9c9ae35eabe19c322f.png",
                              "is_trinket": false,
                              "name": "Maw of Malmortius"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 14,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 5,
                            "wards": 4
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 1061,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 2,
                          "level": 17,
                          "magic_damage": {
                            "dealt": 5747,
                            "dealt_percentage": 2.21,
                            "dealt_to_champions": 4290,
                            "dealt_to_champions_percentage": 17.66,
                            "taken": 4405
                          },
                          "masteries": [],
                          "minions_killed": 285,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 199356,
                            "dealt_percentage": 50.61,
                            "dealt_to_champions": 13870,
                            "dealt_to_champions_percentage": 43.18,
                            "taken": 8089
                          },
                          "player": {
                            "active": true,
                            "age": 26,
                            "birthday": "1999-05-28",
                            "first_name": "Kim",
                            "id": 3524,
                            "image_url": "https://cdn.pandascore.co/images/player/image/3524/kt_kiin_2023_split_2.png",
                            "last_name": "Gi-in ",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Kiin",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "kiin"
                          },
                          "player_id": 3524,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 216605,
                            "dealt_percentage": 30.72,
                            "dealt_to_champions": 19625,
                            "dealt_to_champions_percentage": 33.27,
                            "taken": 13958
                          },
                          "total_heal": 3928,
                          "total_time_crowd_control_dealt": 289,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 11500,
                            "dealt_percentage": 22.68,
                            "dealt_to_champions": 1464,
                            "dealt_to_champions_percentage": 56.85,
                            "taken": 1462
                          },
                          "wards": {
                            "placed": 19,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 9
                          },
                          "wards_placed": 19
                        },
                        {
                          "assists": 8,
                          "champion": {
                            "id": 3087,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/596326c80f939f6cafdb73d9e5917311.png",
                            "name": "Seraphine",
                            "slug": "Seraphine"
                          },
                          "creep_score": 236,
                          "cs_at_14": 95,
                          "cs_diff_at_14": 71,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": true,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235718,
                          "gold_earned": 11608,
                          "gold_percentage": 20.25,
                          "gold_spent": 10950,
                          "items": [
                            {
                              "id": 2499,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/95f8b2323890310c5d277d71551bc0e6.png",
                              "is_trinket": false,
                              "name": "Mejai's Soulstealer"
                            },
                            {
                              "id": 2642,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d3c7dce8ed50a8553198bdefbacac855.png",
                              "is_trinket": false,
                              "name": "Needlessly Large Rod"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2871,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/8cef60e74adf20cb8372afd4aa49cde9.png",
                              "is_trinket": false,
                              "name": "Liandry's Anguish"
                            },
                            {
                              "id": 2919,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/47c001c40f4d6d169be155b0a74e08d5.png",
                              "is_trinket": false,
                              "name": "Seraph's Embrace"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 3,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 2,
                            "wards": 3
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 132464,
                            "dealt_percentage": 50.86,
                            "dealt_to_champions": 8325,
                            "dealt_to_champions_percentage": 34.27,
                            "taken": 2831
                          },
                          "masteries": [],
                          "minions_killed": 236,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 15055,
                            "dealt_percentage": 3.82,
                            "dealt_to_champions": 936,
                            "dealt_to_champions_percentage": 2.91,
                            "taken": 5295
                          },
                          "player": {
                            "active": false,
                            "age": 26,
                            "birthday": "1999-07-06",
                            "first_name": "Ryu",
                            "id": 8142,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8142/t1.c_hoit_2021_split_2.png",
                            "last_name": "Ho-seong",
                            "modified_at": "2025-12-30T20:38:46Z",
                            "name": "Hoit",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "hoit"
                          },
                          "player_id": 8142,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 147768,
                            "dealt_percentage": 20.96,
                            "dealt_to_champions": 9347,
                            "dealt_to_champions_percentage": 15.84,
                            "taken": 8759
                          },
                          "total_heal": 5806,
                          "total_time_crowd_control_dealt": 143,
                          "total_units_healed": 5,
                          "true_damage": {
                            "dealt": 249,
                            "dealt_percentage": 0.49,
                            "dealt_to_champions": 85,
                            "dealt_to_champions_percentage": 3.3,
                            "taken": 632
                          },
                          "wards": {
                            "placed": 20,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 8
                          },
                          "wards_placed": 20
                        },
                        {
                          "assists": 2,
                          "champion": {
                            "id": 3101,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/57b819d64ef4ee6747946c7a4d53132f.png",
                            "name": "Tahm Kench",
                            "slug": "TahmKench"
                          },
                          "creep_score": 45,
                          "cs_at_14": 24,
                          "cs_diff_at_14": -71,
                          "deaths": 4,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235718,
                          "gold_earned": 6785,
                          "gold_percentage": 12.89,
                          "gold_spent": 6550,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2512,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1e29f7f8a099017ed7b1a6333a9357b1.png",
                              "is_trinket": false,
                              "name": "Kindlegem"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2804,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d05cf3b9331e5b13d9e4b73b4b1ff22a.png",
                              "is_trinket": false,
                              "name": "Bulwark of the Mountain"
                            },
                            {
                              "id": 2902,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7c53fbb2a912cc56797a86bfe1dc596f.png",
                              "is_trinket": false,
                              "name": "Locket of the Iron Solari"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 0,
                            "turrets": 0,
                            "wards": 15
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 10,
                          "magic_damage": {
                            "dealt": 12965,
                            "dealt_percentage": 4.72,
                            "dealt_to_champions": 3826,
                            "dealt_to_champions_percentage": 13.99,
                            "taken": 5912
                          },
                          "masteries": [],
                          "minions_killed": 45,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 3308,
                            "dealt_percentage": 0.91,
                            "dealt_to_champions": 402,
                            "dealt_to_champions_percentage": 3.36,
                            "taken": 10912
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-10-14",
                            "first_name": "Ryu",
                            "id": 8158,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                            "last_name": "Min-seok",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Keria",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "keria"
                          },
                          "player_id": 8158,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 24459,
                            "dealt_percentage": 3.5,
                            "dealt_to_champions": 4803,
                            "dealt_to_champions_percentage": 11.07,
                            "taken": 17317
                          },
                          "total_heal": 3119,
                          "total_time_crowd_control_dealt": 108,
                          "total_units_healed": 2,
                          "true_damage": {
                            "dealt": 8185,
                            "dealt_percentage": 13.51,
                            "dealt_to_champions": 574,
                            "dealt_to_champions_percentage": 14.08,
                            "taken": 492
                          },
                          "wards": {
                            "placed": 57,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 20
                          },
                          "wards_placed": 57
                        },
                        {
                          "assists": 7,
                          "champion": {
                            "id": 3098,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/f832bf9dbd11be46cc18f7635eea5348.png",
                            "name": "Swain",
                            "slug": "Swain"
                          },
                          "creep_score": 239,
                          "cs_at_14": 103,
                          "cs_diff_at_14": -21,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": true,
                            "first_tower_assist": true,
                            "first_tower_kill": false
                          },
                          "game_id": 235718,
                          "gold_earned": 11420,
                          "gold_percentage": 19.93,
                          "gold_spent": 9500,
                          "items": [
                            {
                              "id": 2473,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7e869611bdd37522a83fb50079aadafb.png",
                              "is_trinket": false,
                              "name": "Corrupting Potion"
                            },
                            {
                              "id": 2537,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                              "is_trinket": false,
                              "name": "Mercury's Treads"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2720,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d703d8cf515d6fef18fdbacd320248ad.png",
                              "is_trinket": false,
                              "name": "Imperial Mandate"
                            },
                            {
                              "id": 2776,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/000057177c6cd0f3895e67b2199dacb9.png",
                              "is_trinket": false,
                              "name": "Zhonya's Hourglass"
                            },
                            {
                              "id": 2924,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d4fde29e50e7ed8472b31f4a78134063.png",
                              "is_trinket": false,
                              "name": "Rylai's Crystal Scepter"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 0,
                            "wards": 6
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 108940,
                            "dealt_percentage": 41.83,
                            "dealt_to_champions": 10445,
                            "dealt_to_champions_percentage": 42.99,
                            "taken": 13569
                          },
                          "masteries": [],
                          "minions_killed": 239,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 23618,
                            "dealt_percentage": 6,
                            "dealt_to_champions": 1229,
                            "dealt_to_champions_percentage": 3.83,
                            "taken": 5670
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-08-22",
                            "first_name": "Yoo",
                            "id": 8924,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8924/kdf_fate_2022_split_2.png",
                            "last_name": "Su-hyeok",
                            "modified_at": "2025-08-15T13:43:55Z",
                            "name": "FATE",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "fate"
                          },
                          "player_id": 8924,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 147158,
                            "dealt_percentage": 20.87,
                            "dealt_to_champions": 12024,
                            "dealt_to_champions_percentage": 20.38,
                            "taken": 19879
                          },
                          "total_heal": 6372,
                          "total_time_crowd_control_dealt": 357,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 14600,
                            "dealt_percentage": 28.79,
                            "dealt_to_champions": 350,
                            "dealt_to_champions_percentage": 13.59,
                            "taken": 638
                          },
                          "wards": {
                            "placed": 9,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 6
                          },
                          "wards_placed": 9
                        },
                        {
                          "assists": 3,
                          "champion": {
                            "id": 3120,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/cbc53ec5b2ef342a710ba2c56ca13915.png",
                            "name": "Viego",
                            "slug": "Viego"
                          },
                          "creep_score": 166,
                          "cs_at_14": 82,
                          "cs_diff_at_14": -6,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235718,
                          "gold_earned": 10542,
                          "gold_percentage": 18.39,
                          "gold_spent": 7900,
                          "items": [
                            {
                              "id": 2450,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/5ff4236356a2fc30dd646724b53a5354.png",
                              "is_trinket": false,
                              "name": "Cloth Armor"
                            },
                            {
                              "id": 2481,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/84b0db5c9726c8bd47c9c8c088f6e8fb.png",
                              "is_trinket": false,
                              "name": "Broken Stopwatch"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2932,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3b53081565041e3e40a806f68cb7a360.png",
                              "is_trinket": false,
                              "name": "Hexdrinker"
                            },
                            {
                              "id": 2937,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/0085138b38b1f85411988b1db668bc94.png",
                              "is_trinket": false,
                              "name": "Divine Sunderer"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 131,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 4,
                            "turrets": 0,
                            "wards": 17
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 4,
                          "largest_multi_kill": 2,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 13126,
                            "dealt_percentage": 5.04,
                            "dealt_to_champions": 1072,
                            "dealt_to_champions_percentage": 4.41,
                            "taken": 6005
                          },
                          "masteries": [],
                          "minions_killed": 166,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 107113,
                            "dealt_percentage": 27.19,
                            "dealt_to_champions": 5375,
                            "dealt_to_champions_percentage": 16.73,
                            "taken": 12235
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-05-25",
                            "first_name": "Choi",
                            "id": 19283,
                            "image_url": "https://cdn.pandascore.co/images/player/image/19283/kdf_ellim_2022_split_2.png",
                            "last_name": "El-lim",
                            "modified_at": "2025-07-21T15:03:38Z",
                            "name": "Ellim",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "ellim"
                          },
                          "player_id": 19283,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 139014,
                            "dealt_percentage": 19.72,
                            "dealt_to_champions": 7123,
                            "dealt_to_champions_percentage": 12.07,
                            "taken": 19456
                          },
                          "total_heal": 10190,
                          "total_time_crowd_control_dealt": 183,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 18774,
                            "dealt_percentage": 37.02,
                            "dealt_to_champions": 676,
                            "dealt_to_champions_percentage": 26.25,
                            "taken": 1216
                          },
                          "wards": {
                            "placed": 16,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 19
                          },
                          "wards_placed": 16
                        },
                        {
                          "assists": 1,
                          "champion": {
                            "id": 3031,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/e05b5fd8059a74ff2a93e5e470865b11.png",
                            "name": "Kalista",
                            "slug": "Kalista"
                          },
                          "creep_score": 343,
                          "cs_at_14": 124,
                          "cs_diff_at_14": 109,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235718,
                          "gold_earned": 12997,
                          "gold_percentage": 24.7,
                          "gold_spent": 12575,
                          "items": [
                            {
                              "id": 2456,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/dc01e13700dcf1cc4c4ad8a5939e17dc.png",
                              "is_trinket": false,
                              "name": "B. F. Sword"
                            },
                            {
                              "id": 2544,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/924cb9f122b90bf1ee29b9650c092524.png",
                              "is_trinket": false,
                              "name": "Guinsoo's Rageblade"
                            },
                            {
                              "id": 2639,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7d33d9c83789bb40d7710612438109e0.png",
                              "is_trinket": false,
                              "name": "Vampiric Scepter"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2699,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/0f33f102856e8d40f6d38ff057856e1d.png",
                              "is_trinket": false,
                              "name": "Immortal Shieldbow"
                            },
                            {
                              "id": 2763,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1a0dab15964871b507375c342d5536bc.png",
                              "is_trinket": false,
                              "name": "Runaan's Hurricane"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 24,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 0,
                            "turrets": 2,
                            "wards": 13
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 238,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 275,
                            "dealt_percentage": 0.1,
                            "dealt_to_champions": 125,
                            "dealt_to_champions_percentage": 0.46,
                            "taken": 4891
                          },
                          "masteries": [],
                          "minions_killed": 343,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 209074,
                            "dealt_percentage": 57.59,
                            "dealt_to_champions": 7388,
                            "dealt_to_champions_percentage": 61.72,
                            "taken": 7454
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-02-06",
                            "first_name": "Lee",
                            "id": 19285,
                            "image_url": "https://cdn.pandascore.co/images/player/image/19285/t1_gumayusi_2023_split_2.png",
                            "last_name": "Min-hyeon",
                            "modified_at": "2026-01-06T07:15:49Z",
                            "name": "Gumayusi",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "gumayusi"
                          },
                          "player_id": 19285,
                          "role": "adc",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 23,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/65eea722a1fc79fb6469e7246eb0afb8.png",
                              "name": "Cleanse"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 211215,
                            "dealt_percentage": 30.26,
                            "dealt_to_champions": 7514,
                            "dealt_to_champions_percentage": 17.31,
                            "taken": 12663
                          },
                          "total_heal": 760,
                          "total_time_crowd_control_dealt": 391,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 1865,
                            "dealt_percentage": 3.08,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 317
                          },
                          "wards": {
                            "placed": 14,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 7
                          },
                          "wards_placed": 14
                        },
                        {
                          "assists": 0,
                          "champion": {
                            "id": 3018,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/a7483c3b14ed866fecd8726a1046187b.png",
                            "name": "Gwen",
                            "slug": "Gwen"
                          },
                          "creep_score": 276,
                          "cs_at_14": 116,
                          "cs_diff_at_14": 2,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235718,
                          "gold_earned": 11377,
                          "gold_percentage": 21.62,
                          "gold_spent": 11725,
                          "items": [
                            {
                              "id": 2540,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/e0bb551fce03c63d9385356960cbfce0.png",
                              "is_trinket": false,
                              "name": "Nashor's Tooth"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2907,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3f929f236ba0734da501690a3c38174.png",
                              "is_trinket": false,
                              "name": "Demonic Embrace"
                            },
                            {
                              "id": 3017,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/81cd1acbc7ee06bec32014055901b37e.png",
                              "is_trinket": false,
                              "name": "Riftmaker"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 12,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 0,
                            "turrets": 1,
                            "wards": 10
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 73525,
                            "dealt_percentage": 26.79,
                            "dealt_to_champions": 3791,
                            "dealt_to_champions_percentage": 13.86,
                            "taken": 4081
                          },
                          "masteries": [],
                          "minions_killed": 276,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 47898,
                            "dealt_percentage": 13.19,
                            "dealt_to_champions": 1473,
                            "dealt_to_champions_percentage": 12.3,
                            "taken": 18141
                          },
                          "player": {
                            "active": true,
                            "age": 21,
                            "birthday": "2004-01-31",
                            "first_name": "Choi",
                            "id": 31391,
                            "image_url": "https://cdn.pandascore.co/images/player/image/31391/t1_zeus_2023_split_2.png",
                            "last_name": "Woo-je",
                            "modified_at": "2026-01-06T07:15:50Z",
                            "name": "Zeus",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "zeus-choi-woo-je"
                          },
                          "player_id": 31391,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 29,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/58955cb861c3b51375948a05e260996a.png",
                              "name": "Ghost"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 157546,
                            "dealt_percentage": 22.57,
                            "dealt_to_champions": 7594,
                            "dealt_to_champions_percentage": 17.5,
                            "taken": 23067
                          },
                          "total_heal": 2648,
                          "total_time_crowd_control_dealt": 104,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 36123,
                            "dealt_percentage": 59.63,
                            "dealt_to_champions": 2329,
                            "dealt_to_champions_percentage": 57.11,
                            "taken": 844
                          },
                          "wards": {
                            "placed": 12,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 7
                          },
                          "wards_placed": 12
                        },
                        {
                          "assists": 0,
                          "champion": {
                            "id": 3056,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/842947265b0e075804b15ae06011afda.png",
                            "name": "Wukong",
                            "slug": "MonkeyKing"
                          },
                          "creep_score": 184,
                          "cs_at_14": 88,
                          "cs_diff_at_14": 6,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235718,
                          "gold_earned": 9228,
                          "gold_percentage": 17.54,
                          "gold_spent": 9250,
                          "items": [
                            {
                              "id": 2451,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7c23780ddc70d6db6bdbaff941acf146.png",
                              "is_trinket": false,
                              "name": "Chain Vest"
                            },
                            {
                              "id": 2481,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/84b0db5c9726c8bd47c9c8c088f6e8fb.png",
                              "is_trinket": false,
                              "name": "Broken Stopwatch"
                            },
                            {
                              "id": 2537,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                              "is_trinket": false,
                              "name": "Mercury's Treads"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2937,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/0085138b38b1f85411988b1db668bc94.png",
                              "is_trinket": false,
                              "name": "Divine Sunderer"
                            },
                            {
                              "id": 3018,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6e620845d16abd235e4e5703ed8221b6.png",
                              "is_trinket": false,
                              "name": "Chempunk Chainsword"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 162,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 0,
                            "wards": 13
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 13,
                          "magic_damage": {
                            "dealt": 43059,
                            "dealt_percentage": 15.69,
                            "dealt_to_champions": 591,
                            "dealt_to_champions_percentage": 2.16,
                            "taken": 8057
                          },
                          "masteries": [],
                          "minions_killed": 184,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 94659,
                            "dealt_percentage": 26.07,
                            "dealt_to_champions": 2498,
                            "dealt_to_champions_percentage": 20.87,
                            "taken": 16028
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-12-24",
                            "first_name": "Moon",
                            "id": 31392,
                            "image_url": "https://cdn.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                            "last_name": "Hyeon-joon",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Oner",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "oner"
                          },
                          "player_id": 31392,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 151352,
                            "dealt_percentage": 21.68,
                            "dealt_to_champions": 3493,
                            "dealt_to_champions_percentage": 8.05,
                            "taken": 24587
                          },
                          "total_heal": 8990,
                          "total_time_crowd_control_dealt": 180,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 13634,
                            "dealt_percentage": 22.51,
                            "dealt_to_champions": 404,
                            "dealt_to_champions_percentage": 9.91,
                            "taken": 500
                          },
                          "wards": {
                            "placed": 9,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 8
                          },
                          "wards_placed": 9
                        }
                      ],
                      "position": 2,
                      "status": "finished",
                      "teams": [
                        {
                          "atakhan_kills": null,
                          "bans": [
                            2981,
                            3068,
                            3110,
                            2982,
                            3131
                          ],
                          "baron_kills": 0,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 1,
                          "color": "blue",
                          "dragon_kills": 1,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": false,
                          "first_blood": false,
                          "first_dragon": false,
                          "first_herald": true,
                          "first_inhibitor": false,
                          "first_tower": false,
                          "first_voidgrub": null,
                          "gold_earned": 52626,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 0,
                          "kills": 2,
                          "mountain_drake_kills": 0,
                          "ocean_drake_kills": 0,
                          "player_ids": [
                            585,
                            8158,
                            19285,
                            31391,
                            31392
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "tower_kills": 4,
                          "voidgrub_kills": null
                        },
                        {
                          "atakhan_kills": null,
                          "bans": [
                            2985,
                            3000,
                            3078,
                            3048,
                            3134
                          ],
                          "baron_kills": 1,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 1,
                          "color": "red",
                          "dragon_kills": 3,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": true,
                          "first_blood": true,
                          "first_dragon": true,
                          "first_herald": false,
                          "first_inhibitor": true,
                          "first_tower": true,
                          "first_voidgrub": null,
                          "gold_earned": 57311,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 1,
                          "kills": 12,
                          "mountain_drake_kills": 1,
                          "ocean_drake_kills": 1,
                          "player_ids": [
                            1456,
                            3524,
                            8142,
                            8924,
                            19283
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "tower_kills": 6,
                          "voidgrub_kills": null
                        }
                      ],
                      "winner": {
                        "id": 130063,
                        "type": "Team"
                      },
                      "winner_type": "Team"
                    },
                    {
                      "begin_at": "2022-06-29T11:46:04Z",
                      "complete": true,
                      "detailed_stats": true,
                      "end_at": "2022-06-29T12:21:47Z",
                      "finished": true,
                      "forfeit": false,
                      "id": 235717,
                      "length": 1675,
                      "match_id": 637569,
                      "players": [
                        {
                          "assists": 6,
                          "champion": {
                            "id": 2991,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/baf32ee97457437ea20c42ba23003e0c.png",
                            "name": "Azir",
                            "slug": "Azir"
                          },
                          "creep_score": 251,
                          "cs_at_14": 129,
                          "cs_diff_at_14": 3,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": true,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235717,
                          "gold_earned": 12875,
                          "gold_percentage": 23.43,
                          "gold_spent": 11000,
                          "items": [
                            {
                              "id": 2480,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/49631901cd0f2419b756e4118109e312.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2871,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/8cef60e74adf20cb8372afd4aa49cde9.png",
                              "is_trinket": false,
                              "name": "Liandry's Anguish"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2924,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d4fde29e50e7ed8472b31f4a78134063.png",
                              "is_trinket": false,
                              "name": "Rylai's Crystal Scepter"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 2,
                            "neutral_minions": 12,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 2,
                            "wards": 3
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 159102,
                            "dealt_percentage": 60.56,
                            "dealt_to_champions": 30011,
                            "dealt_to_champions_percentage": 62.16,
                            "taken": 2499
                          },
                          "masteries": [],
                          "minions_killed": 251,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 7011,
                            "dealt_percentage": 2.21,
                            "dealt_to_champions": 422,
                            "dealt_to_champions_percentage": 2.23,
                            "taken": 6037
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-05-07",
                            "first_name": "Lee",
                            "id": 585,
                            "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                            "last_name": "Sang-hyeok",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Faker",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "faker"
                          },
                          "player_id": 585,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 167346,
                            "dealt_percentage": 25.16,
                            "dealt_to_champions": 31667,
                            "dealt_to_champions_percentage": 42.25,
                            "taken": 8607
                          },
                          "total_heal": 38,
                          "total_time_crowd_control_dealt": 414,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 1233,
                            "dealt_percentage": 1.45,
                            "dealt_to_champions": 1233,
                            "dealt_to_champions_percentage": 15.9,
                            "taken": 70
                          },
                          "wards": {
                            "placed": 13,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 4
                          },
                          "wards_placed": 13
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3147,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/8f448f569bc040fbeaf36de3805ed2eb.png",
                            "name": "Senna",
                            "slug": "Senna"
                          },
                          "creep_score": 76,
                          "cs_at_14": 33,
                          "cs_diff_at_14": -89,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235717,
                          "gold_earned": 8131,
                          "gold_percentage": 18.65,
                          "gold_spent": 7850,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2489,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/7c39a6acc5d50b697a09e78338c3d4a0.png",
                              "is_trinket": false,
                              "name": "Boots of Swiftness"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2806,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/f530d00c32c745acf57bf0521cf565f7.png",
                              "is_trinket": false,
                              "name": "Black Mist Scythe"
                            },
                            {
                              "id": 2912,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/eaef5f4c2f6f2d5fcf13f287c321e59b.png",
                              "is_trinket": false,
                              "name": "Eclipse"
                            },
                            {
                              "id": 2963,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/b024e8ca8cf9873201744933ec14c30c.png",
                              "is_trinket": false,
                              "name": "Umbral Glaive"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 4,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 2,
                            "turrets": 0,
                            "wards": 28
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 379,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 11,
                          "magic_damage": {
                            "dealt": 0,
                            "dealt_percentage": 0,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 6853
                          },
                          "masteries": [],
                          "minions_killed": 76,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 59712,
                            "dealt_percentage": 23.03,
                            "dealt_to_champions": 12329,
                            "dealt_to_champions_percentage": 50.03,
                            "taken": 4644
                          },
                          "player": {
                            "active": true,
                            "age": 27,
                            "birthday": "1998-03-15",
                            "first_name": "Park",
                            "id": 1456,
                            "image_url": "https://cdn.pandascore.co/images/player/image/1456/t1_teddy_2021_split_2.png",
                            "last_name": "Jin-seong",
                            "modified_at": "2026-01-06T07:15:57Z",
                            "name": "Teddy",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "teddy"
                          },
                          "player_id": 1456,
                          "role": "adc",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 30,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/62cc94a564835cd3abd80d74346c35da.png",
                              "name": "Heal"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 59870,
                            "dealt_percentage": 12.51,
                            "dealt_to_champions": 12425,
                            "dealt_to_champions_percentage": 29.12,
                            "taken": 12085
                          },
                          "total_heal": 12151,
                          "total_time_crowd_control_dealt": 277,
                          "total_units_healed": 5,
                          "true_damage": {
                            "dealt": 158,
                            "dealt_percentage": 0.59,
                            "dealt_to_champions": 96,
                            "dealt_to_champions_percentage": 14.35,
                            "taken": 587
                          },
                          "wards": {
                            "placed": 51,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 14
                          },
                          "wards_placed": 51
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3141,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/c8033f9a53a37b2055e4305aa852a9b3.png",
                            "name": "Kayle",
                            "slug": "Kayle"
                          },
                          "creep_score": 239,
                          "cs_at_14": 93,
                          "cs_diff_at_14": -29,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235717,
                          "gold_earned": 9547,
                          "gold_percentage": 21.9,
                          "gold_spent": 9525,
                          "items": [
                            {
                              "id": 2447,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/93bb71d5aba94a73ab32a16bf3708869.png",
                              "is_trinket": false,
                              "name": "Blasting Wand"
                            },
                            {
                              "id": 2472,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6cf6837b7cc656d332c883d0ebde2f67.png",
                              "is_trinket": false,
                              "name": "Refillable Potion"
                            },
                            {
                              "id": 2540,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/e0bb551fce03c63d9385356960cbfce0.png",
                              "is_trinket": false,
                              "name": "Nashor's Tooth"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2930,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/5bc313a2ec67cebd731e4cf0549cb077.png",
                              "is_trinket": false,
                              "name": "Wit's End"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 7,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 0,
                            "turrets": 0,
                            "wards": 9
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 81545,
                            "dealt_percentage": 42.38,
                            "dealt_to_champions": 5808,
                            "dealt_to_champions_percentage": 33.47,
                            "taken": 6717
                          },
                          "masteries": [],
                          "minions_killed": 239,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 58856,
                            "dealt_percentage": 22.7,
                            "dealt_to_champions": 4721,
                            "dealt_to_champions_percentage": 19.16,
                            "taken": 6586
                          },
                          "player": {
                            "active": true,
                            "age": 26,
                            "birthday": "1999-05-28",
                            "first_name": "Kim",
                            "id": 3524,
                            "image_url": "https://cdn.pandascore.co/images/player/image/3524/kt_kiin_2023_split_2.png",
                            "last_name": "Gi-in ",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Kiin",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "kiin"
                          },
                          "player_id": 3524,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 143404,
                            "dealt_percentage": 29.96,
                            "dealt_to_champions": 10529,
                            "dealt_to_champions_percentage": 24.68,
                            "taken": 15595
                          },
                          "total_heal": 6212,
                          "total_time_crowd_control_dealt": 186,
                          "total_units_healed": 5,
                          "true_damage": {
                            "dealt": 3002,
                            "dealt_percentage": 11.16,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 2292
                          },
                          "wards": {
                            "placed": 13,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 5
                          },
                          "wards_placed": 13
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 3101,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/57b819d64ef4ee6747946c7a4d53132f.png",
                            "name": "Tahm Kench",
                            "slug": "TahmKench"
                          },
                          "creep_score": 151,
                          "cs_at_14": 81,
                          "cs_diff_at_14": 80,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235717,
                          "gold_earned": 8046,
                          "gold_percentage": 18.46,
                          "gold_spent": 7975,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2640,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/178aee5eaa5e7a70f6a05155b7dcf3e2.png",
                              "is_trinket": false,
                              "name": "Doran's Shield"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2688,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c38d52b6bb9b984bf353c56585dae43d.png",
                              "is_trinket": false,
                              "name": "Force of Nature"
                            },
                            {
                              "id": 3019,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/5c65145d1a8bab82316337cd7e27cd6c.png",
                              "is_trinket": false,
                              "name": "Frostfire Gauntlet"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 0,
                            "wards": 4
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 13,
                          "magic_damage": {
                            "dealt": 44448,
                            "dealt_percentage": 23.1,
                            "dealt_to_champions": 6919,
                            "dealt_to_champions_percentage": 39.88,
                            "taken": 11255
                          },
                          "masteries": [],
                          "minions_killed": 151,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 16244,
                            "dealt_percentage": 6.26,
                            "dealt_to_champions": 634,
                            "dealt_to_champions_percentage": 2.57,
                            "taken": 8359
                          },
                          "player": {
                            "active": false,
                            "age": 26,
                            "birthday": "1999-07-06",
                            "first_name": "Ryu",
                            "id": 8142,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8142/t1.c_hoit_2021_split_2.png",
                            "last_name": "Ho-seong",
                            "modified_at": "2025-12-30T20:38:46Z",
                            "name": "Hoit",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "hoit"
                          },
                          "player_id": 8142,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 27,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/37e058ce96cf92adf6831ad5946956f4.png",
                              "name": "Exhaust"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 60692,
                            "dealt_percentage": 12.68,
                            "dealt_to_champions": 7554,
                            "dealt_to_champions_percentage": 17.7,
                            "taken": 21566
                          },
                          "total_heal": 5407,
                          "total_time_crowd_control_dealt": 786,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 0,
                            "dealt_percentage": 0,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 1950
                          },
                          "wards": {
                            "placed": 12,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 7
                          },
                          "wards_placed": 12
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 3059,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/e8bad58096e0bf120d2945d2ae8c83cb.png",
                            "name": "Nami",
                            "slug": "Nami"
                          },
                          "creep_score": 5,
                          "cs_at_14": 1,
                          "cs_diff_at_14": -80,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235717,
                          "gold_earned": 7643,
                          "gold_percentage": 13.91,
                          "gold_spent": 7425,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2720,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/d703d8cf515d6fef18fdbacd320248ad.png",
                              "is_trinket": false,
                              "name": "Imperial Mandate"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 3007,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/a53f4c97c8d30ad58cb978e397107463.png",
                              "is_trinket": false,
                              "name": "Chemtech Putrifier"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 0,
                            "wards": 4
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 11,
                          "magic_damage": {
                            "dealt": 10001,
                            "dealt_percentage": 3.81,
                            "dealt_to_champions": 5138,
                            "dealt_to_champions_percentage": 10.64,
                            "taken": 1508
                          },
                          "masteries": [],
                          "minions_killed": 5,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 5891,
                            "dealt_percentage": 1.86,
                            "dealt_to_champions": 1392,
                            "dealt_to_champions_percentage": 7.36,
                            "taken": 4514
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-10-14",
                            "first_name": "Ryu",
                            "id": 8158,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                            "last_name": "Min-seok",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Keria",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "keria"
                          },
                          "player_id": 8158,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 16759,
                            "dealt_percentage": 2.52,
                            "dealt_to_champions": 7397,
                            "dealt_to_champions_percentage": 9.87,
                            "taken": 6022
                          },
                          "total_heal": 4490,
                          "total_time_crowd_control_dealt": 232,
                          "total_units_healed": 5,
                          "true_damage": {
                            "dealt": 866,
                            "dealt_percentage": 1.02,
                            "dealt_to_champions": 866,
                            "dealt_to_champions_percentage": 11.16,
                            "taken": 0
                          },
                          "wards": {
                            "placed": 63,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 15
                          },
                          "wards_placed": 63
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3068,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/c85a85ae33a47512d18da2cf10d65a90.png",
                            "name": "Ornn",
                            "slug": "Ornn"
                          },
                          "creep_score": 198,
                          "cs_at_14": 126,
                          "cs_diff_at_14": -3,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235717,
                          "gold_earned": 8794,
                          "gold_percentage": 20.17,
                          "gold_spent": 8875,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2660,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c5709a137fafe955c32ae4511fb78d99.png",
                              "is_trinket": false,
                              "name": "Tear of the Goddess"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2688,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c38d52b6bb9b984bf353c56585dae43d.png",
                              "is_trinket": false,
                              "name": "Force of Nature"
                            },
                            {
                              "id": 2862,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/cd94b3bb54d41475f8a5e68c262f8c9c.png",
                              "is_trinket": false,
                              "name": "Bramble Vest"
                            },
                            {
                              "id": 3023,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/88ccb778-dc32-46ff-85d2-65f2f7c5158a.png",
                              "is_trinket": false,
                              "name": "Rimeforged Grasp"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 3,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 0,
                            "wards": 2
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 14,
                          "magic_damage": {
                            "dealt": 53164,
                            "dealt_percentage": 27.63,
                            "dealt_to_champions": 4001,
                            "dealt_to_champions_percentage": 23.06,
                            "taken": 17250
                          },
                          "masteries": [],
                          "minions_killed": 198,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 40653,
                            "dealt_percentage": 15.68,
                            "dealt_to_champions": 1673,
                            "dealt_to_champions_percentage": 6.79,
                            "taken": 7394
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-08-22",
                            "first_name": "Yoo",
                            "id": 8924,
                            "image_url": "https://cdn.pandascore.co/images/player/image/8924/kdf_fate_2022_split_2.png",
                            "last_name": "Su-hyeok",
                            "modified_at": "2025-08-15T13:43:55Z",
                            "name": "FATE",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "fate"
                          },
                          "player_id": 8924,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 100640,
                            "dealt_percentage": 21.03,
                            "dealt_to_champions": 5874,
                            "dealt_to_champions_percentage": 13.77,
                            "taken": 26076
                          },
                          "total_heal": 853,
                          "total_time_crowd_control_dealt": 980,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 6823,
                            "dealt_percentage": 25.37,
                            "dealt_to_champions": 200,
                            "dealt_to_champions_percentage": 29.9,
                            "taken": 1431
                          },
                          "wards": {
                            "placed": 8,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 7
                          },
                          "wards_placed": 8
                        },
                        {
                          "assists": 2,
                          "champion": {
                            "id": 3120,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/cbc53ec5b2ef342a710ba2c56ca13915.png",
                            "name": "Viego",
                            "slug": "Viego"
                          },
                          "creep_score": 136,
                          "cs_at_14": 84,
                          "cs_diff_at_14": -7,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235717,
                          "gold_earned": 9075,
                          "gold_percentage": 20.82,
                          "gold_spent": 9050,
                          "items": [
                            {
                              "id": 2472,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6cf6837b7cc656d332c883d0ebde2f67.png",
                              "is_trinket": false,
                              "name": "Refillable Potion"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2480,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/49631901cd0f2419b756e4118109e312.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2933,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/9eb16adb98fcdc9c9ae35eabe19c322f.png",
                              "is_trinket": false,
                              "name": "Maw of Malmortius"
                            },
                            {
                              "id": 2937,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/0085138b38b1f85411988b1db668bc94.png",
                              "is_trinket": false,
                              "name": "Divine Sunderer"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 108,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 4,
                            "turrets": 0,
                            "wards": 9
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 3,
                          "largest_multi_kill": 2,
                          "level": 13,
                          "magic_damage": {
                            "dealt": 13264,
                            "dealt_percentage": 6.89,
                            "dealt_to_champions": 623,
                            "dealt_to_champions_percentage": 3.59,
                            "taken": 8096
                          },
                          "masteries": [],
                          "minions_killed": 136,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 83842,
                            "dealt_percentage": 32.33,
                            "dealt_to_champions": 5287,
                            "dealt_to_champions_percentage": 21.45,
                            "taken": 8413
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-05-25",
                            "first_name": "Choi",
                            "id": 19283,
                            "image_url": "https://cdn.pandascore.co/images/player/image/19283/kdf_ellim_2022_split_2.png",
                            "last_name": "El-lim",
                            "modified_at": "2025-07-21T15:03:38Z",
                            "name": "Ellim",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "ellim"
                          },
                          "player_id": 19283,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "total_damage": {
                            "dealt": 114017,
                            "dealt_percentage": 23.82,
                            "dealt_to_champions": 6284,
                            "dealt_to_champions_percentage": 14.73,
                            "taken": 18005
                          },
                          "total_heal": 7647,
                          "total_time_crowd_control_dealt": 80,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 16910,
                            "dealt_percentage": 62.88,
                            "dealt_to_champions": 373,
                            "dealt_to_champions_percentage": 55.75,
                            "taken": 1494
                          },
                          "wards": {
                            "placed": 13,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 16
                          },
                          "wards_placed": 13
                        },
                        {
                          "assists": 2,
                          "champion": {
                            "id": 3048,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/f20ca11ca10442feb6293133a4af552c.png",
                            "name": "Lucian",
                            "slug": "Lucian"
                          },
                          "creep_score": 281,
                          "cs_at_14": 122,
                          "cs_diff_at_14": 89,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235717,
                          "gold_earned": 12465,
                          "gold_percentage": 22.68,
                          "gold_spent": 11800,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2494,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/fcd28e708879aa54037da3539604b1c4.png",
                              "is_trinket": false,
                              "name": "Infinity Edge"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2727,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/6c611c3082d7c565a4e4ba63d3255c10.png",
                              "is_trinket": false,
                              "name": "Galeforce"
                            },
                            {
                              "id": 2820,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/82133cdb92c1ca86e27b1e021faa84e9.png",
                              "is_trinket": false,
                              "name": "Lord Dominik's Regards"
                            }
                          ],
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 27,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 3,
                            "turrets": 1,
                            "wards": 14
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 582,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 14,
                          "magic_damage": {
                            "dealt": 13931,
                            "dealt_percentage": 5.3,
                            "dealt_to_champions": 3442,
                            "dealt_to_champions_percentage": 7.13,
                            "taken": 2347
                          },
                          "masteries": [],
                          "minions_killed": 281,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 156490,
                            "dealt_percentage": 49.35,
                            "dealt_to_champions": 10234,
                            "dealt_to_champions_percentage": 54.12,
                            "taken": 9244
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-02-06",
                            "first_name": "Lee",
                            "id": 19285,
                            "image_url": "https://cdn.pandascore.co/images/player/image/19285/t1_gumayusi_2023_split_2.png",
                            "last_name": "Min-hyeon",
                            "modified_at": "2026-01-06T07:15:49Z",
                            "name": "Gumayusi",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "gumayusi"
                          },
                          "player_id": 19285,
                          "role": "adc",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 179698,
                            "dealt_percentage": 27.02,
                            "dealt_to_champions": 13785,
                            "dealt_to_champions_percentage": 18.39,
                            "taken": 11812
                          },
                          "total_heal": 0,
                          "total_time_crowd_control_dealt": 71,
                          "total_units_healed": 0,
                          "true_damage": {
                            "dealt": 9276,
                            "dealt_percentage": 10.88,
                            "dealt_to_champions": 108,
                            "dealt_to_champions_percentage": 1.39,
                            "taken": 220
                          },
                          "wards": {
                            "placed": 16,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 10
                          },
                          "wards_placed": 16
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 3018,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/a7483c3b14ed866fecd8726a1046187b.png",
                            "name": "Gwen",
                            "slug": "Gwen"
                          },
                          "creep_score": 246,
                          "cs_at_14": 122,
                          "cs_diff_at_14": 29,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": true
                          },
                          "game_id": 235717,
                          "gold_earned": 12361,
                          "gold_percentage": 22.49,
                          "gold_spent": 10535,
                          "items": [
                            {
                              "id": 2447,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/93bb71d5aba94a73ab32a16bf3708869.png",
                              "is_trinket": false,
                              "name": "Blasting Wand"
                            },
                            {
                              "id": 2459,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/a6e22f9da01ca771ca63126e1ff93ac6.png",
                              "is_trinket": false,
                              "name": "Recurve Bow"
                            },
                            {
                              "id": 2460,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/0f07d995a4de9dc12ffaf8c403658755.png",
                              "is_trinket": false,
                              "name": "Amplifying Tome"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2907,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3f929f236ba0734da501690a3c38174.png",
                              "is_trinket": false,
                              "name": "Demonic Embrace"
                            },
                            {
                              "id": 3017,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/81cd1acbc7ee06bec32014055901b37e.png",
                              "is_trinket": false,
                              "name": "Riftmaker"
                            }
                          ],
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 12,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 3,
                            "turrets": 4,
                            "wards": 7
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 65310,
                            "dealt_percentage": 24.86,
                            "dealt_to_champions": 9185,
                            "dealt_to_champions_percentage": 19.02,
                            "taken": 8080
                          },
                          "masteries": [],
                          "minions_killed": 246,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 38804,
                            "dealt_percentage": 12.24,
                            "dealt_to_champions": 1471,
                            "dealt_to_champions_percentage": 7.78,
                            "taken": 12747
                          },
                          "player": {
                            "active": true,
                            "age": 21,
                            "birthday": "2004-01-31",
                            "first_name": "Choi",
                            "id": 31391,
                            "image_url": "https://cdn.pandascore.co/images/player/image/31391/t1_zeus_2023_split_2.png",
                            "last_name": "Woo-je",
                            "modified_at": "2026-01-06T07:15:50Z",
                            "name": "Zeus",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "zeus-choi-woo-je"
                          },
                          "player_id": 31391,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 29,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/58955cb861c3b51375948a05e260996a.png",
                              "name": "Ghost"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 161182,
                            "dealt_percentage": 24.23,
                            "dealt_to_champions": 15934,
                            "dealt_to_champions_percentage": 21.26,
                            "taken": 21078
                          },
                          "total_heal": 3074,
                          "total_time_crowd_control_dealt": 65,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 57066,
                            "dealt_percentage": 66.93,
                            "dealt_to_champions": 5278,
                            "dealt_to_champions_percentage": 68.04,
                            "taken": 251
                          },
                          "wards": {
                            "placed": 10,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 6
                          },
                          "wards_placed": 10
                        },
                        {
                          "assists": 3,
                          "champion": {
                            "id": 3127,
                            "image_url": "https://cdn.pandascore.co/images/lol/champion/image/f9ba83de2c8b43d1c5e4778f50595c6b.png",
                            "name": "Xin Zhao",
                            "slug": "XinZhao"
                          },
                          "creep_score": 172,
                          "cs_at_14": 91,
                          "cs_diff_at_14": 7,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": true,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 235717,
                          "gold_earned": 9608,
                          "gold_percentage": 17.48,
                          "gold_spent": 9325,
                          "items": [
                            {
                              "id": 2450,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/5ff4236356a2fc30dd646724b53a5354.png",
                              "is_trinket": false,
                              "name": "Cloth Armor"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2481,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/84b0db5c9726c8bd47c9c8c088f6e8fb.png",
                              "is_trinket": false,
                              "name": "Broken Stopwatch"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2926,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/9e7450aaa9bd2694e330a2d84b974eba.png",
                              "is_trinket": false,
                              "name": "Sterak's Gage"
                            },
                            {
                              "id": 2935,
                              "image_url": "https://cdn.pandascore.co/images/lol/item/image/97032f4cae42f011b132d0bca2438e8b.png",
                              "is_trinket": false,
                              "name": "Goredrinker"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 150,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 3,
                            "wards": 20
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 13,
                          "magic_damage": {
                            "dealt": 14386,
                            "dealt_percentage": 5.48,
                            "dealt_to_champions": 508,
                            "dealt_to_champions_percentage": 1.05,
                            "taken": 5464
                          },
                          "masteries": [],
                          "minions_killed": 172,
                          "opponent": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "physical_damage": {
                            "dealt": 108902,
                            "dealt_percentage": 34.34,
                            "dealt_to_champions": 5392,
                            "dealt_to_champions_percentage": 28.51,
                            "taken": 16036
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-12-24",
                            "first_name": "Moon",
                            "id": 31392,
                            "image_url": "https://cdn.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                            "last_name": "Hyeon-joon",
                            "modified_at": "2026-01-06T07:15:55Z",
                            "name": "Oner",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "oner"
                          },
                          "player_id": 31392,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": null,
                            "secondary_path": null,
                            "shards": {
                              "defense": null,
                              "flex": null,
                              "offense": null
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 140116,
                            "dealt_percentage": 21.07,
                            "dealt_to_champions": 6172,
                            "dealt_to_champions_percentage": 8.23,
                            "taken": 21629
                          },
                          "total_heal": 11106,
                          "total_time_crowd_control_dealt": 459,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 16827,
                            "dealt_percentage": 19.73,
                            "dealt_to_champions": 272,
                            "dealt_to_champions_percentage": 3.51,
                            "taken": 128
                          },
                          "wards": {
                            "placed": 9,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 9
                          },
                          "wards_placed": 9
                        }
                      ],
                      "position": 1,
                      "status": "finished",
                      "teams": [
                        {
                          "atakhan_kills": null,
                          "bans": [
                            2981,
                            2982,
                            3110,
                            3013,
                            3061
                          ],
                          "baron_kills": 1,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 1,
                          "color": "blue",
                          "dragon_kills": 3,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": true,
                          "first_blood": true,
                          "first_dragon": true,
                          "first_herald": false,
                          "first_inhibitor": true,
                          "first_tower": true,
                          "first_voidgrub": null,
                          "gold_earned": 54952,
                          "herald_kills": 1,
                          "hextech_drake_kills": 1,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 2,
                          "kills": 10,
                          "mountain_drake_kills": 1,
                          "ocean_drake_kills": 0,
                          "player_ids": [
                            585,
                            8158,
                            19285,
                            31391,
                            31392
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-01-06T07:15:56Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "tower_kills": 10,
                          "voidgrub_kills": null
                        },
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3142,
                            3000,
                            3108,
                            3134,
                            3056
                          ],
                          "baron_kills": 0,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 0,
                          "color": "red",
                          "dragon_kills": 0,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": false,
                          "first_blood": false,
                          "first_dragon": false,
                          "first_herald": true,
                          "first_inhibitor": false,
                          "first_tower": false,
                          "first_voidgrub": null,
                          "gold_earned": 43593,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 0,
                          "kills": 8,
                          "mountain_drake_kills": 0,
                          "ocean_drake_kills": 0,
                          "player_ids": [
                            1456,
                            3524,
                            8142,
                            8924,
                            19283
                          ],
                          "team": {
                            "acronym": "KDF",
                            "dark_mode_image_url": null,
                            "id": 130063,
                            "image_url": "https://cdn.pandascore.co/images/team/image/130063/kwangdong_freecslogo_square.png",
                            "location": "KR",
                            "modified_at": "2024-12-29T11:45:20Z",
                            "name": "Kwangdong Freecs",
                            "slug": "kwangdong-freecs"
                          },
                          "tower_kills": 0,
                          "voidgrub_kills": null
                        }
                      ],
                      "winner": {
                        "id": 126061,
                        "type": "Team"
                      },
                      "winner_type": "Team"
                    }
                  ],
                  "location": "KR",
                  "modified_at": "2026-01-06T07:15:56Z",
                  "most_banned": [
                    {
                      "count": 23,
                      "name": "Akali",
                      "slug": "Akali"
                    },
                    {
                      "count": 22,
                      "name": "Zeri",
                      "slug": "Zeri"
                    },
                    {
                      "count": 19,
                      "name": "Twisted Fate",
                      "slug": "TwistedFate"
                    },
                    {
                      "count": 18,
                      "name": "Lucian",
                      "slug": "Lucian"
                    },
                    {
                      "count": 17,
                      "name": "Nautilus",
                      "slug": "Nautilus"
                    },
                    {
                      "count": 15,
                      "name": "Rakan",
                      "slug": "Rakan"
                    },
                    {
                      "count": 14,
                      "name": "Ryze",
                      "slug": "Ryze"
                    },
                    {
                      "count": 13,
                      "name": "Ahri",
                      "slug": "Ahri"
                    },
                    {
                      "count": 13,
                      "name": "Wukong",
                      "slug": "MonkeyKing"
                    },
                    {
                      "count": 11,
                      "name": "Renekton",
                      "slug": "Renekton"
                    },
                    {
                      "count": 10,
                      "name": "Hecarim",
                      "slug": "Hecarim"
                    },
                    {
                      "count": 8,
                      "name": "Corki",
                      "slug": "Corki"
                    },
                    {
                      "count": 8,
                      "name": "Ezreal",
                      "slug": "Ezreal"
                    },
                    {
                      "count": 8,
                      "name": "Leona",
                      "slug": "Leona"
                    },
                    {
                      "count": 8,
                      "name": "Tryndamere",
                      "slug": "Tryndamere"
                    },
                    {
                      "count": 8,
                      "name": "Xin Zhao",
                      "slug": "XinZhao"
                    },
                    {
                      "count": 7,
                      "name": "Aphelios",
                      "slug": "Aphelios"
                    },
                    {
                      "count": 7,
                      "name": "Gwen",
                      "slug": "Gwen"
                    },
                    {
                      "count": 7,
                      "name": "Jayce",
                      "slug": "Jayce"
                    },
                    {
                      "count": 7,
                      "name": "LeBlanc",
                      "slug": "Leblanc"
                    },
                    {
                      "count": 7,
                      "name": "Ornn",
                      "slug": "Ornn"
                    },
                    {
                      "count": 6,
                      "name": "Galio",
                      "slug": "Galio"
                    },
                    {
                      "count": 6,
                      "name": "Gragas",
                      "slug": "Gragas"
                    },
                    {
                      "count": 6,
                      "name": "Kai'Sa",
                      "slug": "Kaisa"
                    },
                    {
                      "count": 6,
                      "name": "Karma",
                      "slug": "Karma"
                    },
                    {
                      "count": 6,
                      "name": "Volibear",
                      "slug": "Volibear"
                    },
                    {
                      "count": 6,
                      "name": "Yuumi",
                      "slug": "Yuumi"
                    },
                    {
                      "count": 5,
                      "name": "Graves",
                      "slug": "Graves"
                    },
                    {
                      "count": 5,
                      "name": "Kayle",
                      "slug": "Kayle"
                    },
                    {
                      "count": 5,
                      "name": "Lee Sin",
                      "slug": "LeeSin"
                    },
                    {
                      "count": 5,
                      "name": "Nocturne",
                      "slug": "Nocturne"
                    },
                    {
                      "count": 5,
                      "name": "Poppy",
                      "slug": "Poppy"
                    },
                    {
                      "count": 5,
                      "name": "Vex",
                      "slug": "Vex"
                    },
                    {
                      "count": 4,
                      "name": "Gangplank",
                      "slug": "Gangplank"
                    },
                    {
                      "count": 4,
                      "name": "Jarvan IV",
                      "slug": "JarvanIV"
                    },
                    {
                      "count": 4,
                      "name": "Jax",
                      "slug": "Jax"
                    },
                    {
                      "count": 4,
                      "name": "Jinx",
                      "slug": "Jinx"
                    },
                    {
                      "count": 4,
                      "name": "Malphite",
                      "slug": "Malphite"
                    },
                    {
                      "count": 4,
                      "name": "Renata Glasc",
                      "slug": "Renata"
                    },
                    {
                      "count": 4,
                      "name": "Senna",
                      "slug": "Senna"
                    },
                    {
                      "count": 4,
                      "name": "Taliyah",
                      "slug": "Taliyah"
                    },
                    {
                      "count": 4,
                      "name": "Viego",
                      "slug": "Viego"
                    },
                    {
                      "count": 3,
                      "name": "Diana",
                      "slug": "Diana"
                    },
                    {
                      "count": 3,
                      "name": "Gnar",
                      "slug": "Gnar"
                    },
                    {
                      "count": 3,
                      "name": "Irelia",
                      "slug": "Irelia"
                    },
                    {
                      "count": 3,
                      "name": "Kalista",
                      "slug": "Kalista"
                    },
                    {
                      "count": 3,
                      "name": "Sylas",
                      "slug": "Sylas"
                    },
                    {
                      "count": 3,
                      "name": "Syndra",
                      "slug": "Syndra"
                    },
                    {
                      "count": 3,
                      "name": "Tahm Kench",
                      "slug": "TahmKench"
                    },
                    {
                      "count": 3,
                      "name": "Tristana",
                      "slug": "Tristana"
                    },
                    {
                      "count": 3,
                      "name": "Viktor",
                      "slug": "Viktor"
                    },
                    {
                      "count": 3,
                      "name": "Xayah",
                      "slug": "Xayah"
                    },
                    {
                      "count": 3,
                      "name": "Yone",
                      "slug": "Yone"
                    },
                    {
                      "count": 3,
                      "name": "Zoe",
                      "slug": "Zoe"
                    },
                    {
                      "count": 2,
                      "name": "Akshan",
                      "slug": "Akshan"
                    },
                    {
                      "count": 2,
                      "name": "Azir",
                      "slug": "Azir"
                    },
                    {
                      "count": 2,
                      "name": "Caitlyn",
                      "slug": "Caitlyn"
                    },
                    {
                      "count": 2,
                      "name": "Kennen",
                      "slug": "Kennen"
                    },
                    {
                      "count": 2,
                      "name": "Urgot",
                      "slug": "Urgot"
                    },
                    {
                      "count": 2,
                      "name": "Yasuo",
                      "slug": "Yasuo"
                    },
                    {
                      "count": 1,
                      "name": "Aatrox",
                      "slug": "Aatrox"
                    },
                    {
                      "count": 1,
                      "name": "Alistar",
                      "slug": "Alistar"
                    },
                    {
                      "count": 1,
                      "name": "Amumu",
                      "slug": "Amumu"
                    },
                    {
                      "count": 1,
                      "name": "Camille",
                      "slug": "Camille"
                    },
                    {
                      "count": 1,
                      "name": "Janna",
                      "slug": "Janna"
                    },
                    {
                      "count": 1,
                      "name": "Jhin",
                      "slug": "Jhin"
                    },
                    {
                      "count": 1,
                      "name": "Nidalee",
                      "slug": "Nidalee"
                    },
                    {
                      "count": 1,
                      "name": "Olaf",
                      "slug": "Olaf"
                    },
                    {
                      "count": 1,
                      "name": "Orianna",
                      "slug": "Orianna"
                    },
                    {
                      "count": 1,
                      "name": "Rell",
                      "slug": "Rell"
                    },
                    {
                      "count": 1,
                      "name": "Sejuani",
                      "slug": "Sejuani"
                    },
                    {
                      "count": 1,
                      "name": "Swain",
                      "slug": "Swain"
                    },
                    {
                      "count": 1,
                      "name": "Thresh",
                      "slug": "Thresh"
                    },
                    {
                      "count": 1,
                      "name": "Vi",
                      "slug": "Vi"
                    },
                    {
                      "count": 1,
                      "name": "Ziggs",
                      "slug": "Ziggs"
                    }
                  ],
                  "most_banned_against": [
                    {
                      "count": 42,
                      "name": "Caitlyn",
                      "slug": "Caitlyn"
                    },
                    {
                      "count": 32,
                      "name": "Twisted Fate",
                      "slug": "TwistedFate"
                    },
                    {
                      "count": 21,
                      "name": "Karma",
                      "slug": "Karma"
                    },
                    {
                      "count": 21,
                      "name": "LeBlanc",
                      "slug": "Leblanc"
                    },
                    {
                      "count": 20,
                      "name": "Jayce",
                      "slug": "Jayce"
                    },
                    {
                      "count": 18,
                      "name": "Lucian",
                      "slug": "Lucian"
                    },
                    {
                      "count": 17,
                      "name": "Zeri",
                      "slug": "Zeri"
                    },
                    {
                      "count": 13,
                      "name": "Corki",
                      "slug": "Corki"
                    },
                    {
                      "count": 13,
                      "name": "Gangplank",
                      "slug": "Gangplank"
                    },
                    {
                      "count": 12,
                      "name": "Tahm Kench",
                      "slug": "TahmKench"
                    },
                    {
                      "count": 10,
                      "name": "Renata Glasc",
                      "slug": "Renata"
                    },
                    {
                      "count": 9,
                      "name": "Ahri",
                      "slug": "Ahri"
                    },
                    {
                      "count": 9,
                      "name": "Gwen",
                      "slug": "Gwen"
                    },
                    {
                      "count": 9,
                      "name": "Lee Sin",
                      "slug": "LeeSin"
                    },
                    {
                      "count": 8,
                      "name": "Kalista",
                      "slug": "Kalista"
                    },
                    {
                      "count": 8,
                      "name": "Senna",
                      "slug": "Senna"
                    },
                    {
                      "count": 8,
                      "name": "Thresh",
                      "slug": "Thresh"
                    },
                    {
                      "count": 8,
                      "name": "Tryndamere",
                      "slug": "Tryndamere"
                    },
                    {
                      "count": 8,
                      "name": "Wukong",
                      "slug": "MonkeyKing"
                    },
                    {
                      "count": 7,
                      "name": "Viego",
                      "slug": "Viego"
                    },
                    {
                      "count": 7,
                      "name": "Xayah",
                      "slug": "Xayah"
                    },
                    {
                      "count": 6,
                      "name": "Aphelios",
                      "slug": "Aphelios"
                    },
                    {
                      "count": 6,
                      "name": "Azir",
                      "slug": "Azir"
                    },
                    {
                      "count": 6,
                      "name": "Hecarim",
                      "slug": "Hecarim"
                    },
                    {
                      "count": 6,
                      "name": "Jinx",
                      "slug": "Jinx"
                    },
                    {
                      "count": 6,
                      "name": "Nautilus",
                      "slug": "Nautilus"
                    },
                    {
                      "count": 5,
                      "name": "Kai'Sa",
                      "slug": "Kaisa"
                    },
                    {
                      "count": 5,
                      "name": "Ryze",
                      "slug": "Ryze"
                    },
                    {
                      "count": 4,
                      "name": "Ezreal",
                      "slug": "Ezreal"
                    },
                    {
                      "count": 4,
                      "name": "Graves",
                      "slug": "Graves"
                    },
                    {
                      "count": 4,
                      "name": "Poppy",
                      "slug": "Poppy"
                    },
                    {
                      "count": 4,
                      "name": "Yuumi",
                      "slug": "Yuumi"
                    },
                    {
                      "count": 3,
                      "name": "Gnar",
                      "slug": "Gnar"
                    },
                    {
                      "count": 3,
                      "name": "Gragas",
                      "slug": "Gragas"
                    },
                    {
                      "count": 3,
                      "name": "Jarvan IV",
                      "slug": "JarvanIV"
                    },
                    {
                      "count": 3,
                      "name": "Jax",
                      "slug": "Jax"
                    },
                    {
                      "count": 3,
                      "name": "Jhin",
                      "slug": "Jhin"
                    },
                    {
                      "count": 3,
                      "name": "Kennen",
                      "slug": "Kennen"
                    },
                    {
                      "count": 3,
                      "name": "Renekton",
                      "slug": "Renekton"
                    },
                    {
                      "count": 3,
                      "name": "Vex",
                      "slug": "Vex"
                    },
                    {
                      "count": 3,
                      "name": "Vi",
                      "slug": "Vi"
                    },
                    {
                      "count": 3,
                      "name": "Xin Zhao",
                      "slug": "XinZhao"
                    },
                    {
                      "count": 2,
                      "name": "Alistar",
                      "slug": "Alistar"
                    },
                    {
                      "count": 2,
                      "name": "Miss Fortune",
                      "slug": "MissFortune"
                    },
                    {
                      "count": 2,
                      "name": "Nocturne",
                      "slug": "Nocturne"
                    },
                    {
                      "count": 2,
                      "name": "Rakan",
                      "slug": "Rakan"
                    },
                    {
                      "count": 2,
                      "name": "Sylas",
                      "slug": "Sylas"
                    },
                    {
                      "count": 2,
                      "name": "Trundle",
                      "slug": "Trundle"
                    },
                    {
                      "count": 2,
                      "name": "Zoe",
                      "slug": "Zoe"
                    },
                    {
                      "count": 1,
                      "name": "Akali",
                      "slug": "Akali"
                    },
                    {
                      "count": 1,
                      "name": "Amumu",
                      "slug": "Amumu"
                    },
                    {
                      "count": 1,
                      "name": "Braum",
                      "slug": "Braum"
                    },
                    {
                      "count": 1,
                      "name": "Draven",
                      "slug": "Draven"
                    },
                    {
                      "count": 1,
                      "name": "Leona",
                      "slug": "Leona"
                    },
                    {
                      "count": 1,
                      "name": "Neeko",
                      "slug": "Neeko"
                    },
                    {
                      "count": 1,
                      "name": "Pyke",
                      "slug": "Pyke"
                    },
                    {
                      "count": 1,
                      "name": "Swain",
                      "slug": "Swain"
                    },
                    {
                      "count": 1,
                      "name": "Tristana",
                      "slug": "Tristana"
                    },
                    {
                      "count": 1,
                      "name": "Varus",
                      "slug": "Varus"
                    },
                    {
                      "count": 1,
                      "name": "Viktor",
                      "slug": "Viktor"
                    },
                    {
                      "count": 1,
                      "name": "Vladimir",
                      "slug": "Vladimir"
                    },
                    {
                      "count": 1,
                      "name": "Yone",
                      "slug": "Yone"
                    },
                    {
                      "count": 1,
                      "name": "Ziggs",
                      "slug": "Ziggs"
                    },
                    {
                      "count": 1,
                      "name": "Zilean",
                      "slug": "Zilean"
                    }
                  ],
                  "most_picked": [
                    {
                      "count": 25,
                      "games_lost": 3,
                      "games_won": 22,
                      "name": "Lee Sin",
                      "slug": "LeeSin"
                    },
                    {
                      "count": 23,
                      "games_lost": 6,
                      "games_won": 17,
                      "name": "Jinx",
                      "slug": "Jinx"
                    },
                    {
                      "count": 21,
                      "games_lost": 5,
                      "games_won": 16,
                      "name": "Jayce",
                      "slug": "Jayce"
                    },
                    {
                      "count": 16,
                      "games_lost": 3,
                      "games_won": 13,
                      "name": "Ahri",
                      "slug": "Ahri"
                    },
                    {
                      "count": 16,
                      "games_lost": 5,
                      "games_won": 11,
                      "name": "Gwen",
                      "slug": "Gwen"
                    },
                    {
                      "count": 16,
                      "games_lost": 2,
                      "games_won": 14,
                      "name": "Nautilus",
                      "slug": "Nautilus"
                    },
                    {
                      "count": 16,
                      "games_lost": 1,
                      "games_won": 15,
                      "name": "Viego",
                      "slug": "Viego"
                    },
                    {
                      "count": 14,
                      "games_lost": 2,
                      "games_won": 12,
                      "name": "Tahm Kench",
                      "slug": "TahmKench"
                    },
                    {
                      "count": 13,
                      "games_lost": 0,
                      "games_won": 13,
                      "name": "LeBlanc",
                      "slug": "Leblanc"
                    },
                    {
                      "count": 12,
                      "games_lost": 2,
                      "games_won": 10,
                      "name": "Xin Zhao",
                      "slug": "XinZhao"
                    },
                    {
                      "count": 11,
                      "games_lost": 2,
                      "games_won": 9,
                      "name": "Aphelios",
                      "slug": "Aphelios"
                    },
                    {
                      "count": 10,
                      "games_lost": 3,
                      "games_won": 7,
                      "name": "Wukong",
                      "slug": "MonkeyKing"
                    },
                    {
                      "count": 10,
                      "games_lost": 0,
                      "games_won": 10,
                      "name": "Xayah",
                      "slug": "Xayah"
                    },
                    {
                      "count": 9,
                      "games_lost": 1,
                      "games_won": 8,
                      "name": "Gnar",
                      "slug": "Gnar"
                    },
                    {
                      "count": 8,
                      "games_lost": 0,
                      "games_won": 8,
                      "name": "Corki",
                      "slug": "Corki"
                    },
                    {
                      "count": 8,
                      "games_lost": 1,
                      "games_won": 7,
                      "name": "Gangplank",
                      "slug": "Gangplank"
                    },
                    {
                      "count": 8,
                      "games_lost": 0,
                      "games_won": 8,
                      "name": "Gragas",
                      "slug": "Gragas"
                    },
                    {
                      "count": 8,
                      "games_lost": 0,
                      "games_won": 8,
                      "name": "Thresh",
                      "slug": "Thresh"
                    },
                    {
                      "count": 7,
                      "games_lost": 2,
                      "games_won": 5,
                      "name": "Azir",
                      "slug": "Azir"
                    },
                    {
                      "count": 7,
                      "games_lost": 3,
                      "games_won": 4,
                      "name": "Kalista",
                      "slug": "Kalista"
                    },
                    {
                      "count": 7,
                      "games_lost": 2,
                      "games_won": 5,
                      "name": "Kennen",
                      "slug": "Kennen"
                    },
                    {
                      "count": 6,
                      "games_lost": 1,
                      "games_won": 5,
                      "name": "Caitlyn",
                      "slug": "Caitlyn"
                    },
                    {
                      "count": 6,
                      "games_lost": 1,
                      "games_won": 5,
                      "name": "Renata Glasc",
                      "slug": "Renata"
                    },
                    {
                      "count": 6,
                      "games_lost": 0,
                      "games_won": 6,
                      "name": "Senna",
                      "slug": "Senna"
                    },
                    {
                      "count": 5,
                      "games_lost": 1,
                      "games_won": 4,
                      "name": "Camille",
                      "slug": "Camille"
                    },
                    {
                      "count": 5,
                      "games_lost": 1,
                      "games_won": 4,
                      "name": "Ezreal",
                      "slug": "Ezreal"
                    },
                    {
                      "count": 5,
                      "games_lost": 3,
                      "games_won": 2,
                      "name": "Ryze",
                      "slug": "Ryze"
                    },
                    {
                      "count": 5,
                      "games_lost": 2,
                      "games_won": 3,
                      "name": "Zoe",
                      "slug": "Zoe"
                    },
                    {
                      "count": 4,
                      "games_lost": 2,
                      "games_won": 2,
                      "name": "Diana",
                      "slug": "Diana"
                    },
                    {
                      "count": 4,
                      "games_lost": 0,
                      "games_won": 4,
                      "name": "Graves",
                      "slug": "Graves"
                    },
                    {
                      "count": 4,
                      "games_lost": 1,
                      "games_won": 3,
                      "name": "Hecarim",
                      "slug": "Hecarim"
                    },
                    {
                      "count": 4,
                      "games_lost": 2,
                      "games_won": 2,
                      "name": "Jhin",
                      "slug": "Jhin"
                    },
                    {
                      "count": 4,
                      "games_lost": 1,
                      "games_won": 3,
                      "name": "Twisted Fate",
                      "slug": "TwistedFate"
                    },
                    {
                      "count": 4,
                      "games_lost": 0,
                      "games_won": 4,
                      "name": "Vex",
                      "slug": "Vex"
                    },
                    {
                      "count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Galio",
                      "slug": "Galio"
                    },
                    {
                      "count": 3,
                      "games_lost": 0,
                      "games_won": 3,
                      "name": "Irelia",
                      "slug": "Irelia"
                    },
                    {
                      "count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Kai'Sa",
                      "slug": "Kaisa"
                    },
                    {
                      "count": 3,
                      "games_lost": 2,
                      "games_won": 1,
                      "name": "Karma",
                      "slug": "Karma"
                    },
                    {
                      "count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Lissandra",
                      "slug": "Lissandra"
                    },
                    {
                      "count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Lucian",
                      "slug": "Lucian"
                    },
                    {
                      "count": 3,
                      "games_lost": 0,
                      "games_won": 3,
                      "name": "Lux",
                      "slug": "Lux"
                    },
                    {
                      "count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Nocturne",
                      "slug": "Nocturne"
                    },
                    {
                      "count": 3,
                      "games_lost": 0,
                      "games_won": 3,
                      "name": "Pyke",
                      "slug": "Pyke"
                    },
                    {
                      "count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Tryndamere",
                      "slug": "Tryndamere"
                    },
                    {
                      "count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Viktor",
                      "slug": "Viktor"
                    },
                    {
                      "count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Yuumi",
                      "slug": "Yuumi"
                    },
                    {
                      "count": 3,
                      "games_lost": 0,
                      "games_won": 3,
                      "name": "Zeri",
                      "slug": "Zeri"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Akali",
                      "slug": "Akali"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Bard",
                      "slug": "Bard"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Braum",
                      "slug": "Braum"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Fiora",
                      "slug": "Fiora"
                    },
                    {
                      "count": 2,
                      "games_lost": 2,
                      "games_won": 0,
                      "name": "Jarvan IV",
                      "slug": "JarvanIV"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Jax",
                      "slug": "Jax"
                    },
                    {
                      "count": 2,
                      "games_lost": 2,
                      "games_won": 0,
                      "name": "Leona",
                      "slug": "Leona"
                    },
                    {
                      "count": 2,
                      "games_lost": 1,
                      "games_won": 1,
                      "name": "Lulu",
                      "slug": "Lulu"
                    },
                    {
                      "count": 2,
                      "games_lost": 1,
                      "games_won": 1,
                      "name": "Morgana",
                      "slug": "Morgana"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Nami",
                      "slug": "Nami"
                    },
                    {
                      "count": 2,
                      "games_lost": 1,
                      "games_won": 1,
                      "name": "Poppy",
                      "slug": "Poppy"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Rumble",
                      "slug": "Rumble"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Samira",
                      "slug": "Samira"
                    },
                    {
                      "count": 2,
                      "games_lost": 1,
                      "games_won": 1,
                      "name": "Seraphine",
                      "slug": "Seraphine"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Swain",
                      "slug": "Swain"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Sylas",
                      "slug": "Sylas"
                    },
                    {
                      "count": 2,
                      "games_lost": 1,
                      "games_won": 1,
                      "name": "Tristana",
                      "slug": "Tristana"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Vi",
                      "slug": "Vi"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Alistar",
                      "slug": "Alistar"
                    },
                    {
                      "count": 1,
                      "games_lost": 1,
                      "games_won": 0,
                      "name": "Kassadin",
                      "slug": "Kassadin"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Kindred",
                      "slug": "Kindred"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Rakan",
                      "slug": "Rakan"
                    },
                    {
                      "count": 1,
                      "games_lost": 1,
                      "games_won": 0,
                      "name": "Rell",
                      "slug": "Rell"
                    },
                    {
                      "count": 1,
                      "games_lost": 1,
                      "games_won": 0,
                      "name": "Taric",
                      "slug": "Taric"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Varus",
                      "slug": "Varus"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Vayne",
                      "slug": "Vayne"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Veigar",
                      "slug": "Veigar"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Yasuo",
                      "slug": "Yasuo"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Yone",
                      "slug": "Yone"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Zac",
                      "slug": "Zac"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Zilean",
                      "slug": "Zilean"
                    }
                  ],
                  "name": "T1",
                  "players": [
                    {
                      "active": true,
                      "age": 29,
                      "birthday": "1996-05-07",
                      "first_name": "Lee",
                      "id": 585,
                      "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                      "last_name": "Sang-hyeok",
                      "modified_at": "2026-01-06T07:15:55Z",
                      "name": "Faker",
                      "nationality": "KR",
                      "role": "mid",
                      "slug": "faker"
                    },
                    {
                      "active": true,
                      "age": 23,
                      "birthday": "2002-10-14",
                      "first_name": "Ryu",
                      "id": 8158,
                      "image_url": "https://cdn.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                      "last_name": "Min-seok",
                      "modified_at": "2026-01-06T07:15:55Z",
                      "name": "Keria",
                      "nationality": "KR",
                      "role": "sup",
                      "slug": "keria"
                    },
                    {
                      "active": true,
                      "age": 25,
                      "birthday": "2000-07-22",
                      "first_name": "Choi",
                      "id": 19282,
                      "image_url": "https://cdn.pandascore.co/images/player/image/19282/gen_doran_2023_split_2.png",
                      "last_name": "Hyeon-joon",
                      "modified_at": "2026-01-06T07:15:55Z",
                      "name": "Doran",
                      "nationality": "KR",
                      "role": "top",
                      "slug": "doran-2686e2c9-bd34-47fb-9d17-87debb7be1b6"
                    },
                    {
                      "active": true,
                      "age": 23,
                      "birthday": "2002-12-24",
                      "first_name": "Moon",
                      "id": 31392,
                      "image_url": "https://cdn.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                      "last_name": "Hyeon-joon",
                      "modified_at": "2026-01-06T07:15:55Z",
                      "name": "Oner",
                      "nationality": "KR",
                      "role": "jun",
                      "slug": "oner"
                    },
                    {
                      "active": true,
                      "age": 20,
                      "birthday": "2005-12-05",
                      "first_name": "Kim",
                      "id": 38351,
                      "image_url": "https://cdn.pandascore.co/images/player/image/38351/jdg_peyz_2025_split_1.png",
                      "last_name": "Su-hwan",
                      "modified_at": "2026-01-06T07:15:56Z",
                      "name": "Peyz",
                      "nationality": "KR",
                      "role": "adc",
                      "slug": "peyz"
                    }
                  ],
                  "slug": "t1",
                  "stats": [
                    {
                      "averages": {
                        "assists": 30.71,
                        "atakhan_kills": null,
                        "baron_kills": 1.21,
                        "deaths": 10.64,
                        "dragon_kills": 2.36,
                        "game_length": 2025,
                        "gold_earned": 64631,
                        "herald_kill": 0.93,
                        "inhibitor_kills": 1.29,
                        "kills": 13,
                        "ratios": {
                          "first_atakhan": null,
                          "first_baron": 0.57,
                          "first_blood": 0.43,
                          "first_dragon": 0.5,
                          "first_herald": 0.5,
                          "first_inhibitor": 0.71,
                          "first_tower": 0.79,
                          "first_voidgrub": null,
                          "win": 0.79
                        },
                        "total_minions_killed": 1155.79,
                        "tower_kills": 7.93,
                        "voidgrub_kills": null,
                        "wards_placed": 123.36
                      },
                      "games_count": 14,
                      "serie": {
                        "begin_at": "2022-06-15T07:00:00Z",
                        "end_at": "2022-08-28T09:17:00Z",
                        "full_name": "Summer 2022",
                        "id": 4763,
                        "league": {
                          "id": 293,
                          "image_url": "https://cdn.pandascore.co/images/league/image/293/lck_2021_logo-png",
                          "modified_at": "2021-01-06T15:41:48Z",
                          "name": "LCK",
                          "slug": "league-of-legends-lck-champions-korea",
                          "url": null
                        },
                        "league_id": 293,
                        "modified_at": "2022-08-28T18:54:39Z",
                        "name": null,
                        "season": "Summer",
                        "slug": "league-of-legends-lck-champions-korea-summer-2022",
                        "tournaments": [
                          {
                            "begin_at": "2022-06-15T08:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-08-14T11:02:00Z",
                            "has_bracket": false,
                            "id": 8281,
                            "league_id": 293,
                            "live_supported": true,
                            "modified_at": "2022-08-28T18:54:39Z",
                            "name": "Regular Season",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4763,
                            "slug": "league-of-legends-lck-champions-korea-summer-2022-regular-season",
                            "tier": "a",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-08-17T08:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-08-28T09:17:00Z",
                            "has_bracket": true,
                            "id": 8592,
                            "league_id": 293,
                            "live_supported": true,
                            "modified_at": "2023-04-25T16:38:01Z",
                            "name": "Playoffs",
                            "prizepool": "375000000 South Korean Won",
                            "region": null,
                            "serie_id": 4763,
                            "slug": "league-of-legends-lck-champions-korea-summer-2022-playoffs",
                            "tier": "a",
                            "type": null,
                            "winner_id": 2882,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-09-01T08:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-09-03T12:24:00Z",
                            "has_bracket": true,
                            "id": 8812,
                            "league_id": 293,
                            "live_supported": true,
                            "modified_at": "2022-09-03T19:51:47Z",
                            "name": "Regional Finals",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4763,
                            "slug": "league-of-legends-lck-champions-korea-summer-2022-regional-finals",
                            "tier": "a",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          }
                        ],
                        "videogame": {
                          "id": 1,
                          "name": "LoL",
                          "slug": "league-of-legends"
                        },
                        "videogame_title": null,
                        "winner_id": 2882,
                        "winner_type": "Team",
                        "year": 2022
                      },
                      "totals": {
                        "assists": 430,
                        "atakhan_kills": null,
                        "baron_kills": 17,
                        "blue_games_lost": 2,
                        "blue_games_won": 6,
                        "chemtech_drake_kills": 0,
                        "cloud_drake_kills": 9,
                        "deaths": 149,
                        "dragon_kills": 33,
                        "elder_drake_kills": 1,
                        "games_lost": 3,
                        "games_played": 14,
                        "games_won": 11,
                        "herald_kill": 13,
                        "hextech_drake_kills": 7,
                        "infernal_drake_kills": 5,
                        "inhibitor_kills": 18,
                        "kills": 182,
                        "matches_lost": 1,
                        "matches_played": 6,
                        "matches_won": 5,
                        "mountain_drake_kills": 9,
                        "ocean_drake_kills": 2,
                        "red_games_lost": 1,
                        "red_games_won": 5,
                        "tower_kills": 111,
                        "voidgrub_kills": null,
                        "wards_placed": 1727
                      }
                    },
                    {
                      "averages": {
                        "assists": 31.04,
                        "atakhan_kills": null,
                        "baron_kills": 0.67,
                        "deaths": 10.83,
                        "dragon_kills": 1.92,
                        "game_length": 1641,
                        "gold_earned": 54169.83,
                        "herald_kill": 1.5,
                        "inhibitor_kills": 1.13,
                        "kills": 15.5,
                        "ratios": {
                          "first_atakhan": null,
                          "first_baron": 0.63,
                          "first_blood": 0.54,
                          "first_dragon": 0.38,
                          "first_herald": 0.75,
                          "first_inhibitor": 0.75,
                          "first_tower": 0.88,
                          "first_voidgrub": null,
                          "win": 0.75
                        },
                        "total_minions_killed": 923.13,
                        "tower_kills": 8.13,
                        "voidgrub_kills": null,
                        "wards_placed": 98.21
                      },
                      "games_count": 24,
                      "serie": {
                        "begin_at": "2022-05-09T22:00:00Z",
                        "end_at": "2022-05-29T12:26:00Z",
                        "full_name": "2022",
                        "id": 4534,
                        "league": {
                          "id": 300,
                          "image_url": "https://cdn.pandascore.co/images/league/image/300/900px-msi_2021_lightmode-png",
                          "modified_at": "2019-06-13T11:53:14Z",
                          "name": "Mid-Season Invitational",
                          "slug": "league-of-legends-mid-invitational",
                          "url": null
                        },
                        "league_id": 300,
                        "modified_at": "2022-05-29T17:10:35Z",
                        "name": null,
                        "season": null,
                        "slug": "league-of-legends-mid-invitational-2022",
                        "tournaments": [
                          {
                            "begin_at": "2022-05-09T22:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-05-15T11:00:00Z",
                            "has_bracket": false,
                            "id": 7998,
                            "league_id": 300,
                            "live_supported": true,
                            "modified_at": "2022-05-29T17:10:35Z",
                            "name": "Group A",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4534,
                            "slug": "league-of-legends-mid-invitational-2022-group-a",
                            "tier": "s",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-05-09T22:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-05-14T14:30:00Z",
                            "has_bracket": false,
                            "id": 7999,
                            "league_id": 300,
                            "live_supported": true,
                            "modified_at": "2022-05-29T17:10:35Z",
                            "name": "Group B",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4534,
                            "slug": "league-of-legends-mid-invitational-2022-group-b",
                            "tier": "s",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-05-09T22:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-05-14T11:35:00Z",
                            "has_bracket": false,
                            "id": 8000,
                            "league_id": 300,
                            "live_supported": true,
                            "modified_at": "2022-05-29T17:10:35Z",
                            "name": "Group C",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4534,
                            "slug": "league-of-legends-mid-invitational-2022-group-c",
                            "tier": "s",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-05-19T22:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-05-29T13:00:00Z",
                            "has_bracket": false,
                            "id": 8001,
                            "league_id": 300,
                            "live_supported": true,
                            "modified_at": "2022-05-29T17:10:35Z",
                            "name": "Rumble Stage",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4534,
                            "slug": "league-of-legends-mid-invitational-2022-rumble-stage",
                            "tier": "s",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-05-26T22:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-05-29T12:26:00Z",
                            "has_bracket": true,
                            "id": 8002,
                            "league_id": 300,
                            "live_supported": true,
                            "modified_at": "2023-04-25T16:23:17Z",
                            "name": "Knockout Stage",
                            "prizepool": "250000 United States Dollar",
                            "region": null,
                            "serie_id": 4534,
                            "slug": "league-of-legends-mid-invitational-2022-knockout-stage",
                            "tier": "s",
                            "type": null,
                            "winner_id": 74,
                            "winner_type": "Team"
                          }
                        ],
                        "videogame": {
                          "id": 1,
                          "name": "LoL",
                          "slug": "league-of-legends"
                        },
                        "videogame_title": null,
                        "winner_id": 74,
                        "winner_type": "Team",
                        "year": 2022
                      },
                      "totals": {
                        "assists": 745,
                        "atakhan_kills": null,
                        "baron_kills": 16,
                        "blue_games_lost": 2,
                        "blue_games_won": 9,
                        "chemtech_drake_kills": 0,
                        "cloud_drake_kills": 10,
                        "deaths": 260,
                        "dragon_kills": 46,
                        "elder_drake_kills": 0,
                        "games_lost": 6,
                        "games_played": 24,
                        "games_won": 18,
                        "herald_kill": 36,
                        "hextech_drake_kills": 12,
                        "infernal_drake_kills": 8,
                        "inhibitor_kills": 27,
                        "kills": 372,
                        "matches_lost": 4,
                        "matches_played": 18,
                        "matches_won": 14,
                        "mountain_drake_kills": 7,
                        "ocean_drake_kills": 9,
                        "red_games_lost": 4,
                        "red_games_won": 9,
                        "tower_kills": 195,
                        "voidgrub_kills": null,
                        "wards_placed": 2357
                      }
                    },
                    {
                      "averages": {
                        "assists": 34.91,
                        "atakhan_kills": null,
                        "baron_kills": 0.98,
                        "deaths": 10.4,
                        "dragon_kills": 2.36,
                        "game_length": 1947,
                        "gold_earned": 62308.51,
                        "herald_kill": 1.47,
                        "inhibitor_kills": 1.64,
                        "kills": 16.13,
                        "ratios": {
                          "first_atakhan": null,
                          "first_baron": 0.64,
                          "first_blood": 0.58,
                          "first_dragon": 0.42,
                          "first_herald": 0.67,
                          "first_inhibitor": 0.87,
                          "first_tower": 0.84,
                          "first_voidgrub": null,
                          "win": 0.84
                        },
                        "total_minions_killed": 1086.31,
                        "tower_kills": 8.69,
                        "voidgrub_kills": null,
                        "wards_placed": 119.07
                      },
                      "games_count": 45,
                      "serie": {
                        "begin_at": "2022-01-12T08:00:00Z",
                        "end_at": "2022-04-02T12:24:00Z",
                        "full_name": "Spring 2022",
                        "id": 4250,
                        "league": {
                          "id": 293,
                          "image_url": "https://cdn.pandascore.co/images/league/image/293/lck_2021_logo-png",
                          "modified_at": "2021-01-06T15:41:48Z",
                          "name": "LCK",
                          "slug": "league-of-legends-lck-champions-korea",
                          "url": null
                        },
                        "league_id": 293,
                        "modified_at": "2022-04-02T13:58:05Z",
                        "name": null,
                        "season": "Spring",
                        "slug": "league-of-legends-lck-champions-korea-spring-2022",
                        "tournaments": [
                          {
                            "begin_at": "2022-01-12T08:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-03-20T12:20:00Z",
                            "has_bracket": false,
                            "id": 7313,
                            "league_id": 293,
                            "live_supported": true,
                            "modified_at": "2022-08-08T14:39:01Z",
                            "name": "Regular Season",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4250,
                            "slug": "league-of-legends-lck-champions-korea-spring-2022-regular-season",
                            "tier": "a",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-03-23T08:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-04-02T12:24:00Z",
                            "has_bracket": true,
                            "id": 7628,
                            "league_id": 293,
                            "live_supported": true,
                            "modified_at": "2023-04-25T16:35:34Z",
                            "name": "Playoffs",
                            "prizepool": "375000000 South Korean Won",
                            "region": null,
                            "serie_id": 4250,
                            "slug": "league-of-legends-lck-champions-korea-spring-2022-playoffs",
                            "tier": "a",
                            "type": null,
                            "winner_id": 126061,
                            "winner_type": "Team"
                          }
                        ],
                        "videogame": {
                          "id": 1,
                          "name": "LoL",
                          "slug": "league-of-legends"
                        },
                        "videogame_title": null,
                        "winner_id": 126061,
                        "winner_type": "Team",
                        "year": 2022
                      },
                      "totals": {
                        "assists": 1571,
                        "atakhan_kills": null,
                        "baron_kills": 44,
                        "blue_games_lost": 2,
                        "blue_games_won": 15,
                        "chemtech_drake_kills": 4,
                        "cloud_drake_kills": 26,
                        "deaths": 468,
                        "dragon_kills": 106,
                        "elder_drake_kills": 6,
                        "games_lost": 7,
                        "games_played": 45,
                        "games_won": 38,
                        "herald_kill": 66,
                        "hextech_drake_kills": 12,
                        "infernal_drake_kills": 23,
                        "inhibitor_kills": 74,
                        "kills": 726,
                        "matches_lost": 0,
                        "matches_played": 18,
                        "matches_won": 18,
                        "mountain_drake_kills": 16,
                        "ocean_drake_kills": 19,
                        "red_games_lost": 5,
                        "red_games_won": 23,
                        "tower_kills": 391,
                        "voidgrub_kills": null,
                        "wards_placed": 5358
                      }
                    }
                  ],
                  "total_stats": {
                    "averages": {
                      "assists": 33.08,
                      "atakhan_kills": null,
                      "baron_kills": 0.93,
                      "deaths": 10.56,
                      "dragon_kills": 2.23,
                      "game_length": 1872,
                      "gold_earned": 60346.9,
                      "herald_kill": 1.39,
                      "inhibitor_kills": 1.43,
                      "kills": 15.42,
                      "ratios": {
                        "first_atakhan": null,
                        "first_baron": 0.63,
                        "first_blood": 0.54,
                        "first_dragon": 0.42,
                        "first_herald": 0.66,
                        "first_inhibitor": 0.81,
                        "first_tower": 0.84,
                        "first_voidgrub": null,
                        "win": 0.81
                      },
                      "total_minions_killed": 1050.84,
                      "tower_kills": 8.4,
                      "voidgrub_kills": null,
                      "wards_placed": 113.76
                    },
                    "games_count": 83,
                    "totals": {
                      "assists": 2746,
                      "atakhan_kills": null,
                      "baron_kills": 77,
                      "blue_games_lost": 6,
                      "blue_games_won": 30,
                      "chemtech_drake_kills": 4,
                      "cloud_drake_kills": 45,
                      "deaths": 877,
                      "dragon_kills": 185,
                      "elder_drake_kills": 7,
                      "games_lost": 16,
                      "games_played": 83,
                      "games_won": 67,
                      "herald_kill": 115,
                      "hextech_drake_kills": 31,
                      "infernal_drake_kills": 36,
                      "inhibitor_kills": 119,
                      "kills": 1280,
                      "matches_lost": 5,
                      "matches_played": 42,
                      "matches_won": 37,
                      "mountain_drake_kills": 32,
                      "ocean_drake_kills": 30,
                      "red_games_lost": 10,
                      "red_games_won": 37,
                      "tower_kills": 697,
                      "voidgrub_kills": null,
                      "wards_placed": 9442
                    }
                  }
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLStatsForTeam"
            }
          }
        },
        "description": "Statistics of a League-of-Legends team\n\nDeprecated fields:\n- last_games[].players[].minions_killed\n"
      }
    },
    "schemas": {
      "LoLStatsForTeam": {
        "additionalProperties": false,
        "deprecated": false,
        "description": "Aggregated statistics for a team grouped by serie",
        "properties": {
          "acronym": {
            "deprecated": false,
            "nullable": true,
            "title": "TeamAcronym",
            "type": "string"
          },
          "dark_mode_image_url": {
            "deprecated": false,
            "description": "URL of the team logo",
            "format": "uri",
            "nullable": true,
            "title": "TeamImageURL",
            "type": "string"
          },
          "id": {
            "description": "The ID of the team.",
            "minimum": 1,
            "title": "TeamID",
            "type": "integer"
          },
          "image_url": {
            "deprecated": false,
            "description": "URL of the team logo",
            "format": "uri",
            "nullable": true,
            "title": "TeamImageURL",
            "type": "string"
          },
          "last_games": {
            "items": {
              "additionalProperties": false,
              "deprecated": false,
              "description": "A team's last game",
              "properties": {
                "begin_at": {
                  "deprecated": false,
                  "description": "The game begin time, UTC.\n`null` when the game status is `not_started`",
                  "format": "date-time",
                  "minLength": 1,
                  "nullable": true,
                  "title": "GameBeginAt",
                  "type": "string"
                },
                "complete": {
                  "description": "Whether When `true`, the game statistics are complete and will not be updated again",
                  "title": "GameComplete",
                  "type": "boolean"
                },
                "detailed_stats": {
                  "description": "Whether historical data is available for the game",
                  "title": "GameDetailedStats",
                  "type": "boolean"
                },
                "end_at": {
                  "deprecated": false,
                  "description": "The game end time, UTC.\n`null` when the game status is not `finished`",
                  "format": "date-time",
                  "minLength": 1,
                  "nullable": true,
                  "title": "GameEndAt",
                  "type": "string"
                },
                "finished": {
                  "description": "Whether the game is finished",
                  "title": "GameIsFinished",
                  "type": "boolean"
                },
                "forfeit": {
                  "description": "Whether the game has been forfeited",
                  "title": "GameIsForfeit",
                  "type": "boolean"
                },
                "id": {
                  "description": "LoL game ID",
                  "minimum": 1,
                  "title": "LoLGameID",
                  "type": "integer"
                },
                "length": {
                  "deprecated": false,
                  "description": "Duration of the game in seconds.\n`null` when the game status is not `finished`",
                  "minimum": 0,
                  "nullable": true,
                  "title": "GameLength",
                  "type": "integer"
                },
                "match_id": {
                  "minimum": 1,
                  "title": "MatchID",
                  "type": "integer"
                },
                "players": {
                  "deprecated": false,
                  "items": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "description": "Player's data for a Game",
                    "properties": {
                      "assists": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAssistCount",
                        "type": "integer"
                      },
                      "champion": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "nullable": true,
                        "properties": {
                          "id": {
                            "minimum": 1,
                            "title": "LoLChampionID",
                            "type": "integer"
                          },
                          "image_url": {
                            "format": "uri",
                            "title": "LoLChampionImageURL",
                            "type": "string"
                          },
                          "name": {
                            "title": "LoLChampionName",
                            "type": "string"
                          },
                          "slug": {
                            "description": "Human-readable identifier of the champion.",
                            "title": "LoLChampionSlug",
                            "type": "string"
                          }
                        },
                        "required": [
                          "id",
                          "image_url",
                          "name",
                          "slug"
                        ],
                        "title": "BaseLoLChampion",
                        "type": "object"
                      },
                      "creep_score": {
                        "deprecated": false,
                        "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLCreepScore",
                        "type": "integer"
                      },
                      "cs_at_14": {
                        "deprecated": false,
                        "description": "The player's Creep Score (CS.) at 14minutes",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LolCreepScoreAt14",
                        "type": "integer"
                      },
                      "cs_diff_at_14": {
                        "deprecated": false,
                        "description": "Player CS difference compared to their lane opponent at the 14th minute in-game",
                        "nullable": true,
                        "title": "LolCreepScoreDifferenceAt14",
                        "type": "number"
                      },
                      "deaths": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDeathCount",
                        "type": "integer"
                      },
                      "flags": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "first_blood_assist": {
                            "deprecated": false,
                            "description": "Whether player got first blood assist",
                            "nullable": true,
                            "title": "LoLGotFirstBloodAssist",
                            "type": "boolean"
                          },
                          "first_blood_kill": {
                            "deprecated": false,
                            "description": "Whether player got first blood kill",
                            "nullable": true,
                            "title": "LoLGotFirstBloodKill",
                            "type": "boolean"
                          },
                          "first_inhibitor_assist": {
                            "deprecated": false,
                            "description": "Whether player got first inhibitor assist",
                            "nullable": true,
                            "title": "LoLGotFirstInhibitorAssist",
                            "type": "boolean"
                          },
                          "first_inhibitor_kill": {
                            "deprecated": false,
                            "description": "Whether player got first inhibitor kill",
                            "nullable": true,
                            "title": "LoLGotFirstInhibitorKill",
                            "type": "boolean"
                          },
                          "first_tower_assist": {
                            "deprecated": false,
                            "description": "Whether player got first tower assist",
                            "nullable": true,
                            "title": "LoLGotGirstTowerAssist",
                            "type": "boolean"
                          },
                          "first_tower_kill": {
                            "deprecated": false,
                            "description": "Whether player got first tower kill",
                            "nullable": true,
                            "title": "LoLGotFirstTowerKill",
                            "type": "boolean"
                          }
                        },
                        "required": [
                          "first_blood_assist",
                          "first_blood_kill",
                          "first_inhibitor_assist",
                          "first_inhibitor_kill",
                          "first_tower_assist",
                          "first_tower_kill"
                        ],
                        "title": "LoLFlags",
                        "type": "object"
                      },
                      "game_id": {
                        "description": "LoL game ID",
                        "minimum": 1,
                        "title": "LoLGameID",
                        "type": "integer"
                      },
                      "gold_earned": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLGold",
                        "type": "integer"
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
                        "title": "LoLGold",
                        "type": "integer"
                      },
                      "items": {
                        "items": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "id": {
                              "minimum": 1,
                              "title": "LoLItemID",
                              "type": "integer"
                            },
                            "image_url": {
                              "deprecated": false,
                              "format": "uri",
                              "nullable": true,
                              "title": "LoLItemImageURL",
                              "type": "string"
                            },
                            "is_trinket": {
                              "deprecated": false,
                              "description": "Whether item is a trinket",
                              "nullable": true,
                              "title": "LoLItemIsTrinket",
                              "type": "boolean"
                            },
                            "name": {
                              "title": "LoLItemName",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "is_trinket",
                            "name"
                          ],
                          "title": "BaseLoLItem",
                          "type": "object"
                        },
                        "title": "BaseLoLItems",
                        "type": "array"
                      },
                      "kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLKillCount",
                        "type": "integer"
                      },
                      "kills_counters": {
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
                          "neutral_minions": {
                            "deprecated": false,
                            "description": "Creep Score awarded for killing neutral minions.\n\nNB: This can be different than the actual number of neutral minions killed.",
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLNeutralMinionCount",
                            "type": "integer"
                          },
                          "neutral_minions_enemy_jungle": {
                            "deprecated": false,
                            "description": "Creep Score awarded for killing neutral minions in the player's enemy jungle.\n\nNB: This can be different than the actual number of neutral minions killed.",
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLNeutralMinionsEnemyJungleCount",
                            "type": "integer"
                          },
                          "neutral_minions_team_jungle": {
                            "deprecated": false,
                            "description": "Creep Score awarded for killing neutral minions in the player's team jungle.\n\nNB: This can be different than the actual number of neutral minions killed.",
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLNeutralMinionsTeamJungleCount",
                            "type": "integer"
                          },
                          "players": {
                            "deprecated": false,
                            "description": "Number of players killed",
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLPlayerCount",
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
                          "neutral_minions",
                          "neutral_minions_enemy_jungle",
                          "neutral_minions_team_jungle",
                          "players",
                          "turrets",
                          "wards"
                        ],
                        "title": "LoLKillCounters",
                        "type": "object"
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
                      "largest_critical_strike": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLLargestCriticalStrike",
                        "type": "integer"
                      },
                      "largest_killing_spree": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLLargestKillingSpree",
                        "type": "integer"
                      },
                      "largest_multi_kill": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLLargestMultiKill",
                        "type": "integer"
                      },
                      "level": {
                        "deprecated": false,
                        "minimum": 1,
                        "nullable": true,
                        "title": "LoLChampionLevel",
                        "type": "integer"
                      },
                      "magic_damage": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "dealt": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLDamage",
                            "type": "integer"
                          },
                          "dealt_percentage": {
                            "deprecated": false,
                            "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                            "maximum": 100,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLPlayerDamageDealtPercentage",
                            "type": "number"
                          },
                          "dealt_to_champions": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLDamage",
                            "type": "integer"
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
                            "title": "LoLDamage",
                            "type": "integer"
                          }
                        },
                        "required": [
                          "dealt",
                          "dealt_percentage",
                          "dealt_to_champions",
                          "dealt_to_champions_percentage",
                          "taken"
                        ],
                        "title": "LoLMagicDamage",
                        "type": "object"
                      },
                      "masteries": {
                        "items": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "id": {
                              "minimum": 1,
                              "title": "LoLMasteryID",
                              "type": "integer"
                            },
                            "name": {
                              "title": "LoLMasteryName",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "name"
                          ],
                          "title": "LoLMastery",
                          "type": "object"
                        },
                        "title": "LoLMasteries",
                        "type": "array"
                      },
                      "minions_killed": {
                        "deprecated": true,
                        "description": "The player's Creep Score (CS.)",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLMinionsKilled",
                        "type": "integer"
                      },
                      "opponent": {
                        "deprecated": false,
                        "nullable": true,
                        "oneOf": [
                          {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "active": {
                                "description": "Whether player is active",
                                "title": "PlayerIsActive",
                                "type": "boolean"
                              },
                              "age": {
                                "deprecated": false,
                                "description": "Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age)\n**Note**: This field is only present for users running the Historical plan or above.",
                                "minimum": 0,
                                "nullable": true,
                                "title": "PlayerAge",
                                "type": "number"
                              },
                              "birthday": {
                                "deprecated": false,
                                "description": "Birth day of the player, `YYYY-MM-DD` format. `null` if unknown.\n**Note**: This field is only present for users running the Historical plan or above.",
                                "nullable": true,
                                "title": "PlayerBirthday",
                                "type": "string"
                              },
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
                              "image_url": {
                                "deprecated": false,
                                "description": "URL to the photo of the player. `null` if not available.",
                                "format": "uri",
                                "nullable": true,
                                "title": "PlayerImageURL",
                                "type": "string"
                              },
                              "last_name": {
                                "deprecated": false,
                                "description": "Last name of the player. `null` if unknown",
                                "nullable": true,
                                "title": "PlayerLastName",
                                "type": "string"
                              },
                              "modified_at": {
                                "format": "date-time",
                                "minLength": 1,
                                "title": "PlayerModifiedAt",
                                "type": "string"
                              },
                              "name": {
                                "description": "Professional name of the player",
                                "title": "PlayerName",
                                "type": "string"
                              },
                              "nationality": {
                                "deprecated": false,
                                "description": "Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code).\nIn addition to the standard, the `XK` code is used for Kosovo.\n`null` if unknown",
                                "nullable": true,
                                "title": "PlayerNationality",
                                "type": "string"
                              },
                              "role": {
                                "deprecated": false,
                                "description": "Role/position of the player. Field value varies depending on the video game.`null` if unknown.\n**Note**: role is only available for DotA 2, League of Legends, and Overwatch players.\n`null` for other video games.",
                                "nullable": true,
                                "title": "PlayerRoleSlug",
                                "type": "string"
                              },
                              "slug": {
                                "deprecated": false,
                                "description": "Unique, human-readable identifier for the player.\n`id` and `slug` can be used interchangeably throughout the API.",
                                "minLength": 1,
                                "nullable": true,
                                "pattern": "^[a-z0-9_-]+$",
                                "title": "PlayerSlug",
                                "type": "string"
                              }
                            },
                            "required": [
                              "active",
                              "age",
                              "birthday",
                              "first_name",
                              "id",
                              "image_url",
                              "last_name",
                              "modified_at",
                              "name",
                              "nationality",
                              "role",
                              "slug"
                            ],
                            "title": "BasePlayer",
                            "type": "object"
                          },
                          {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "acronym": {
                                "deprecated": false,
                                "nullable": true,
                                "title": "TeamAcronym",
                                "type": "string"
                              },
                              "dark_mode_image_url": {
                                "deprecated": false,
                                "description": "URL of the team logo",
                                "format": "uri",
                                "nullable": true,
                                "title": "TeamImageURL",
                                "type": "string"
                              },
                              "id": {
                                "description": "The ID of the team.",
                                "minimum": 1,
                                "title": "TeamID",
                                "type": "integer"
                              },
                              "image_url": {
                                "deprecated": false,
                                "description": "URL of the team logo",
                                "format": "uri",
                                "nullable": true,
                                "title": "TeamImageURL",
                                "type": "string"
                              },
                              "location": {
                                "deprecated": false,
                                "description": "The team's organization location",
                                "nullable": true,
                                "title": "TeamLocation",
                                "type": "string"
                              },
                              "modified_at": {
                                "format": "date-time",
                                "minLength": 1,
                                "title": "TeamModifiedAt",
                                "type": "string"
                              },
                              "name": {
                                "description": "The name of the team.",
                                "title": "TeamName",
                                "type": "string"
                              },
                              "slug": {
                                "deprecated": false,
                                "minLength": 1,
                                "nullable": true,
                                "pattern": "^[a-z0-9_-]+$",
                                "title": "TeamSlug",
                                "type": "string"
                              }
                            },
                            "required": [
                              "acronym",
                              "dark_mode_image_url",
                              "id",
                              "image_url",
                              "location",
                              "modified_at",
                              "name",
                              "slug"
                            ],
                            "title": "BaseTeam",
                            "type": "object"
                          }
                        ],
                        "title": "BaseOpponent"
                      },
                      "physical_damage": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "dealt": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLDamage",
                            "type": "integer"
                          },
                          "dealt_percentage": {
                            "deprecated": false,
                            "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                            "maximum": 100,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLPlayerDamageDealtPercentage",
                            "type": "number"
                          },
                          "dealt_to_champions": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLDamage",
                            "type": "integer"
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
                            "title": "LoLDamage",
                            "type": "integer"
                          }
                        },
                        "required": [
                          "dealt",
                          "dealt_percentage",
                          "dealt_to_champions",
                          "dealt_to_champions_percentage",
                          "taken"
                        ],
                        "title": "LoLPhysicalDamage",
                        "type": "object"
                      },
                      "player": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "active": {
                            "description": "Whether player is active",
                            "title": "PlayerIsActive",
                            "type": "boolean"
                          },
                          "age": {
                            "deprecated": false,
                            "description": "Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age)\n**Note**: This field is only present for users running the Historical plan or above.",
                            "minimum": 0,
                            "nullable": true,
                            "title": "PlayerAge",
                            "type": "number"
                          },
                          "birthday": {
                            "deprecated": false,
                            "description": "Birth day of the player, `YYYY-MM-DD` format. `null` if unknown.\n**Note**: This field is only present for users running the Historical plan or above.",
                            "nullable": true,
                            "title": "PlayerBirthday",
                            "type": "string"
                          },
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
                          "image_url": {
                            "deprecated": false,
                            "description": "URL to the photo of the player. `null` if not available.",
                            "format": "uri",
                            "nullable": true,
                            "title": "PlayerImageURL",
                            "type": "string"
                          },
                          "last_name": {
                            "deprecated": false,
                            "description": "Last name of the player. `null` if unknown",
                            "nullable": true,
                            "title": "PlayerLastName",
                            "type": "string"
                          },
                          "modified_at": {
                            "format": "date-time",
                            "minLength": 1,
                            "title": "PlayerModifiedAt",
                            "type": "string"
                          },
                          "name": {
                            "description": "Professional name of the player",
                            "title": "PlayerName",
                            "type": "string"
                          },
                          "nationality": {
                            "deprecated": false,
                            "description": "Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code).\nIn addition to the standard, the `XK` code is used for Kosovo.\n`null` if unknown",
                            "nullable": true,
                            "title": "PlayerNationality",
                            "type": "string"
                          },
                          "role": {
                            "deprecated": false,
                            "description": "Role/position of the player. Field value varies depending on the video game.`null` if unknown.\n**Note**: role is only available for DotA 2, League of Legends, and Overwatch players.\n`null` for other video games.",
                            "nullable": true,
                            "title": "PlayerRoleSlug",
                            "type": "string"
                          },
                          "slug": {
                            "deprecated": false,
                            "description": "Unique, human-readable identifier for the player.\n`id` and `slug` can be used interchangeably throughout the API.",
                            "minLength": 1,
                            "nullable": true,
                            "pattern": "^[a-z0-9_-]+$",
                            "title": "PlayerSlug",
                            "type": "string"
                          }
                        },
                        "required": [
                          "active",
                          "age",
                          "birthday",
                          "first_name",
                          "id",
                          "image_url",
                          "last_name",
                          "modified_at",
                          "name",
                          "nationality",
                          "role",
                          "slug"
                        ],
                        "title": "BasePlayer",
                        "type": "object"
                      },
                      "player_id": {
                        "description": "ID of the player",
                        "minimum": 1,
                        "title": "PlayerID",
                        "type": "integer"
                      },
                      "role": {
                        "deprecated": false,
                        "enum": [
                          "adc",
                          "jun",
                          "mid",
                          "sup",
                          "top"
                        ],
                        "nullable": true,
                        "title": "LoLPlayerRole",
                        "type": "string"
                      },
                      "runes": {
                        "items": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "id": {
                              "minimum": 1,
                              "title": "LoLRuneID",
                              "type": "integer"
                            },
                            "name": {
                              "title": "LoLRuneName",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "name"
                          ],
                          "title": "LoLRune",
                          "type": "object"
                        },
                        "title": "LoLRunes",
                        "type": "array"
                      },
                      "runes_reforged": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "primary_path": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "nullable": true,
                            "properties": {
                              "id": {
                                "description": "ID of the rune",
                                "minimum": 1,
                                "title": "LoLRuneReforgedID",
                                "type": "integer"
                              },
                              "image_url": {
                                "description": "URL to an image of the rune",
                                "format": "uri",
                                "title": "LoLRuneReforgedImageURL",
                                "type": "string"
                              },
                              "keystone": {
                                "additionalProperties": false,
                                "deprecated": false,
                                "properties": {
                                  "id": {
                                    "description": "ID of the rune",
                                    "minimum": 1,
                                    "title": "LoLRuneReforgedID",
                                    "type": "integer"
                                  },
                                  "image_url": {
                                    "description": "URL to an image of the rune",
                                    "format": "uri",
                                    "title": "LoLRuneReforgedImageURL",
                                    "type": "string"
                                  },
                                  "name": {
                                    "description": "Name of the rune path",
                                    "title": "LoLRuneReforgedName",
                                    "type": "string"
                                  },
                                  "type": {
                                    "enum": [
                                      "keystone",
                                      "path",
                                      "shard",
                                      "slot1",
                                      "slot2",
                                      "slot3"
                                    ],
                                    "title": "LoLRuneReforgedType",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "id",
                                  "image_url",
                                  "name",
                                  "type"
                                ],
                                "title": "LoLRuneReforged",
                                "type": "object"
                              },
                              "lesser_runes": {
                                "items": {
                                  "additionalProperties": false,
                                  "deprecated": false,
                                  "properties": {
                                    "id": {
                                      "description": "ID of the rune",
                                      "minimum": 1,
                                      "title": "LoLRuneReforgedID",
                                      "type": "integer"
                                    },
                                    "image_url": {
                                      "description": "URL to an image of the rune",
                                      "format": "uri",
                                      "title": "LoLRuneReforgedImageURL",
                                      "type": "string"
                                    },
                                    "name": {
                                      "description": "Name of the rune path",
                                      "title": "LoLRuneReforgedName",
                                      "type": "string"
                                    },
                                    "type": {
                                      "enum": [
                                        "keystone",
                                        "path",
                                        "shard",
                                        "slot1",
                                        "slot2",
                                        "slot3"
                                      ],
                                      "title": "LoLRuneReforgedType",
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "image_url",
                                    "name",
                                    "type"
                                  ],
                                  "title": "LoLRuneReforged",
                                  "type": "object"
                                },
                                "title": "LoLRunesReforged",
                                "type": "array"
                              },
                              "name": {
                                "description": "Name of the rune path",
                                "title": "LoLRuneReforgedName",
                                "type": "string"
                              },
                              "type": {
                                "enum": [
                                  "keystone",
                                  "path",
                                  "shard",
                                  "slot1",
                                  "slot2",
                                  "slot3"
                                ],
                                "title": "LoLRuneReforgedType",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "image_url",
                              "keystone",
                              "lesser_runes",
                              "name",
                              "type"
                            ],
                            "title": "LoLPlayerPrimaryRunePath",
                            "type": "object"
                          },
                          "secondary_path": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "nullable": true,
                            "properties": {
                              "id": {
                                "description": "ID of the rune",
                                "minimum": 1,
                                "title": "LoLRuneReforgedID",
                                "type": "integer"
                              },
                              "image_url": {
                                "description": "URL to an image of the rune",
                                "format": "uri",
                                "title": "LoLRuneReforgedImageURL",
                                "type": "string"
                              },
                              "lesser_runes": {
                                "items": {
                                  "additionalProperties": false,
                                  "deprecated": false,
                                  "properties": {
                                    "id": {
                                      "description": "ID of the rune",
                                      "minimum": 1,
                                      "title": "LoLRuneReforgedID",
                                      "type": "integer"
                                    },
                                    "image_url": {
                                      "description": "URL to an image of the rune",
                                      "format": "uri",
                                      "title": "LoLRuneReforgedImageURL",
                                      "type": "string"
                                    },
                                    "name": {
                                      "description": "Name of the rune path",
                                      "title": "LoLRuneReforgedName",
                                      "type": "string"
                                    },
                                    "type": {
                                      "enum": [
                                        "keystone",
                                        "path",
                                        "shard",
                                        "slot1",
                                        "slot2",
                                        "slot3"
                                      ],
                                      "title": "LoLRuneReforgedType",
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "image_url",
                                    "name",
                                    "type"
                                  ],
                                  "title": "LoLRuneReforged",
                                  "type": "object"
                                },
                                "title": "LoLRunesReforged",
                                "type": "array"
                              },
                              "name": {
                                "description": "Name of the rune path",
                                "title": "LoLRuneReforgedName",
                                "type": "string"
                              },
                              "type": {
                                "enum": [
                                  "keystone",
                                  "path",
                                  "shard",
                                  "slot1",
                                  "slot2",
                                  "slot3"
                                ],
                                "title": "LoLRuneReforgedType",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "image_url",
                              "lesser_runes",
                              "name",
                              "type"
                            ],
                            "title": "LoLPlayerSecondaryRunePath",
                            "type": "object"
                          },
                          "shards": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "defense": {
                                "additionalProperties": false,
                                "deprecated": false,
                                "nullable": true,
                                "properties": {
                                  "id": {
                                    "description": "ID of the rune",
                                    "minimum": 1,
                                    "title": "LoLRuneReforgedID",
                                    "type": "integer"
                                  },
                                  "image_url": {
                                    "description": "URL to an image of the rune",
                                    "format": "uri",
                                    "title": "LoLRuneReforgedImageURL",
                                    "type": "string"
                                  },
                                  "name": {
                                    "description": "Name of the rune path",
                                    "title": "LoLRuneReforgedName",
                                    "type": "string"
                                  },
                                  "type": {
                                    "enum": [
                                      "keystone",
                                      "path",
                                      "shard",
                                      "slot1",
                                      "slot2",
                                      "slot3"
                                    ],
                                    "title": "LoLRuneReforgedType",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "id",
                                  "image_url",
                                  "name",
                                  "type"
                                ],
                                "title": "LoLRuneReforged",
                                "type": "object"
                              },
                              "flex": {
                                "additionalProperties": false,
                                "deprecated": false,
                                "nullable": true,
                                "properties": {
                                  "id": {
                                    "description": "ID of the rune",
                                    "minimum": 1,
                                    "title": "LoLRuneReforgedID",
                                    "type": "integer"
                                  },
                                  "image_url": {
                                    "description": "URL to an image of the rune",
                                    "format": "uri",
                                    "title": "LoLRuneReforgedImageURL",
                                    "type": "string"
                                  },
                                  "name": {
                                    "description": "Name of the rune path",
                                    "title": "LoLRuneReforgedName",
                                    "type": "string"
                                  },
                                  "type": {
                                    "enum": [
                                      "keystone",
                                      "path",
                                      "shard",
                                      "slot1",
                                      "slot2",
                                      "slot3"
                                    ],
                                    "title": "LoLRuneReforgedType",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "id",
                                  "image_url",
                                  "name",
                                  "type"
                                ],
                                "title": "LoLRuneReforged",
                                "type": "object"
                              },
                              "offense": {
                                "additionalProperties": false,
                                "deprecated": false,
                                "nullable": true,
                                "properties": {
                                  "id": {
                                    "description": "ID of the rune",
                                    "minimum": 1,
                                    "title": "LoLRuneReforgedID",
                                    "type": "integer"
                                  },
                                  "image_url": {
                                    "description": "URL to an image of the rune",
                                    "format": "uri",
                                    "title": "LoLRuneReforgedImageURL",
                                    "type": "string"
                                  },
                                  "name": {
                                    "description": "Name of the rune path",
                                    "title": "LoLRuneReforgedName",
                                    "type": "string"
                                  },
                                  "type": {
                                    "enum": [
                                      "keystone",
                                      "path",
                                      "shard",
                                      "slot1",
                                      "slot2",
                                      "slot3"
                                    ],
                                    "title": "LoLRuneReforgedType",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "id",
                                  "image_url",
                                  "name",
                                  "type"
                                ],
                                "title": "LoLRuneReforged",
                                "type": "object"
                              }
                            },
                            "required": [
                              "defense",
                              "flex",
                              "offense"
                            ],
                            "title": "LoLPlayerRuneShards",
                            "type": "object"
                          }
                        },
                        "required": [
                          "primary_path",
                          "secondary_path",
                          "shards"
                        ],
                        "title": "LoLPlayerRunesReforged",
                        "type": "object"
                      },
                      "spells": {
                        "items": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "id": {
                              "minimum": 1,
                              "title": "LoLSpellID",
                              "type": "integer"
                            },
                            "image_url": {
                              "format": "uri",
                              "title": "LoLSpellImageURL",
                              "type": "string"
                            },
                            "name": {
                              "title": "LoLSpellName",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name"
                          ],
                          "title": "LoLSpell",
                          "type": "object"
                        },
                        "title": "LoLSpells",
                        "type": "array"
                      },
                      "team": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "acronym": {
                            "deprecated": false,
                            "nullable": true,
                            "title": "TeamAcronym",
                            "type": "string"
                          },
                          "dark_mode_image_url": {
                            "deprecated": false,
                            "description": "URL of the team logo",
                            "format": "uri",
                            "nullable": true,
                            "title": "TeamImageURL",
                            "type": "string"
                          },
                          "id": {
                            "description": "The ID of the team.",
                            "minimum": 1,
                            "title": "TeamID",
                            "type": "integer"
                          },
                          "image_url": {
                            "deprecated": false,
                            "description": "URL of the team logo",
                            "format": "uri",
                            "nullable": true,
                            "title": "TeamImageURL",
                            "type": "string"
                          },
                          "location": {
                            "deprecated": false,
                            "description": "The team's organization location",
                            "nullable": true,
                            "title": "TeamLocation",
                            "type": "string"
                          },
                          "modified_at": {
                            "format": "date-time",
                            "minLength": 1,
                            "title": "TeamModifiedAt",
                            "type": "string"
                          },
                          "name": {
                            "description": "The name of the team.",
                            "title": "TeamName",
                            "type": "string"
                          },
                          "slug": {
                            "deprecated": false,
                            "minLength": 1,
                            "nullable": true,
                            "pattern": "^[a-z0-9_-]+$",
                            "title": "TeamSlug",
                            "type": "string"
                          }
                        },
                        "required": [
                          "acronym",
                          "dark_mode_image_url",
                          "id",
                          "image_url",
                          "location",
                          "modified_at",
                          "name",
                          "slug"
                        ],
                        "title": "BaseTeam",
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
                            "title": "LoLDamage",
                            "type": "integer"
                          },
                          "dealt_percentage": {
                            "deprecated": false,
                            "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                            "maximum": 100,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLPlayerDamageDealtPercentage",
                            "type": "number"
                          },
                          "dealt_to_champions": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLDamage",
                            "type": "integer"
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
                            "title": "LoLDamage",
                            "type": "integer"
                          }
                        },
                        "required": [
                          "dealt",
                          "dealt_percentage",
                          "dealt_to_champions",
                          "dealt_to_champions_percentage",
                          "taken"
                        ],
                        "title": "LoLTotalDamage",
                        "type": "object"
                      },
                      "total_heal": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLTotalHeal",
                        "type": "integer"
                      },
                      "total_time_crowd_control_dealt": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLTotalTimeCrowdControlDealt",
                        "type": "integer"
                      },
                      "total_units_healed": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLTotalUnitsHealed",
                        "type": "integer"
                      },
                      "true_damage": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "dealt": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLDamage",
                            "type": "integer"
                          },
                          "dealt_percentage": {
                            "deprecated": false,
                            "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                            "maximum": 100,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLPlayerDamageDealtPercentage",
                            "type": "number"
                          },
                          "dealt_to_champions": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLDamage",
                            "type": "integer"
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
                            "title": "LoLDamage",
                            "type": "integer"
                          }
                        },
                        "required": [
                          "dealt",
                          "dealt_percentage",
                          "dealt_to_champions",
                          "dealt_to_champions_percentage",
                          "taken"
                        ],
                        "title": "LoLTrueDamage",
                        "type": "object"
                      },
                      "wards": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "placed": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLWardsPlaced",
                            "type": "integer"
                          },
                          "sight_wards_bought_in_game": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLSightWards",
                            "type": "integer"
                          },
                          "vision_wards_bought_in_game": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLVisionWards",
                            "type": "integer"
                          }
                        },
                        "required": [
                          "placed",
                          "sight_wards_bought_in_game",
                          "vision_wards_bought_in_game"
                        ],
                        "title": "LoLWards",
                        "type": "object"
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
                      "champion",
                      "creep_score",
                      "cs_at_14",
                      "cs_diff_at_14",
                      "deaths",
                      "flags",
                      "game_id",
                      "gold_earned",
                      "gold_percentage",
                      "gold_spent",
                      "items",
                      "kills",
                      "kills_counters",
                      "kills_series",
                      "largest_critical_strike",
                      "largest_killing_spree",
                      "largest_multi_kill",
                      "level",
                      "magic_damage",
                      "masteries",
                      "minions_killed",
                      "opponent",
                      "physical_damage",
                      "player",
                      "player_id",
                      "role",
                      "runes",
                      "runes_reforged",
                      "spells",
                      "team",
                      "total_damage",
                      "total_heal",
                      "total_time_crowd_control_dealt",
                      "total_units_healed",
                      "true_damage",
                      "wards",
                      "wards_placed"
                    ],
                    "title": "LoLGamePlayer",
                    "type": "object"
                  },
                  "nullable": true,
                  "title": "LoLGamePlayers",
                  "type": "array"
                },
                "position": {
                  "description": "Game position in the match. Starts at 1",
                  "minimum": 1,
                  "title": "GamePosition",
                  "type": "integer"
                },
                "status": {
                  "description": "The game status",
                  "enum": [
                    "finished",
                    "not_played",
                    "not_started",
                    "running"
                  ],
                  "title": "GameStatus",
                  "type": "string"
                },
                "teams": {
                  "deprecated": false,
                  "items": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "description": "Team's data for a Game",
                    "properties": {
                      "atakhan_kills": {
                        "deprecated": false,
                        "description": "The number of Atakhan killed by a team.",
                        "maximum": 1,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAtakhanKills",
                        "type": "integer"
                      },
                      "bans": {
                        "items": {
                          "minimum": 1,
                          "title": "LoLChampionID",
                          "type": "integer"
                        },
                        "title": "LoLChampionIDs",
                        "type": "array"
                      },
                      "baron_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLBaronKills",
                        "type": "integer"
                      },
                      "chemtech_drake_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLChemtechDrakeKills",
                        "type": "integer"
                      },
                      "cloud_drake_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLCloudDrakeKills",
                        "type": "integer"
                      },
                      "color": {
                        "enum": [
                          "blue",
                          "red"
                        ],
                        "title": "LoLTeamColor",
                        "type": "string"
                      },
                      "dragon_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDragonKills",
                        "type": "integer"
                      },
                      "elder_drake_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLElderDrakeKills",
                        "type": "integer"
                      },
                      "first_atakhan": {
                        "deprecated": false,
                        "description": "Whether team killed the first Atakhan",
                        "nullable": true,
                        "title": "LoLTeamGotFirstAtakhan",
                        "type": "boolean"
                      },
                      "first_baron": {
                        "deprecated": false,
                        "description": "Whether team got first baron Nashor",
                        "nullable": true,
                        "title": "LoLTeamGotFirstBaron",
                        "type": "boolean"
                      },
                      "first_blood": {
                        "deprecated": false,
                        "description": "Whether team got first blood",
                        "nullable": true,
                        "title": "LoLTeamGotFirstBlood",
                        "type": "boolean"
                      },
                      "first_dragon": {
                        "deprecated": false,
                        "description": "Whether team got first dragon",
                        "nullable": true,
                        "title": "LoLTeamGotFirstDragon",
                        "type": "boolean"
                      },
                      "first_herald": {
                        "deprecated": false,
                        "description": "Whether team got first herald",
                        "nullable": true,
                        "title": "LoLTeamGotFirstHerald",
                        "type": "boolean"
                      },
                      "first_inhibitor": {
                        "deprecated": false,
                        "description": "Whether team got first inhibitor",
                        "nullable": true,
                        "title": "LoLTeamGotFirstInhibitor",
                        "type": "boolean"
                      },
                      "first_tower": {
                        "deprecated": false,
                        "description": "Whether team got first tower",
                        "nullable": true,
                        "title": "LoLTeamGotFirstTower",
                        "type": "boolean"
                      },
                      "first_voidgrub": {
                        "deprecated": false,
                        "description": "Whether team killed the first voidgrub",
                        "nullable": true,
                        "title": "LoLTeamGotFirstVoidgrub",
                        "type": "boolean"
                      },
                      "gold_earned": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLGold",
                        "type": "integer"
                      },
                      "herald_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLHeraldKills",
                        "type": "integer"
                      },
                      "hextech_drake_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLHextechDrakeKills",
                        "type": "integer"
                      },
                      "infernal_drake_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLInfernalDrakeKills",
                        "type": "integer"
                      },
                      "inhibitor_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLInhibitorKills",
                        "type": "integer"
                      },
                      "kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLKillCount",
                        "type": "integer"
                      },
                      "mountain_drake_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLMountainDrakeKills",
                        "type": "integer"
                      },
                      "ocean_drake_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLOceanDrakeKills",
                        "type": "integer"
                      },
                      "player_ids": {
                        "items": {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        "title": "PlayerIDs",
                        "type": "array"
                      },
                      "team": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "acronym": {
                            "deprecated": false,
                            "nullable": true,
                            "title": "TeamAcronym",
                            "type": "string"
                          },
                          "dark_mode_image_url": {
                            "deprecated": false,
                            "description": "URL of the team logo",
                            "format": "uri",
                            "nullable": true,
                            "title": "TeamImageURL",
                            "type": "string"
                          },
                          "id": {
                            "description": "The ID of the team.",
                            "minimum": 1,
                            "title": "TeamID",
                            "type": "integer"
                          },
                          "image_url": {
                            "deprecated": false,
                            "description": "URL of the team logo",
                            "format": "uri",
                            "nullable": true,
                            "title": "TeamImageURL",
                            "type": "string"
                          },
                          "location": {
                            "deprecated": false,
                            "description": "The team's organization location",
                            "nullable": true,
                            "title": "TeamLocation",
                            "type": "string"
                          },
                          "modified_at": {
                            "format": "date-time",
                            "minLength": 1,
                            "title": "TeamModifiedAt",
                            "type": "string"
                          },
                          "name": {
                            "description": "The name of the team.",
                            "title": "TeamName",
                            "type": "string"
                          },
                          "slug": {
                            "deprecated": false,
                            "minLength": 1,
                            "nullable": true,
                            "pattern": "^[a-z0-9_-]+$",
                            "title": "TeamSlug",
                            "type": "string"
                          }
                        },
                        "required": [
                          "acronym",
                          "dark_mode_image_url",
                          "id",
                          "image_url",
                          "location",
                          "modified_at",
                          "name",
                          "slug"
                        ],
                        "title": "BaseTeam",
                        "type": "object"
                      },
                      "tower_kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLTowerKills",
                        "type": "integer"
                      },
                      "voidgrub_kills": {
                        "deprecated": false,
                        "description": "The number of voidgrubs killed by a team.",
                        "maximum": 6,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLVoidgrubKills",
                        "type": "integer"
                      }
                    },
                    "required": [
                      "atakhan_kills",
                      "bans",
                      "baron_kills",
                      "chemtech_drake_kills",
                      "cloud_drake_kills",
                      "color",
                      "dragon_kills",
                      "elder_drake_kills",
                      "first_atakhan",
                      "first_baron",
                      "first_blood",
                      "first_dragon",
                      "first_herald",
                      "first_inhibitor",
                      "first_tower",
                      "first_voidgrub",
                      "gold_earned",
                      "herald_kills",
                      "hextech_drake_kills",
                      "infernal_drake_kills",
                      "inhibitor_kills",
                      "kills",
                      "mountain_drake_kills",
                      "ocean_drake_kills",
                      "player_ids",
                      "team",
                      "tower_kills",
                      "voidgrub_kills"
                    ],
                    "title": "LoLGameTeam",
                    "type": "object"
                  },
                  "nullable": true,
                  "title": "LoLGameTeams",
                  "type": "array"
                },
                "winner": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "id": {
                      "anyOf": [
                        {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        {
                          "description": "The ID of the team.",
                          "minimum": 1,
                          "title": "TeamID",
                          "type": "integer"
                        }
                      ],
                      "deprecated": false,
                      "nullable": true,
                      "title": "OpponentID"
                    },
                    "type": {
                      "deprecated": false,
                      "enum": [
                        "Player",
                        "Team"
                      ],
                      "nullable": true,
                      "title": "OpponentType",
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "type"
                  ],
                  "title": "GameWinner",
                  "type": "object"
                },
                "winner_type": {
                  "deprecated": false,
                  "enum": [
                    "Player",
                    "Team"
                  ],
                  "nullable": true,
                  "title": "OpponentType",
                  "type": "string"
                }
              },
              "required": [
                "begin_at",
                "complete",
                "detailed_stats",
                "end_at",
                "finished",
                "forfeit",
                "id",
                "length",
                "match_id",
                "players",
                "position",
                "status",
                "teams",
                "winner",
                "winner_type"
              ],
              "title": "LoLTeamLastGame",
              "type": "object"
            },
            "title": "LoLTeamLastGames",
            "type": "array"
          },
          "location": {
            "deprecated": false,
            "description": "The team's organization location",
            "nullable": true,
            "title": "TeamLocation",
            "type": "string"
          },
          "modified_at": {
            "format": "date-time",
            "minLength": 1,
            "title": "TeamModifiedAt",
            "type": "string"
          },
          "most_banned": {
            "items": {
              "additionalProperties": false,
              "deprecated": false,
              "description": "A team's banned champion",
              "properties": {
                "count": {
                  "minimum": 0,
                  "title": "LoLChampionPickedOrBannedCount",
                  "type": "integer"
                },
                "name": {
                  "title": "LoLChampionName",
                  "type": "string"
                },
                "slug": {
                  "description": "Human-readable identifier of the champion.",
                  "title": "LoLChampionSlug",
                  "type": "string"
                }
              },
              "required": [
                "count",
                "name",
                "slug"
              ],
              "title": "LoLBannedChampion",
              "type": "object"
            },
            "title": "LoLBannedChampions",
            "type": "array"
          },
          "most_banned_against": {
            "items": {
              "additionalProperties": false,
              "deprecated": false,
              "description": "A team's banned champion",
              "properties": {
                "count": {
                  "minimum": 0,
                  "title": "LoLChampionPickedOrBannedCount",
                  "type": "integer"
                },
                "name": {
                  "title": "LoLChampionName",
                  "type": "string"
                },
                "slug": {
                  "description": "Human-readable identifier of the champion.",
                  "title": "LoLChampionSlug",
                  "type": "string"
                }
              },
              "required": [
                "count",
                "name",
                "slug"
              ],
              "title": "LoLBannedChampion",
              "type": "object"
            },
            "title": "LoLBannedChampions",
            "type": "array"
          },
          "most_picked": {
            "items": {
              "additionalProperties": false,
              "deprecated": false,
              "description": "A team's picked champion",
              "properties": {
                "count": {
                  "minimum": 0,
                  "title": "LoLChampionPickedOrBannedCount",
                  "type": "integer"
                },
                "games_lost": {
                  "description": "Number of games lost by the team on the given champion",
                  "type": "integer"
                },
                "games_won": {
                  "description": "Number of games won by the team on the given champion",
                  "type": "integer"
                },
                "name": {
                  "title": "LoLChampionName",
                  "type": "string"
                },
                "slug": {
                  "description": "Human-readable identifier of the champion.",
                  "title": "LoLChampionSlug",
                  "type": "string"
                }
              },
              "required": [
                "count",
                "games_lost",
                "games_won",
                "name",
                "slug"
              ],
              "title": "LoLPickedChampion",
              "type": "object"
            },
            "title": "LoLPickedChampions",
            "type": "array"
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
                "active": {
                  "description": "Whether player is active",
                  "title": "PlayerIsActive",
                  "type": "boolean"
                },
                "age": {
                  "deprecated": false,
                  "description": "Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age)\n**Note**: This field is only present for users running the Historical plan or above.",
                  "minimum": 0,
                  "nullable": true,
                  "title": "PlayerAge",
                  "type": "number"
                },
                "birthday": {
                  "deprecated": false,
                  "description": "Birth day of the player, `YYYY-MM-DD` format. `null` if unknown.\n**Note**: This field is only present for users running the Historical plan or above.",
                  "nullable": true,
                  "title": "PlayerBirthday",
                  "type": "string"
                },
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
                "image_url": {
                  "deprecated": false,
                  "description": "URL to the photo of the player. `null` if not available.",
                  "format": "uri",
                  "nullable": true,
                  "title": "PlayerImageURL",
                  "type": "string"
                },
                "last_name": {
                  "deprecated": false,
                  "description": "Last name of the player. `null` if unknown",
                  "nullable": true,
                  "title": "PlayerLastName",
                  "type": "string"
                },
                "modified_at": {
                  "format": "date-time",
                  "minLength": 1,
                  "title": "PlayerModifiedAt",
                  "type": "string"
                },
                "name": {
                  "description": "Professional name of the player",
                  "title": "PlayerName",
                  "type": "string"
                },
                "nationality": {
                  "deprecated": false,
                  "description": "Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code).\nIn addition to the standard, the `XK` code is used for Kosovo.\n`null` if unknown",
                  "nullable": true,
                  "title": "PlayerNationality",
                  "type": "string"
                },
                "role": {
                  "deprecated": false,
                  "description": "Role/position of the player. Field value varies depending on the video game.`null` if unknown.\n**Note**: role is only available for DotA 2, League of Legends, and Overwatch players.\n`null` for other video games.",
                  "nullable": true,
                  "title": "PlayerRoleSlug",
                  "type": "string"
                },
                "slug": {
                  "deprecated": false,
                  "description": "Unique, human-readable identifier for the player.\n`id` and `slug` can be used interchangeably throughout the API.",
                  "minLength": 1,
                  "nullable": true,
                  "pattern": "^[a-z0-9_-]+$",
                  "title": "PlayerSlug",
                  "type": "string"
                }
              },
              "required": [
                "active",
                "age",
                "birthday",
                "first_name",
                "id",
                "image_url",
                "last_name",
                "modified_at",
                "name",
                "nationality",
                "role",
                "slug"
              ],
              "title": "BasePlayer",
              "type": "object"
            },
            "title": "BasePlayers",
            "type": "array"
          },
          "slug": {
            "deprecated": false,
            "minLength": 1,
            "nullable": true,
            "pattern": "^[a-z0-9_-]+$",
            "title": "TeamSlug",
            "type": "string"
          },
          "stats": {
            "items": {
              "additionalProperties": false,
              "deprecated": false,
              "description": "Team's statistics for a serie",
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
                    "atakhan_kills": {
                      "deprecated": false,
                      "description": "The number of Atakhan killed by a team.",
                      "maximum": 1,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLTeamAtakhanKillsAverage",
                      "type": "number"
                    },
                    "baron_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLAverageBaronKills",
                      "type": "number"
                    },
                    "deaths": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLAverageDeaths",
                      "type": "number"
                    },
                    "dragon_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLAverageDragonKills",
                      "type": "number"
                    },
                    "game_length": {
                      "deprecated": false,
                      "description": "Duration of the game in seconds.\n`null` when the game status is not `finished`",
                      "minimum": 0,
                      "nullable": true,
                      "title": "GameLength",
                      "type": "integer"
                    },
                    "gold_earned": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLAverageGoldEarned",
                      "type": "number"
                    },
                    "herald_kill": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLAverageHeraldKills",
                      "type": "number"
                    },
                    "inhibitor_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLAverageInhibitorKills",
                      "type": "number"
                    },
                    "kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLAverageKills",
                      "type": "number"
                    },
                    "ratios": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "first_atakhan": {
                          "deprecated": false,
                          "description": "Whether the team killed the first Atakhan.",
                          "minimum": 0,
                          "nullable": true,
                          "title": "LoLTeamFirstAtakhanRatio",
                          "type": "number"
                        },
                        "first_baron": {
                          "deprecated": false,
                          "maximum": 1,
                          "minimum": 0,
                          "nullable": true,
                          "title": "LoLRatioFirstBaron",
                          "type": "number"
                        },
                        "first_blood": {
                          "deprecated": false,
                          "maximum": 1,
                          "minimum": 0,
                          "nullable": true,
                          "title": "LoLRatioFirstBlood",
                          "type": "number"
                        },
                        "first_dragon": {
                          "deprecated": false,
                          "maximum": 1,
                          "minimum": 0,
                          "nullable": true,
                          "title": "LoLRatioFirstDragon",
                          "type": "number"
                        },
                        "first_herald": {
                          "deprecated": false,
                          "maximum": 1,
                          "minimum": 0,
                          "nullable": true,
                          "title": "LoLRatioFirstHerald",
                          "type": "number"
                        },
                        "first_inhibitor": {
                          "deprecated": false,
                          "maximum": 1,
                          "minimum": 0,
                          "nullable": true,
                          "title": "LoLRatioFirstInhibitor",
                          "type": "number"
                        },
                        "first_tower": {
                          "deprecated": false,
                          "maximum": 1,
                          "minimum": 0,
                          "nullable": true,
                          "title": "LoLRatioFirstTower",
                          "type": "number"
                        },
                        "first_voidgrub": {
                          "deprecated": false,
                          "description": "Whether the team killed the first voidgrub.",
                          "minimum": 0,
                          "nullable": true,
                          "title": "LoLTeamFirstVoidgrubRatio",
                          "type": "number"
                        },
                        "win": {
                          "deprecated": false,
                          "maximum": 1,
                          "minimum": 0,
                          "nullable": true,
                          "title": "LoLRatioWin",
                          "type": "number"
                        }
                      },
                      "required": [
                        "first_atakhan",
                        "first_baron",
                        "first_blood",
                        "first_dragon",
                        "first_herald",
                        "first_inhibitor",
                        "first_tower",
                        "first_voidgrub",
                        "win"
                      ],
                      "title": "LoLTeamRatios",
                      "type": "object"
                    },
                    "total_minions_killed": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLAverageMinionsKilled",
                      "type": "number"
                    },
                    "tower_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLAverageTowerKills",
                      "type": "number"
                    },
                    "voidgrub_kills": {
                      "deprecated": false,
                      "description": "The number of voidgrubs killed by a team.",
                      "maximum": 6,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLTeamVoidgrubKillsAverage",
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
                    "atakhan_kills",
                    "baron_kills",
                    "deaths",
                    "dragon_kills",
                    "game_length",
                    "gold_earned",
                    "herald_kill",
                    "inhibitor_kills",
                    "kills",
                    "ratios",
                    "total_minions_killed",
                    "tower_kills",
                    "voidgrub_kills",
                    "wards_placed"
                  ],
                  "title": "LoLTeamAverages",
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
                "serie": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "description": "A serie, an occurrence of a league event",
                  "properties": {
                    "begin_at": {
                      "deprecated": false,
                      "format": "date-time",
                      "minLength": 1,
                      "nullable": true,
                      "title": "SerieBeginAt",
                      "type": "string"
                    },
                    "end_at": {
                      "deprecated": false,
                      "format": "date-time",
                      "minLength": 1,
                      "nullable": true,
                      "title": "SerieEndAt",
                      "type": "string"
                    },
                    "full_name": {
                      "title": "SerieFullName",
                      "type": "string"
                    },
                    "id": {
                      "minimum": 1,
                      "title": "SerieID",
                      "type": "integer"
                    },
                    "league": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "id": {
                          "minimum": 1,
                          "title": "LeagueID",
                          "type": "integer"
                        },
                        "image_url": {
                          "deprecated": false,
                          "format": "uri",
                          "nullable": true,
                          "title": "LeagueImageURL",
                          "type": "string"
                        },
                        "modified_at": {
                          "format": "date-time",
                          "minLength": 1,
                          "title": "LeagueModifiedAt",
                          "type": "string"
                        },
                        "name": {
                          "title": "LeagueName",
                          "type": "string"
                        },
                        "slug": {
                          "minLength": 1,
                          "pattern": "^[a-z0-9:_-]+$",
                          "title": "LeagueSlug",
                          "type": "string"
                        },
                        "url": {
                          "deprecated": false,
                          "format": "uri",
                          "nullable": true,
                          "title": "LeagueURL",
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "image_url",
                        "modified_at",
                        "name",
                        "slug",
                        "url"
                      ],
                      "title": "BaseLeague",
                      "type": "object"
                    },
                    "league_id": {
                      "minimum": 1,
                      "title": "LeagueID",
                      "type": "integer"
                    },
                    "modified_at": {
                      "format": "date-time",
                      "minLength": 1,
                      "title": "SerieModifiedAt",
                      "type": "string"
                    },
                    "name": {
                      "deprecated": false,
                      "nullable": true,
                      "title": "SerieName",
                      "type": "string"
                    },
                    "season": {
                      "deprecated": false,
                      "nullable": true,
                      "title": "SerieSeason",
                      "type": "string"
                    },
                    "slug": {
                      "minLength": 1,
                      "pattern": "^[a-z0-9_-]+$",
                      "title": "SerieSlug",
                      "type": "string"
                    },
                    "tournaments": {
                      "items": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "begin_at": {
                            "deprecated": false,
                            "format": "date-time",
                            "minLength": 1,
                            "nullable": true,
                            "title": "TournamentBeginAt",
                            "type": "string"
                          },
                          "country": {
                            "deprecated": false,
                            "description": "Country code matching the location of the tournament according to the ISO 3166-1 standard (Alpha-2 code). In addition to the standard, the XK code is used for Kosovo. null if unknown",
                            "nullable": true,
                            "title": "TournamentCountry",
                            "type": "string"
                          },
                          "detailed_stats": {
                            "description": "Whether the tournament is expected to have detailed statistics available",
                            "title": "TournamentDetailedStats",
                            "type": "boolean"
                          },
                          "end_at": {
                            "deprecated": false,
                            "format": "date-time",
                            "minLength": 1,
                            "nullable": true,
                            "title": "TournamentEndAt",
                            "type": "string"
                          },
                          "has_bracket": {
                            "description": "Whether the tournament has a bracket",
                            "title": "TournamentHasBracket",
                            "type": "boolean"
                          },
                          "id": {
                            "minimum": 1,
                            "title": "TournamentID",
                            "type": "integer"
                          },
                          "league_id": {
                            "minimum": 1,
                            "title": "LeagueID",
                            "type": "integer"
                          },
                          "live_supported": {
                            "description": "Whether live is supported",
                            "title": "TournamentLiveSupported",
                            "type": "boolean"
                          },
                          "modified_at": {
                            "format": "date-time",
                            "minLength": 1,
                            "title": "TournamentModifiedAt",
                            "type": "string"
                          },
                          "name": {
                            "title": "TournamentName",
                            "type": "string"
                          },
                          "prizepool": {
                            "deprecated": false,
                            "nullable": true,
                            "title": "TournamentPrizepool",
                            "type": "string"
                          },
                          "region": {
                            "deprecated": false,
                            "description": "Region acronym for the location of the tournament.",
                            "enum": [
                              "AF",
                              "ASIA",
                              "EEU",
                              "ME",
                              "NA",
                              "OCE",
                              "SA",
                              "WEU"
                            ],
                            "nullable": true,
                            "title": "TournamentRegion",
                            "type": "string"
                          },
                          "serie_id": {
                            "minimum": 1,
                            "title": "SerieID",
                            "type": "integer"
                          },
                          "slug": {
                            "minLength": 1,
                            "pattern": "^[a-z0-9_-]+$",
                            "title": "TournamentSlug",
                            "type": "string"
                          },
                          "tier": {
                            "deprecated": false,
                            "description": "The tier of the tournament, ranging from 'S' to 'Unranked'. Ranking 'S' > 'A' > 'B' > 'C' > 'D' > 'Unranked'",
                            "enum": [
                              "a",
                              "b",
                              "c",
                              "d",
                              "s",
                              "unranked"
                            ],
                            "nullable": true,
                            "title": "TournamentTier",
                            "type": "string"
                          },
                          "type": {
                            "deprecated": false,
                            "description": "Location type for a tournament",
                            "enum": [
                              "offline",
                              "online",
                              "online/offline"
                            ],
                            "nullable": true,
                            "title": "TournamentLocationType",
                            "type": "string"
                          },
                          "winner_id": {
                            "anyOf": [
                              {
                                "description": "ID of the player",
                                "minimum": 1,
                                "title": "PlayerID",
                                "type": "integer"
                              },
                              {
                                "description": "The ID of the team.",
                                "minimum": 1,
                                "title": "TeamID",
                                "type": "integer"
                              }
                            ],
                            "deprecated": false,
                            "nullable": true,
                            "title": "OpponentID"
                          },
                          "winner_type": {
                            "deprecated": false,
                            "enum": [
                              "Player",
                              "Team"
                            ],
                            "nullable": true,
                            "title": "OpponentType",
                            "type": "string"
                          }
                        },
                        "required": [
                          "begin_at",
                          "country",
                          "detailed_stats",
                          "end_at",
                          "has_bracket",
                          "id",
                          "league_id",
                          "live_supported",
                          "modified_at",
                          "name",
                          "prizepool",
                          "region",
                          "serie_id",
                          "slug",
                          "tier",
                          "type",
                          "winner_id",
                          "winner_type"
                        ],
                        "title": "BaseTournament",
                        "type": "object"
                      },
                      "title": "BaseTournaments",
                      "type": "array"
                    },
                    "videogame": {
                      "enum": [
                        {
                          "id": 1,
                          "name": "LoL",
                          "slug": "league-of-legends"
                        },
                        {
                          "id": 3,
                          "name": "Counter-Strike",
                          "slug": "cs-go"
                        },
                        {
                          "id": 4,
                          "name": "Dota 2",
                          "slug": "dota-2"
                        },
                        {
                          "id": 14,
                          "name": "Overwatch",
                          "slug": "ow"
                        },
                        {
                          "id": 20,
                          "name": "PUBG",
                          "slug": "pubg"
                        },
                        {
                          "id": 22,
                          "name": "Rocket League",
                          "slug": "rl"
                        },
                        {
                          "id": 23,
                          "name": "Call of Duty",
                          "slug": "cod-mw"
                        },
                        {
                          "id": 24,
                          "name": "Rainbow 6 Siege",
                          "slug": "r6-siege"
                        },
                        {
                          "id": 25,
                          "name": "EA Sports FC",
                          "slug": "fifa"
                        },
                        {
                          "id": 26,
                          "name": "Valorant",
                          "slug": "valorant"
                        },
                        {
                          "id": 27,
                          "name": "King of Glory",
                          "slug": "kog"
                        },
                        {
                          "id": 28,
                          "name": "LoL Wild Rift",
                          "slug": "lol-wild-rift"
                        },
                        {
                          "id": 29,
                          "name": "StarCraft 2",
                          "slug": "starcraft-2"
                        },
                        {
                          "id": 30,
                          "name": "StarCraft Brood War",
                          "slug": "starcraft-brood-war"
                        },
                        {
                          "id": 31,
                          "name": "eSoccer",
                          "slug": "e-soccer"
                        },
                        {
                          "id": 32,
                          "name": "eBasketball",
                          "slug": "e-basketball"
                        },
                        {
                          "id": 33,
                          "name": "eCricket",
                          "slug": "e-cricket"
                        },
                        {
                          "id": 34,
                          "name": "Mobile Legends: Bang Bang",
                          "slug": "mlbb"
                        },
                        {
                          "id": 35,
                          "name": "eHockey",
                          "slug": "e-hockey"
                        },
                        {
                          "id": 36,
                          "name": "eTennis",
                          "slug": "e-tennis"
                        }
                      ],
                      "title": "CurrentVideogame",
                      "type": "object"
                    },
                    "videogame_title": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "nullable": true,
                      "properties": {
                        "id": {
                          "minimum": 1,
                          "title": "VideogameTitleID",
                          "type": "integer"
                        },
                        "name": {
                          "title": "VideogameTitleName",
                          "type": "string"
                        },
                        "slug": {
                          "minLength": 1,
                          "pattern": "^[a-z0-9_-]+$",
                          "title": "VideogameTitleSlug",
                          "type": "string"
                        },
                        "videogame_id": {
                          "description": "A videogame ID",
                          "enum": [
                            1,
                            3,
                            4,
                            14,
                            20,
                            22,
                            23,
                            24,
                            25,
                            26,
                            27,
                            28,
                            29,
                            30,
                            31,
                            32,
                            33,
                            34,
                            35,
                            36
                          ],
                          "title": "VideogameID",
                          "type": "integer"
                        }
                      },
                      "required": [
                        "id",
                        "name",
                        "slug",
                        "videogame_id"
                      ],
                      "title": "VideogameTitle",
                      "type": "object"
                    },
                    "winner_id": {
                      "anyOf": [
                        {
                          "description": "ID of the player",
                          "minimum": 1,
                          "title": "PlayerID",
                          "type": "integer"
                        },
                        {
                          "description": "The ID of the team.",
                          "minimum": 1,
                          "title": "TeamID",
                          "type": "integer"
                        }
                      ],
                      "deprecated": false,
                      "nullable": true,
                      "title": "OpponentID"
                    },
                    "winner_type": {
                      "deprecated": false,
                      "enum": [
                        "Player",
                        "Team"
                      ],
                      "nullable": true,
                      "title": "OpponentType",
                      "type": "string"
                    },
                    "year": {
                      "deprecated": false,
                      "minimum": 2012,
                      "nullable": true,
                      "title": "SerieYear",
                      "type": "integer"
                    }
                  },
                  "required": [
                    "begin_at",
                    "end_at",
                    "full_name",
                    "id",
                    "league",
                    "league_id",
                    "modified_at",
                    "name",
                    "season",
                    "slug",
                    "tournaments",
                    "videogame",
                    "videogame_title",
                    "winner_id",
                    "winner_type",
                    "year"
                  ],
                  "title": "Serie",
                  "type": "object"
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
                    "atakhan_kills": {
                      "deprecated": false,
                      "description": "The number of Atakhan killed by a team.",
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLTeamAtakhanKillsTotal",
                      "type": "integer"
                    },
                    "baron_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLBaronKills",
                      "type": "integer"
                    },
                    "blue_games_lost": {
                      "deprecated": false,
                      "description": "Number of games",
                      "minimum": 0,
                      "nullable": true,
                      "title": "GameCount",
                      "type": "integer"
                    },
                    "blue_games_won": {
                      "deprecated": false,
                      "description": "Number of games",
                      "minimum": 0,
                      "nullable": true,
                      "title": "GameCount",
                      "type": "integer"
                    },
                    "chemtech_drake_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLChemtechDrakeKills",
                      "type": "integer"
                    },
                    "cloud_drake_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLCloudDrakeKills",
                      "type": "integer"
                    },
                    "deaths": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDeathCount",
                      "type": "integer"
                    },
                    "dragon_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDragonKills",
                      "type": "integer"
                    },
                    "elder_drake_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLElderDrakeKills",
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
                    "herald_kill": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLHeraldKills",
                      "type": "integer"
                    },
                    "hextech_drake_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLHextechDrakeKills",
                      "type": "integer"
                    },
                    "infernal_drake_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLInfernalDrakeKills",
                      "type": "integer"
                    },
                    "inhibitor_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLInhibitorKills",
                      "type": "integer"
                    },
                    "kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLKillCount",
                      "type": "integer"
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
                    "mountain_drake_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLMountainDrakeKills",
                      "type": "integer"
                    },
                    "ocean_drake_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLOceanDrakeKills",
                      "type": "integer"
                    },
                    "red_games_lost": {
                      "deprecated": false,
                      "description": "Number of games",
                      "minimum": 0,
                      "nullable": true,
                      "title": "GameCount",
                      "type": "integer"
                    },
                    "red_games_won": {
                      "deprecated": false,
                      "description": "Number of games",
                      "minimum": 0,
                      "nullable": true,
                      "title": "GameCount",
                      "type": "integer"
                    },
                    "tower_kills": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLTowerKills",
                      "type": "integer"
                    },
                    "voidgrub_kills": {
                      "deprecated": false,
                      "description": "The number of voidgrubs killed by a team.",
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLTeamVoidgrubKillsTotal",
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
                    "atakhan_kills",
                    "baron_kills",
                    "blue_games_lost",
                    "blue_games_won",
                    "chemtech_drake_kills",
                    "cloud_drake_kills",
                    "deaths",
                    "dragon_kills",
                    "elder_drake_kills",
                    "games_lost",
                    "games_played",
                    "games_won",
                    "herald_kill",
                    "hextech_drake_kills",
                    "infernal_drake_kills",
                    "inhibitor_kills",
                    "kills",
                    "matches_lost",
                    "matches_played",
                    "matches_won",
                    "mountain_drake_kills",
                    "ocean_drake_kills",
                    "red_games_lost",
                    "red_games_won",
                    "tower_kills",
                    "voidgrub_kills",
                    "wards_placed"
                  ],
                  "title": "LoLTeamStatsTotals",
                  "type": "object"
                }
              },
              "required": [
                "averages",
                "games_count",
                "serie",
                "totals"
              ],
              "title": "LoLTeamBySerieStat",
              "type": "object"
            },
            "title": "LoLTeamBySerieStats",
            "type": "array"
          },
          "total_stats": {
            "additionalProperties": false,
            "deprecated": false,
            "description": "Total Team's statistics",
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
                  "atakhan_kills": {
                    "deprecated": false,
                    "description": "The number of Atakhan killed by a team.",
                    "maximum": 1,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLTeamAtakhanKillsAverage",
                    "type": "number"
                  },
                  "baron_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageBaronKills",
                    "type": "number"
                  },
                  "deaths": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageDeaths",
                    "type": "number"
                  },
                  "dragon_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageDragonKills",
                    "type": "number"
                  },
                  "game_length": {
                    "deprecated": false,
                    "description": "Duration of the game in seconds.\n`null` when the game status is not `finished`",
                    "minimum": 0,
                    "nullable": true,
                    "title": "GameLength",
                    "type": "integer"
                  },
                  "gold_earned": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageGoldEarned",
                    "type": "number"
                  },
                  "herald_kill": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageHeraldKills",
                    "type": "number"
                  },
                  "inhibitor_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageInhibitorKills",
                    "type": "number"
                  },
                  "kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageKills",
                    "type": "number"
                  },
                  "ratios": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "first_atakhan": {
                        "deprecated": false,
                        "description": "Whether the team killed the first Atakhan.",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLTeamFirstAtakhanRatio",
                        "type": "number"
                      },
                      "first_baron": {
                        "deprecated": false,
                        "maximum": 1,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLRatioFirstBaron",
                        "type": "number"
                      },
                      "first_blood": {
                        "deprecated": false,
                        "maximum": 1,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLRatioFirstBlood",
                        "type": "number"
                      },
                      "first_dragon": {
                        "deprecated": false,
                        "maximum": 1,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLRatioFirstDragon",
                        "type": "number"
                      },
                      "first_herald": {
                        "deprecated": false,
                        "maximum": 1,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLRatioFirstHerald",
                        "type": "number"
                      },
                      "first_inhibitor": {
                        "deprecated": false,
                        "maximum": 1,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLRatioFirstInhibitor",
                        "type": "number"
                      },
                      "first_tower": {
                        "deprecated": false,
                        "maximum": 1,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLRatioFirstTower",
                        "type": "number"
                      },
                      "first_voidgrub": {
                        "deprecated": false,
                        "description": "Whether the team killed the first voidgrub.",
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLTeamFirstVoidgrubRatio",
                        "type": "number"
                      },
                      "win": {
                        "deprecated": false,
                        "maximum": 1,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLRatioWin",
                        "type": "number"
                      }
                    },
                    "required": [
                      "first_atakhan",
                      "first_baron",
                      "first_blood",
                      "first_dragon",
                      "first_herald",
                      "first_inhibitor",
                      "first_tower",
                      "first_voidgrub",
                      "win"
                    ],
                    "title": "LoLTeamRatios",
                    "type": "object"
                  },
                  "total_minions_killed": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageMinionsKilled",
                    "type": "number"
                  },
                  "tower_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageTowerKills",
                    "type": "number"
                  },
                  "voidgrub_kills": {
                    "deprecated": false,
                    "description": "The number of voidgrubs killed by a team.",
                    "maximum": 6,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLTeamVoidgrubKillsAverage",
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
                  "atakhan_kills",
                  "baron_kills",
                  "deaths",
                  "dragon_kills",
                  "game_length",
                  "gold_earned",
                  "herald_kill",
                  "inhibitor_kills",
                  "kills",
                  "ratios",
                  "total_minions_killed",
                  "tower_kills",
                  "voidgrub_kills",
                  "wards_placed"
                ],
                "title": "LoLTeamAverages",
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
                  "atakhan_kills": {
                    "deprecated": false,
                    "description": "The number of Atakhan killed by a team.",
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLTeamAtakhanKillsTotal",
                    "type": "integer"
                  },
                  "baron_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLBaronKills",
                    "type": "integer"
                  },
                  "blue_games_lost": {
                    "deprecated": false,
                    "description": "Number of games",
                    "minimum": 0,
                    "nullable": true,
                    "title": "GameCount",
                    "type": "integer"
                  },
                  "blue_games_won": {
                    "deprecated": false,
                    "description": "Number of games",
                    "minimum": 0,
                    "nullable": true,
                    "title": "GameCount",
                    "type": "integer"
                  },
                  "chemtech_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLChemtechDrakeKills",
                    "type": "integer"
                  },
                  "cloud_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLCloudDrakeKills",
                    "type": "integer"
                  },
                  "deaths": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLDeathCount",
                    "type": "integer"
                  },
                  "dragon_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLDragonKills",
                    "type": "integer"
                  },
                  "elder_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLElderDrakeKills",
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
                  "herald_kill": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLHeraldKills",
                    "type": "integer"
                  },
                  "hextech_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLHextechDrakeKills",
                    "type": "integer"
                  },
                  "infernal_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLInfernalDrakeKills",
                    "type": "integer"
                  },
                  "inhibitor_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLInhibitorKills",
                    "type": "integer"
                  },
                  "kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLKillCount",
                    "type": "integer"
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
                  "mountain_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLMountainDrakeKills",
                    "type": "integer"
                  },
                  "ocean_drake_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLOceanDrakeKills",
                    "type": "integer"
                  },
                  "red_games_lost": {
                    "deprecated": false,
                    "description": "Number of games",
                    "minimum": 0,
                    "nullable": true,
                    "title": "GameCount",
                    "type": "integer"
                  },
                  "red_games_won": {
                    "deprecated": false,
                    "description": "Number of games",
                    "minimum": 0,
                    "nullable": true,
                    "title": "GameCount",
                    "type": "integer"
                  },
                  "tower_kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLTowerKills",
                    "type": "integer"
                  },
                  "voidgrub_kills": {
                    "deprecated": false,
                    "description": "The number of voidgrubs killed by a team.",
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLTeamVoidgrubKillsTotal",
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
                  "atakhan_kills",
                  "baron_kills",
                  "blue_games_lost",
                  "blue_games_won",
                  "chemtech_drake_kills",
                  "cloud_drake_kills",
                  "deaths",
                  "dragon_kills",
                  "elder_drake_kills",
                  "games_lost",
                  "games_played",
                  "games_won",
                  "herald_kill",
                  "hextech_drake_kills",
                  "infernal_drake_kills",
                  "inhibitor_kills",
                  "kills",
                  "matches_lost",
                  "matches_played",
                  "matches_won",
                  "mountain_drake_kills",
                  "ocean_drake_kills",
                  "red_games_lost",
                  "red_games_won",
                  "tower_kills",
                  "voidgrub_kills",
                  "wards_placed"
                ],
                "title": "LoLTeamStatsTotals",
                "type": "object"
              }
            },
            "required": [
              "averages",
              "games_count",
              "totals"
            ],
            "title": "LoLTotalTeamStat",
            "type": "object"
          }
        },
        "required": [
          "acronym",
          "dark_mode_image_url",
          "id",
          "image_url",
          "last_games",
          "location",
          "modified_at",
          "most_banned",
          "most_banned_against",
          "most_picked",
          "name",
          "players",
          "slug",
          "stats",
          "total_stats"
        ],
        "title": "LoLStatsForTeam",
        "type": "object"
      },
      "TeamIDOrSlug": {
        "description": "A team ID or slug",
        "oneOf": [
          {
            "description": "The ID of the team.",
            "minimum": 1,
            "title": "TeamID",
            "type": "integer"
          },
          {
            "minLength": 1,
            "pattern": "^[a-z0-9_-]+$",
            "title": "TeamSlug",
            "type": "string"
          }
        ],
        "title": "TeamIDOrSlug"
      },
      "VideogameVersionOrAll": {
        "description": "Possible values are `latest`, `all` or a specific version number.",
        "oneOf": [
          {
            "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
            "title": "VideogameVersion",
            "type": "string"
          },
          {
            "enum": [
              "all"
            ]
          },
          {
            "enum": [
              "latest"
            ]
          }
        ],
        "title": "VideogameVersionOrAll"
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
    "/lol/teams/{team_id_or_slug}/stats": {
      "get": {
        "description": "Get detailed statistics of a given League-of-Legends team\n> ℹ️  \n> \n> This endpoint is only available to customers with a historical or real-time data plan",
        "operationId": "get_lol_teams_teamIdOrSlug_stats",
        "parameters": [
          {
            "description": "A team ID or slug",
            "in": "path",
            "name": "team_id_or_slug",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/TeamIDOrSlug"
            }
          },
          {
            "$ref": "#/components/parameters/GamesCount"
          },
          {
            "$ref": "#/components/parameters/LoLStatsSide"
          },
          {
            "$ref": "#/components/parameters/StatsVideogameVersion"
          },
          {
            "$ref": "#/components/parameters/StatsFrom"
          },
          {
            "$ref": "#/components/parameters/StatsTo"
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLStatsForTeam"
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
        "summary": "Get stats for LoL team",
        "tags": [
          "LoL stats"
        ],
        "x-pandascore-plan": "Historical plan",
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/teams/{team_id_or_slug}/stats' \\\n     --header 'accept: application/json'\n",
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