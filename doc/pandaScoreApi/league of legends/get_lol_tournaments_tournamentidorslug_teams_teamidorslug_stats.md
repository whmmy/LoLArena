> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get stats for LoL team on tournament

Get detailed statistics of a given League-of-Legends team for the given tournament
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
      "LoLStatsForTeamByTournament": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/tournaments/9049/teams/126061/stats": {
                "description": "/lol/tournaments/9049/teams/126061/stats",
                "value": {
                  "acronym": "T1",
                  "dark_mode_image_url": null,
                  "id": 126061,
                  "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                  "last_games": [
                    {
                      "begin_at": "2022-11-06T04:36:27Z",
                      "complete": true,
                      "detailed_stats": true,
                      "end_at": "2022-11-06T05:25:24Z",
                      "finished": true,
                      "forfeit": false,
                      "id": 239290,
                      "length": 2529,
                      "match_id": 651268,
                      "players": [
                        {
                          "assists": 4,
                          "champion": {
                            "id": 3121,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/1a602e7dc475be3ca9ccba41689c71d3.png",
                            "name": "Viktor",
                            "slug": "Viktor"
                          },
                          "creep_score": 325,
                          "cs_at_14": 124,
                          "cs_diff_at_14": 6,
                          "deaths": 5,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239290,
                          "gold_earned": 15380,
                          "gold_percentage": 21.34,
                          "gold_spent": 14925,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2872,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/28a5336738db9b68b288d7796243eb33.png",
                              "is_trinket": false,
                              "name": "Luden's Tempest"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2923,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f0afeb951bcd89aa997e963f075bae83.png",
                              "is_trinket": false,
                              "name": "Lich Bane"
                            },
                            {
                              "id": 3048,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/e8bca3b0-24da-479e-9fa7-13f2021cc106.png",
                              "is_trinket": false,
                              "name": "Zhonya's Hourglass"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 24,
                            "neutral_minions_enemy_jungle": 2,
                            "neutral_minions_team_jungle": 21,
                            "players": 2,
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
                          "largest_multi_kill": 1,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 236647,
                            "dealt_percentage": 52.57,
                            "dealt_to_champions": 21696,
                            "dealt_to_champions_percentage": 40.48,
                            "taken": 10507
                          },
                          "masteries": [],
                          "minions_killed": 325,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 12520,
                            "dealt_percentage": 2.49,
                            "dealt_to_champions": 474,
                            "dealt_to_champions_percentage": 1.12,
                            "taken": 8535
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-05-07",
                            "first_name": "Lee",
                            "id": 585,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                            "last_name": "Sang-hyeok",
                            "modified_at": "2026-02-01T11:19:16Z",
                            "name": "Faker",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "faker"
                          },
                          "player_id": 585,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 52,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fbe3405d6a68d3b7ae3f305fdf129e99.png",
                                "name": "Summon Aery",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 56,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                  "name": "Manaflow Band",
                                  "type": "slot1"
                                },
                                {
                                  "id": 58,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/632a47c2a88802029838e383a866feb1.png",
                                  "name": "Transcendence",
                                  "type": "slot2"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 45,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/592200e1a39d2281977fc92d788cacd1.png",
                                  "name": "Shield Bash",
                                  "type": "slot1"
                                },
                                {
                                  "id": 48,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6054dc49089750c7d576b8e157228f29.png",
                                  "name": "Bone Plating",
                                  "type": "slot2"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 266474,
                            "dealt_percentage": 24.87,
                            "dealt_to_champions": 22454,
                            "dealt_to_champions_percentage": 21.46,
                            "taken": 20289
                          },
                          "total_heal": 1294,
                          "total_time_crowd_control_dealt": 473,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 17307,
                            "dealt_percentage": 14.51,
                            "dealt_to_champions": 284,
                            "dealt_to_champions_percentage": 3.23,
                            "taken": 1246
                          },
                          "wards": {
                            "placed": 21,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 14
                          },
                          "wards_placed": 21
                        },
                        {
                          "assists": 4,
                          "champion": {
                            "id": 3156,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/6bbdffa9-d868-4fc9-b697-7ed6bcb1c79c.png",
                            "name": "Caitlyn",
                            "slug": "Caitlyn"
                          },
                          "creep_score": 388,
                          "cs_at_14": 109,
                          "cs_diff_at_14": -22,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239290,
                          "gold_earned": 17575,
                          "gold_percentage": 23.53,
                          "gold_spent": 16930,
                          "items": [
                            {
                              "id": 2494,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/fcd28e708879aa54037da3539604b1c4.png",
                              "is_trinket": false,
                              "name": "Infinity Edge"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2714,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/2e9e74676892b4fbaf86c33e959bf373.png",
                              "is_trinket": false,
                              "name": "Rapid Firecannon"
                            },
                            {
                              "id": 2727,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6c611c3082d7c565a4e4ba63d3255c10.png",
                              "is_trinket": false,
                              "name": "Galeforce"
                            },
                            {
                              "id": 2866,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/9fe203b01a6b9ae1849a8d0d65d4b48b.png",
                              "is_trinket": false,
                              "name": "Bloodthirster"
                            }
                          ],
                          "kills": 5,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 37,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 37,
                            "players": 5,
                            "turrets": 2,
                            "wards": 15
                          },
                          "kills_series": {
                            "double_kills": 2,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 1658,
                          "largest_killing_spree": 5,
                          "largest_multi_kill": 2,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 8834,
                            "dealt_percentage": 2.12,
                            "dealt_to_champions": 1526,
                            "dealt_to_champions_percentage": 4.79,
                            "taken": 7759
                          },
                          "masteries": [],
                          "minions_killed": 388,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 336112,
                            "dealt_percentage": 49.06,
                            "dealt_to_champions": 16676,
                            "dealt_to_champions_percentage": 33.01,
                            "taken": 13878
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-10-23",
                            "first_name": "Kim",
                            "id": 2169,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/2169/ezgif_3_4d5729796f.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 29,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d7dee9f79afc995429521e2b586aae87.png",
                                "name": "Fleet Footwork",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 33,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                                  "name": "Presence of Mind",
                                  "type": "slot1"
                                },
                                {
                                  "id": 36,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/078fa7db48ed5384e9933f535f0b986a.png",
                                  "name": "Legend: Bloodline",
                                  "type": "slot2"
                                },
                                {
                                  "id": 38,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/08f4edce2a6f85edbfea701c04314cb9.png",
                                  "name": "Cut Down",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "lesser_runes": [
                                {
                                  "id": 60,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/0103e35a695d637b86f7d6344653009b.png",
                                  "name": "Absolute Focus",
                                  "type": "slot2"
                                },
                                {
                                  "id": 63,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aef96161f07e6b0049dd0f69dc214d67.png",
                                  "name": "Gathering Storm",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 23,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/65eea722a1fc79fb6469e7246eb0afb8.png",
                              "name": "Cleanse"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 351509,
                            "dealt_percentage": 30.81,
                            "dealt_to_champions": 19286,
                            "dealt_to_champions_percentage": 21.93,
                            "taken": 22208
                          },
                          "total_heal": 5462,
                          "total_time_crowd_control_dealt": 76,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 6563,
                            "dealt_percentage": 16.54,
                            "dealt_to_champions": 1083,
                            "dealt_to_champions_percentage": 19.33,
                            "taken": 570
                          },
                          "wards": {
                            "placed": 22,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 6
                          },
                          "wards_placed": 22
                        },
                        {
                          "assists": 3,
                          "champion": {
                            "id": 3032,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/cee9e33f3ea3f3b989bcbb342730e231.png",
                            "name": "Karma",
                            "slug": "Karma"
                          },
                          "creep_score": 35,
                          "cs_at_14": 14,
                          "cs_diff_at_14": 3,
                          "deaths": 5,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": true,
                            "first_tower_kill": false
                          },
                          "game_id": 239290,
                          "gold_earned": 10124,
                          "gold_percentage": 14.05,
                          "gold_spent": 10575,
                          "items": [
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2761,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b4754269-dc0f-474a-a3b4-c181b7d6d26c.png",
                              "is_trinket": false,
                              "name": "Shurelya's Battlesong"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2864,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6ef4210b083c4e72497f10bb95ecf5ba.png",
                              "is_trinket": false,
                              "name": "Vigilant Wardstone"
                            },
                            {
                              "id": 3007,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a53f4c97c8d30ad58cb978e397107463.png",
                              "is_trinket": false,
                              "name": "Chemtech Putrifier"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 0,
                            "players": 1,
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
                          "largest_multi_kill": 1,
                          "level": 13,
                          "magic_damage": {
                            "dealt": 39465,
                            "dealt_percentage": 8.77,
                            "dealt_to_champions": 9308,
                            "dealt_to_champions_percentage": 17.37,
                            "taken": 5943
                          },
                          "masteries": [],
                          "minions_killed": 35,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 4651,
                            "dealt_percentage": 0.93,
                            "dealt_to_champions": 496,
                            "dealt_to_champions_percentage": 1.17,
                            "taken": 8762
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-10-14",
                            "first_name": "Ryu",
                            "id": 8158,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                            "last_name": "Min-seok",
                            "modified_at": "2026-02-01T11:19:16Z",
                            "name": "Keria",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "keria"
                          },
                          "player_id": 8158,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 53,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/b8282c680e5d022dc564c54937a20a26.png",
                                "name": "Arcane Comet",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 57,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/59ba46a95f8b51739d4eb2179654cf7e.png",
                                  "name": "Nimbus Cloak",
                                  "type": "slot1"
                                },
                                {
                                  "id": 60,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/0103e35a695d637b86f7d6344653009b.png",
                                  "name": "Absolute Focus",
                                  "type": "slot2"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                },
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 45162,
                            "dealt_percentage": 4.22,
                            "dealt_to_champions": 10850,
                            "dealt_to_champions_percentage": 10.37,
                            "taken": 15192
                          },
                          "total_heal": 863,
                          "total_time_crowd_control_dealt": 224,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 1045,
                            "dealt_percentage": 0.88,
                            "dealt_to_champions": 1045,
                            "dealt_to_champions_percentage": 11.88,
                            "taken": 486
                          },
                          "wards": {
                            "placed": 75,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 25
                          },
                          "wards_placed": 75
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 3166,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/cad8d209-bda9-43f3-a7fa-cebce483ec37.png",
                            "name": "Aatrox",
                            "slug": "Aatrox"
                          },
                          "creep_score": 269,
                          "cs_at_14": 116,
                          "cs_diff_at_14": 14,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239290,
                          "gold_earned": 15346,
                          "gold_percentage": 20.54,
                          "gold_spent": 13600,
                          "items": [
                            {
                              "id": 2465,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/167abf5d0dc59292a78b79ceadffcc99.png",
                              "is_trinket": false,
                              "name": "Negatron Cloak"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2912,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/eaef5f4c2f6f2d5fcf13f287c321e59b.png",
                              "is_trinket": false,
                              "name": "Eclipse"
                            },
                            {
                              "id": 2933,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/9eb16adb98fcdc9c9ae35eabe19c322f.png",
                              "is_trinket": false,
                              "name": "Maw of Malmortius"
                            },
                            {
                              "id": 2934,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6f38d2d2845b0958a9cf0c03b8d592a2.png",
                              "is_trinket": false,
                              "name": "Death's Dance"
                            }
                          ],
                          "kills": 6,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 27,
                            "neutral_minions_enemy_jungle": 4,
                            "neutral_minions_team_jungle": 18,
                            "players": 6,
                            "turrets": 1,
                            "wards": 18
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
                            "dealt": 0,
                            "dealt_percentage": 0,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 15013
                          },
                          "masteries": [],
                          "minions_killed": 269,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 218137,
                            "dealt_percentage": 31.84,
                            "dealt_to_champions": 26129,
                            "dealt_to_champions_percentage": 51.73,
                            "taken": 18933
                          },
                          "player": {
                            "active": true,
                            "age": 26,
                            "birthday": "2000-03-11",
                            "first_name": "Hwang",
                            "id": 8172,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/8172/drx_kingen_2022_split_2.png",
                            "last_name": "Seong-hoon",
                            "modified_at": "2026-02-01T11:16:32Z",
                            "name": "Kingen",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "kingen"
                          },
                          "player_id": 8172,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 49,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
                                  "name": "Overgrowth",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 223503,
                            "dealt_percentage": 19.59,
                            "dealt_to_champions": 27393,
                            "dealt_to_champions_percentage": 31.14,
                            "taken": 40472
                          },
                          "total_heal": 21444,
                          "total_time_crowd_control_dealt": 189,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 5366,
                            "dealt_percentage": 13.52,
                            "dealt_to_champions": 1263,
                            "dealt_to_champions_percentage": 22.54,
                            "taken": 6525
                          },
                          "wards": {
                            "placed": 15,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 12
                          },
                          "wards_placed": 15
                        },
                        {
                          "assists": 10,
                          "champion": {
                            "id": 2992,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/7e4bfdcbf84e00a47c9b59ad065178b1.png",
                            "name": "Bard",
                            "slug": "Bard"
                          },
                          "creep_score": 47,
                          "cs_at_14": 11,
                          "cs_diff_at_14": -3,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239290,
                          "gold_earned": 9449,
                          "gold_percentage": 12.65,
                          "gold_spent": 8475,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2533,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/63ed6bad74e3d767c48590a30eb3d016.png",
                              "is_trinket": false,
                              "name": "Redemption"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2761,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b4754269-dc0f-474a-a3b4-c181b7d6d26c.png",
                              "is_trinket": false,
                              "name": "Shurelya's Battlesong"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 1,
                            "players": 0,
                            "turrets": 0,
                            "wards": 27
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
                            "dealt": 27756,
                            "dealt_percentage": 6.67,
                            "dealt_to_champions": 4166,
                            "dealt_to_champions_percentage": 13.08,
                            "taken": 11004
                          },
                          "masteries": [],
                          "minions_killed": 47,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 5524,
                            "dealt_percentage": 0.81,
                            "dealt_to_champions": 732,
                            "dealt_to_champions_percentage": 1.45,
                            "taken": 10219
                          },
                          "player": {
                            "active": true,
                            "age": 28,
                            "birthday": "1997-04-01",
                            "first_name": "Cho",
                            "id": 15425,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/15425/drx_bery_l_2022_split_2.png",
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
                            "primary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "keystone": {
                                "id": 42,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ded20bb65d8b80ffaf6408be45136628.png",
                                "name": "Guardian",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 44,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/2763ad2665464bf7e9ff63ab7669b521.png",
                                  "name": "Font of Life",
                                  "type": "slot1"
                                },
                                {
                                  "id": 48,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6054dc49089750c7d576b8e157228f29.png",
                                  "name": "Bone Plating",
                                  "type": "slot2"
                                },
                                {
                                  "id": 51,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                                  "name": "Unflinching",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 1,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                              "lesser_runes": [
                                {
                                  "id": 13,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/623d21bc9acd874af4f1c2150bdd7150.png",
                                  "name": "Relentless Hunter",
                                  "type": "slot3"
                                },
                                {
                                  "id": 8,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a5317349f8ce3e0923fe970e5232bf30.png",
                                  "name": "Zombie Ward",
                                  "type": "slot2"
                                }
                              ],
                              "name": "Domination",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 36058,
                            "dealt_percentage": 3.16,
                            "dealt_to_champions": 5520,
                            "dealt_to_champions_percentage": 6.28,
                            "taken": 21875
                          },
                          "total_heal": 14408,
                          "total_time_crowd_control_dealt": 194,
                          "total_units_healed": 5,
                          "true_damage": {
                            "dealt": 2777,
                            "dealt_percentage": 7,
                            "dealt_to_champions": 622,
                            "dealt_to_champions_percentage": 11.1,
                            "taken": 651
                          },
                          "wards": {
                            "placed": 116,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 27
                          },
                          "wards_placed": 116
                        },
                        {
                          "assists": 3,
                          "champion": {
                            "id": 3177,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/bf77b476-a4b2-4433-a896-13d082b51644.png",
                            "name": "Varus",
                            "slug": "Varus"
                          },
                          "creep_score": 356,
                          "cs_at_14": 131,
                          "cs_diff_at_14": 22,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239290,
                          "gold_earned": 16301,
                          "gold_percentage": 22.62,
                          "gold_spent": 15425,
                          "items": [
                            {
                              "id": 2489,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/7c39a6acc5d50b697a09e78338c3d4a0.png",
                              "is_trinket": false,
                              "name": "Boots of Swiftness"
                            },
                            {
                              "id": 2546,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/5b6921f24dd78c4ad534fd550f13a703.png",
                              "is_trinket": false,
                              "name": "Serrated Dirk"
                            },
                            {
                              "id": 2580,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/8017be65dd3b762a53bf8f5efbb4eaef.png",
                              "is_trinket": false,
                              "name": "Edge of Night"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2811,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/28719589de63ed2332d29dd334b368e0.png",
                              "is_trinket": false,
                              "name": "Muramana"
                            },
                            {
                              "id": 2825,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3a6f184fabcf0b060a35cfe67ac8a530.png",
                              "is_trinket": false,
                              "name": "Serylda's Grudge"
                            },
                            {
                              "id": 2912,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/eaef5f4c2f6f2d5fcf13f287c321e59b.png",
                              "is_trinket": false,
                              "name": "Eclipse"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 32,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 24,
                            "players": 1,
                            "turrets": 3,
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
                            "dealt": 13490,
                            "dealt_percentage": 3,
                            "dealt_to_champions": 2608,
                            "dealt_to_champions_percentage": 4.87,
                            "taken": 2255
                          },
                          "masteries": [],
                          "minions_killed": 356,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 249893,
                            "dealt_percentage": 49.79,
                            "dealt_to_champions": 23033,
                            "dealt_to_champions_percentage": 54.51,
                            "taken": 8664
                          },
                          "player": {
                            "active": true,
                            "age": 24,
                            "birthday": "2002-02-06",
                            "first_name": "Lee",
                            "id": 19285,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/19285/t1_gumayusi_2023_split_2.png",
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
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 53,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/b8282c680e5d022dc564c54937a20a26.png",
                                "name": "Arcane Comet",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 56,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                  "name": "Manaflow Band",
                                  "type": "slot1"
                                },
                                {
                                  "id": 58,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/632a47c2a88802029838e383a866feb1.png",
                                  "name": "Transcendence",
                                  "type": "slot2"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 264077,
                            "dealt_percentage": 24.65,
                            "dealt_to_champions": 25818,
                            "dealt_to_champions_percentage": 24.67,
                            "taken": 12202
                          },
                          "total_heal": 3036,
                          "total_time_crowd_control_dealt": 481,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 692,
                            "dealt_percentage": 0.58,
                            "dealt_to_champions": 176,
                            "dealt_to_champions_percentage": 2,
                            "taken": 1282
                          },
                          "wards": {
                            "placed": 24,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 9
                          },
                          "wards_placed": 24
                        },
                        {
                          "assists": 8,
                          "champion": {
                            "id": 3187,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/2430fcbc-2dfd-4aa5-b7b7-c9eb2cc8d55d.png",
                            "name": "Hecarim",
                            "slug": "Hecarim"
                          },
                          "creep_score": 192,
                          "cs_at_14": 92,
                          "cs_diff_at_14": 1,
                          "deaths": 4,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239290,
                          "gold_earned": 13765,
                          "gold_percentage": 18.43,
                          "gold_spent": 12350,
                          "items": [
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2688,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c38d52b6bb9b984bf353c56585dae43d.png",
                              "is_trinket": false,
                              "name": "Force of Nature"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2881,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1e0b1c90b92e68856c4c8623b98cc24f.png",
                              "is_trinket": false,
                              "name": "Dead Man's Plate"
                            },
                            {
                              "id": 3020,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/49ca044dd30a7b6495d9b99f699e20ec.png",
                              "is_trinket": false,
                              "name": "Turbo Chemtank"
                            },
                            {
                              "id": 3044,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d0e13016-50c3-4bf8-926c-a502cced78c4.png",
                              "is_trinket": false,
                              "name": "Broken Stopwatch"
                            }
                          ],
                          "kills": 5,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 163,
                            "neutral_minions_enemy_jungle": 9,
                            "neutral_minions_team_jungle": 104,
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
                          "largest_killing_spree": 3,
                          "largest_multi_kill": 2,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 52920,
                            "dealt_percentage": 12.72,
                            "dealt_to_champions": 3842,
                            "dealt_to_champions_percentage": 12.07,
                            "taken": 16125
                          },
                          "masteries": [],
                          "minions_killed": 192,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 107257,
                            "dealt_percentage": 15.66,
                            "dealt_to_champions": 6709,
                            "dealt_to_champions_percentage": 13.28,
                            "taken": 22696
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-03-21",
                            "first_name": "Hong",
                            "id": 24996,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/24996/tl_pyosik_2023_split_1.png",
                            "last_name": "Chang-hyeon",
                            "modified_at": "2026-02-08T13:14:45Z",
                            "name": "Pyosik",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "pyosik"
                          },
                          "player_id": 24996,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 54,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4ee4739ae4a9cbf7be59650f92009edc.png",
                                "name": "Phase Rush",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 57,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/59ba46a95f8b51739d4eb2179654cf7e.png",
                                  "name": "Nimbus Cloak",
                                  "type": "slot1"
                                },
                                {
                                  "id": 59,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/732d4e2a7fdf6ecc3ec8e42504a111b9.png",
                                  "name": "Celerity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 62,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/abb0332095ac959dacaa1ed0ad4ad5e2.png",
                                  "name": "Waterwalking",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 35,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                                  "name": "Legend: Tenacity",
                                  "type": "slot2"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 29,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/58955cb861c3b51375948a05e260996a.png",
                              "name": "Ghost"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 183257,
                            "dealt_percentage": 16.06,
                            "dealt_to_champions": 12378,
                            "dealt_to_champions_percentage": 14.07,
                            "taken": 40180
                          },
                          "total_heal": 19270,
                          "total_time_crowd_control_dealt": 223,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 23080,
                            "dealt_percentage": 58.15,
                            "dealt_to_champions": 1826,
                            "dealt_to_champions_percentage": 32.58,
                            "taken": 1358
                          },
                          "wards": {
                            "placed": 21,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 21
                          },
                          "wards_placed": 21
                        },
                        {
                          "assists": 9,
                          "champion": {
                            "id": 2991,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/baf32ee97457437ea20c42ba23003e0c.png",
                            "name": "Azir",
                            "slug": "Azir"
                          },
                          "creep_score": 387,
                          "cs_at_14": 118,
                          "cs_diff_at_14": -6,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239290,
                          "gold_earned": 18568,
                          "gold_percentage": 24.86,
                          "gold_spent": 16150,
                          "items": [
                            {
                              "id": 2651,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2774,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/19d538db18a40b62822d7ca7ab1de27a.png",
                              "is_trinket": false,
                              "name": "Banshee's Veil"
                            },
                            {
                              "id": 2814,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                              "is_trinket": false,
                              "name": "Rabadon's Deathcap"
                            },
                            {
                              "id": 2872,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/28a5336738db9b68b288d7796243eb33.png",
                              "is_trinket": false,
                              "name": "Luden's Tempest"
                            },
                            {
                              "id": 2909,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/7ec8f413ab83b109852d5c3fd7c5b197.png",
                              "is_trinket": false,
                              "name": "Shadowflame"
                            },
                            {
                              "id": 3043,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3c9dee81-cfff-4920-87ad-e0516ac0fc92.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            }
                          ],
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 29,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 30,
                            "players": 3,
                            "turrets": 5,
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
                          "level": 18,
                          "magic_damage": {
                            "dealt": 326572,
                            "dealt_percentage": 78.49,
                            "dealt_to_champions": 22308,
                            "dealt_to_champions_percentage": 70.06,
                            "taken": 7886
                          },
                          "masteries": [],
                          "minions_killed": 387,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 18062,
                            "dealt_percentage": 2.64,
                            "dealt_to_champions": 267,
                            "dealt_to_champions_percentage": 0.53,
                            "taken": 7584
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-11-28",
                            "first_name": "Kim",
                            "id": 25391,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/25391/drx_zeka_2022_split_2.png",
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
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 53,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/b8282c680e5d022dc564c54937a20a26.png",
                                "name": "Arcane Comet",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 56,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                  "name": "Manaflow Band",
                                  "type": "slot1"
                                },
                                {
                                  "id": 58,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/632a47c2a88802029838e383a866feb1.png",
                                  "name": "Transcendence",
                                  "type": "slot2"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 346540,
                            "dealt_percentage": 30.38,
                            "dealt_to_champions": 23386,
                            "dealt_to_champions_percentage": 26.59,
                            "taken": 15604
                          },
                          "total_heal": 2981,
                          "total_time_crowd_control_dealt": 312,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 1905,
                            "dealt_percentage": 4.8,
                            "dealt_to_champions": 810,
                            "dealt_to_champions_percentage": 14.45,
                            "taken": 133
                          },
                          "wards": {
                            "placed": 23,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 11
                          },
                          "wards_placed": 23
                        },
                        {
                          "assists": 3,
                          "champion": {
                            "id": 3169,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/e5b2f71c-b353-4968-821f-77b3eed453dd.png",
                            "name": "Gwen",
                            "slug": "Gwen"
                          },
                          "creep_score": 292,
                          "cs_at_14": 102,
                          "cs_diff_at_14": -14,
                          "deaths": 4,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239290,
                          "gold_earned": 15552,
                          "gold_percentage": 21.58,
                          "gold_spent": 15325,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2814,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                              "is_trinket": false,
                              "name": "Rabadon's Deathcap"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2909,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/7ec8f413ab83b109852d5c3fd7c5b197.png",
                              "is_trinket": false,
                              "name": "Shadowflame"
                            },
                            {
                              "id": 3017,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/81cd1acbc7ee06bec32014055901b37e.png",
                              "is_trinket": false,
                              "name": "Riftmaker"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 37,
                            "neutral_minions_enemy_jungle": 1,
                            "neutral_minions_team_jungle": 21,
                            "players": 4,
                            "turrets": 3,
                            "wards": 17
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
                            "dealt": 144740,
                            "dealt_percentage": 32.15,
                            "dealt_to_champions": 18611,
                            "dealt_to_champions_percentage": 34.72,
                            "taken": 7447
                          },
                          "masteries": [],
                          "minions_killed": 292,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 49849,
                            "dealt_percentage": 9.93,
                            "dealt_to_champions": 2756,
                            "dealt_to_champions_percentage": 6.52,
                            "taken": 26667
                          },
                          "player": {
                            "active": true,
                            "age": 22,
                            "birthday": "2004-01-31",
                            "first_name": "Choi",
                            "id": 31391,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31391/t1_zeus_2023_split_2.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 33,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                                  "name": "Presence of Mind",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 51,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                                  "name": "Unflinching",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 29,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/58955cb861c3b51375948a05e260996a.png",
                              "name": "Ghost"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 279878,
                            "dealt_percentage": 26.12,
                            "dealt_to_champions": 27484,
                            "dealt_to_champions_percentage": 26.26,
                            "taken": 36130
                          },
                          "total_heal": 12842,
                          "total_time_crowd_control_dealt": 93,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 85287,
                            "dealt_percentage": 71.5,
                            "dealt_to_champions": 6115,
                            "dealt_to_champions_percentage": 69.51,
                            "taken": 2014
                          },
                          "wards": {
                            "placed": 15,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 9
                          },
                          "wards_placed": 15
                        },
                        {
                          "assists": 7,
                          "champion": {
                            "id": 3120,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/cbc53ec5b2ef342a710ba2c56ca13915.png",
                            "name": "Viego",
                            "slug": "Viego"
                          },
                          "creep_score": 256,
                          "cs_at_14": 91,
                          "cs_diff_at_14": -1,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": true,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": true,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239290,
                          "gold_earned": 14713,
                          "gold_percentage": 20.41,
                          "gold_spent": 14525,
                          "items": [
                            {
                              "id": 2504,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2688,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c38d52b6bb9b984bf353c56585dae43d.png",
                              "is_trinket": false,
                              "name": "Force of Nature"
                            },
                            {
                              "id": 2931,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/936c2b63bc5f576ed6177e87e37a2384.png",
                              "is_trinket": false,
                              "name": "Blade of The Ruined King"
                            },
                            {
                              "id": 2937,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0085138b38b1f85411988b1db668bc94.png",
                              "is_trinket": false,
                              "name": "Divine Sunderer"
                            },
                            {
                              "id": 3047,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f45da294-c8ab-4d20-9216-d887579dc26d.png",
                              "is_trinket": false,
                              "name": "Guardian Angel"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 181,
                            "neutral_minions_enemy_jungle": 19,
                            "neutral_minions_team_jungle": 115,
                            "players": 2,
                            "turrets": 1,
                            "wards": 33
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
                            "dealt": 15845,
                            "dealt_percentage": 3.52,
                            "dealt_to_champions": 1378,
                            "dealt_to_champions_percentage": 2.57,
                            "taken": 8705
                          },
                          "masteries": [],
                          "minions_killed": 256,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 184938,
                            "dealt_percentage": 36.85,
                            "dealt_to_champions": 15492,
                            "dealt_to_champions_percentage": 36.67,
                            "taken": 22287
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-12-24",
                            "first_name": "Moon",
                            "id": 31392,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                            "last_name": "Hyeon-joon",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "Oner",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "oner"
                          },
                          "player_id": 31392,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 35,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                                  "name": "Legend: Tenacity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 37,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6c94f0110a44559cdcab24911a21b452.png",
                                  "name": "Coup de Grace",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 19,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                  "name": "Magical Footwear",
                                  "type": "slot1"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 215731,
                            "dealt_percentage": 20.14,
                            "dealt_to_champions": 18048,
                            "dealt_to_champions_percentage": 17.25,
                            "taken": 31569
                          },
                          "total_heal": 16210,
                          "total_time_crowd_control_dealt": 222,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 14947,
                            "dealt_percentage": 12.53,
                            "dealt_to_champions": 1177,
                            "dealt_to_champions_percentage": 13.38,
                            "taken": 576
                          },
                          "wards": {
                            "placed": 13,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 13
                          },
                          "wards_placed": 13
                        }
                      ],
                      "position": 5,
                      "status": "finished",
                      "teams": [
                        {
                          "atakhan_kills": null,
                          "bans": [
                            2982,
                            3085,
                            3020,
                            3040,
                            3175
                          ],
                          "baron_kills": 2,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 0,
                          "color": "blue",
                          "dragon_kills": 2,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": true,
                          "first_blood": true,
                          "first_dragon": true,
                          "first_herald": false,
                          "first_inhibitor": true,
                          "first_tower": true,
                          "first_voidgrub": null,
                          "gold_earned": 72070,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 1,
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
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "tower_kills": 8,
                          "voidgrub_kills": null
                        },
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3129,
                            3131,
                            3189,
                            3152,
                            3050
                          ],
                          "baron_kills": 0,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 0,
                          "color": "red",
                          "dragon_kills": 5,
                          "elder_drake_kills": 1,
                          "first_atakhan": null,
                          "first_baron": false,
                          "first_blood": false,
                          "first_dragon": false,
                          "first_herald": true,
                          "first_inhibitor": false,
                          "first_tower": false,
                          "first_voidgrub": null,
                          "gold_earned": 74703,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 1,
                          "kills": 19,
                          "mountain_drake_kills": 3,
                          "ocean_drake_kills": 1,
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
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "tower_kills": 8,
                          "voidgrub_kills": null
                        }
                      ],
                      "winner": {
                        "id": 126370,
                        "type": "Team"
                      },
                      "winner_type": "Team"
                    },
                    {
                      "begin_at": "2022-11-06T03:45:11Z",
                      "complete": true,
                      "detailed_stats": true,
                      "end_at": "2022-11-06T04:20:55Z",
                      "finished": true,
                      "forfeit": false,
                      "id": 239289,
                      "length": 1724,
                      "match_id": 651268,
                      "players": [
                        {
                          "assists": 0,
                          "champion": {
                            "id": 2982,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/254171517c5418e10285bba695dfa951.png",
                            "name": "Akali",
                            "slug": "Akali"
                          },
                          "creep_score": 236,
                          "cs_at_14": 131,
                          "cs_diff_at_14": -9,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239289,
                          "gold_earned": 9302,
                          "gold_percentage": 20.05,
                          "gold_spent": 9150,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2640,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/178aee5eaa5e7a70f6a05155b7dcf3e2.png",
                              "is_trinket": false,
                              "name": "Doran's Shield"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2901,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/e5f1a636a1edba83ccd1d7a48cb2cea2.png",
                              "is_trinket": false,
                              "name": "Hextech Rocketbelt"
                            },
                            {
                              "id": 2909,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/7ec8f413ab83b109852d5c3fd7c5b197.png",
                              "is_trinket": false,
                              "name": "Shadowflame"
                            },
                            {
                              "id": 3043,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3c9dee81-cfff-4920-87ad-e0516ac0fc92.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 4,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 4,
                            "players": 0,
                            "turrets": 0,
                            "wards": 8
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
                            "dealt": 100520,
                            "dealt_percentage": 61.32,
                            "dealt_to_champions": 7742,
                            "dealt_to_champions_percentage": 46.59,
                            "taken": 12935
                          },
                          "masteries": [],
                          "minions_killed": 236,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 16623,
                            "dealt_percentage": 4.59,
                            "dealt_to_champions": 800,
                            "dealt_to_champions_percentage": 4.13,
                            "taken": 13599
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-05-07",
                            "first_name": "Lee",
                            "id": 585,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                            "last_name": "Sang-hyeok",
                            "modified_at": "2026-02-01T11:19:16Z",
                            "name": "Faker",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "faker"
                          },
                          "player_id": 585,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 29,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d7dee9f79afc995429521e2b586aae87.png",
                                "name": "Fleet Footwork",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 33,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                                  "name": "Presence of Mind",
                                  "type": "slot1"
                                },
                                {
                                  "id": 35,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                                  "name": "Legend: Tenacity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 49,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
                                  "name": "Overgrowth",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 117583,
                            "dealt_percentage": 21.39,
                            "dealt_to_champions": 8982,
                            "dealt_to_champions_percentage": 22.23,
                            "taken": 26904
                          },
                          "total_heal": 1759,
                          "total_time_crowd_control_dealt": 75,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 439,
                            "dealt_percentage": 1.89,
                            "dealt_to_champions": 439,
                            "dealt_to_champions_percentage": 9.99,
                            "taken": 370
                          },
                          "wards": {
                            "placed": 8,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 6
                          },
                          "wards_placed": 8
                        },
                        {
                          "assists": 4,
                          "champion": {
                            "id": 3177,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/bf77b476-a4b2-4433-a896-13d082b51644.png",
                            "name": "Varus",
                            "slug": "Varus"
                          },
                          "creep_score": 288,
                          "cs_at_14": 121,
                          "cs_diff_at_14": -4,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": true
                          },
                          "game_id": 239289,
                          "gold_earned": 12895,
                          "gold_percentage": 23.55,
                          "gold_spent": 10725,
                          "items": [
                            {
                              "id": 2452,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/39be7228685c0a558c743c21dfc078f9.png",
                              "is_trinket": false,
                              "name": "Null-Magic Mantle"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2544,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/924cb9f122b90bf1ee29b9650c092524.png",
                              "is_trinket": false,
                              "name": "Guinsoo's Rageblade"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2699,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0f33f102856e8d40f6d38ff057856e1d.png",
                              "is_trinket": false,
                              "name": "Immortal Shieldbow"
                            },
                            {
                              "id": 2763,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1a0dab15964871b507375c342d5536bc.png",
                              "is_trinket": false,
                              "name": "Runaan's Hurricane"
                            }
                          ],
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 20,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 20,
                            "players": 3,
                            "turrets": 1,
                            "wards": 7
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 245,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 14,
                          "magic_damage": {
                            "dealt": 25068,
                            "dealt_percentage": 8.42,
                            "dealt_to_champions": 4241,
                            "dealt_to_champions_percentage": 13.26,
                            "taken": 3685
                          },
                          "masteries": [],
                          "minions_killed": 288,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 178209,
                            "dealt_percentage": 47.54,
                            "dealt_to_champions": 10790,
                            "dealt_to_champions_percentage": 27.92,
                            "taken": 10326
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-10-23",
                            "first_name": "Kim",
                            "id": 2169,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/2169/ezgif_3_4d5729796f.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 28,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d11f16420cc7a65ce1f1253d0adf5459.png",
                                "name": "Lethal Tempo",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 30,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/62cc94a564835cd3abd80d74346c35da.png",
                              "name": "Heal"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 212578,
                            "dealt_percentage": 30.34,
                            "dealt_to_champions": 18094,
                            "dealt_to_champions_percentage": 23.89,
                            "taken": 16979
                          },
                          "total_heal": 1998,
                          "total_time_crowd_control_dealt": 346,
                          "total_units_healed": 4,
                          "true_damage": {
                            "dealt": 9300,
                            "dealt_percentage": 33.18,
                            "dealt_to_champions": 3062,
                            "dealt_to_champions_percentage": 59.85,
                            "taken": 2967
                          },
                          "wards": {
                            "placed": 13,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 5
                          },
                          "wards_placed": 13
                        },
                        {
                          "assists": 2,
                          "champion": {
                            "id": 3097,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/e3925977da5cff76ab456040466b1eed.png",
                            "name": "Soraka",
                            "slug": "Soraka"
                          },
                          "creep_score": 16,
                          "cs_at_14": 7,
                          "cs_diff_at_14": -6,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": true,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239289,
                          "gold_earned": 6561,
                          "gold_percentage": 14.15,
                          "gold_spent": 7090,
                          "items": [
                            {
                              "id": 2460,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0f07d995a4de9dc12ffaf8c403658755.png",
                              "is_trinket": false,
                              "name": "Amplifying Tome"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2566,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/e09b668319c871385af2c51023e7e0f9.png",
                              "is_trinket": false,
                              "name": "Mikael's Blessing"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 3016,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b4e5bb16fbc4368c43c9712a2a154e6f.png",
                              "is_trinket": false,
                              "name": "Oblivion Orb"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 0,
                            "players": 2,
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
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 10,
                          "magic_damage": {
                            "dealt": 18017,
                            "dealt_percentage": 10.99,
                            "dealt_to_champions": 4445,
                            "dealt_to_champions_percentage": 26.75,
                            "taken": 3241
                          },
                          "masteries": [],
                          "minions_killed": 16,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 5001,
                            "dealt_percentage": 1.38,
                            "dealt_to_champions": 1239,
                            "dealt_to_champions_percentage": 6.39,
                            "taken": 6581
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-10-14",
                            "first_name": "Ryu",
                            "id": 8158,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                            "last_name": "Min-seok",
                            "modified_at": "2026-02-01T11:19:16Z",
                            "name": "Keria",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "keria"
                          },
                          "player_id": 8158,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 52,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fbe3405d6a68d3b7ae3f305fdf129e99.png",
                                "name": "Summon Aery",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 57,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/59ba46a95f8b51739d4eb2179654cf7e.png",
                                  "name": "Nimbus Cloak",
                                  "type": "slot1"
                                },
                                {
                                  "id": 59,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/732d4e2a7fdf6ecc3ec8e42504a111b9.png",
                                  "name": "Celerity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 50,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/59300ef037fe282f309a78055dd3559f.png",
                                  "name": "Revitalize",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 30,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/62cc94a564835cd3abd80d74346c35da.png",
                              "name": "Heal"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 23256,
                            "dealt_percentage": 4.23,
                            "dealt_to_champions": 5923,
                            "dealt_to_champions_percentage": 14.66,
                            "taken": 10021
                          },
                          "total_heal": 11796,
                          "total_time_crowd_control_dealt": 251,
                          "total_units_healed": 5,
                          "true_damage": {
                            "dealt": 238,
                            "dealt_percentage": 1.03,
                            "dealt_to_champions": 238,
                            "dealt_to_champions_percentage": 5.42,
                            "taken": 198
                          },
                          "wards": {
                            "placed": 43,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 19
                          },
                          "wards_placed": 43
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3166,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/cad8d209-bda9-43f3-a7fa-cebce483ec37.png",
                            "name": "Aatrox",
                            "slug": "Aatrox"
                          },
                          "creep_score": 231,
                          "cs_at_14": 124,
                          "cs_diff_at_14": 14,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": true,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239289,
                          "gold_earned": 13335,
                          "gold_percentage": 24.36,
                          "gold_spent": 12250,
                          "items": [
                            {
                              "id": 2504,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2912,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/eaef5f4c2f6f2d5fcf13f287c321e59b.png",
                              "is_trinket": false,
                              "name": "Eclipse"
                            },
                            {
                              "id": 2933,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/9eb16adb98fcdc9c9ae35eabe19c322f.png",
                              "is_trinket": false,
                              "name": "Maw of Malmortius"
                            },
                            {
                              "id": 2934,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6f38d2d2845b0958a9cf0c03b8d592a2.png",
                              "is_trinket": false,
                              "name": "Death's Dance"
                            },
                            {
                              "id": 3044,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d0e13016-50c3-4bf8-926c-a502cced78c4.png",
                              "is_trinket": false,
                              "name": "Broken Stopwatch"
                            }
                          ],
                          "kills": 5,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 44,
                            "neutral_minions_enemy_jungle": 4,
                            "neutral_minions_team_jungle": 34,
                            "players": 5,
                            "turrets": 2,
                            "wards": 7
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
                            "dealt": 523,
                            "dealt_percentage": 0.18,
                            "dealt_to_champions": 51,
                            "dealt_to_champions_percentage": 0.16,
                            "taken": 5160
                          },
                          "masteries": [],
                          "minions_killed": 231,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 163828,
                            "dealt_percentage": 43.71,
                            "dealt_to_champions": 24940,
                            "dealt_to_champions_percentage": 64.52,
                            "taken": 9091
                          },
                          "player": {
                            "active": true,
                            "age": 26,
                            "birthday": "2000-03-11",
                            "first_name": "Hwang",
                            "id": 8172,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/8172/drx_kingen_2022_split_2.png",
                            "last_name": "Seong-hoon",
                            "modified_at": "2026-02-01T11:16:32Z",
                            "name": "Kingen",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "kingen"
                          },
                          "player_id": 8172,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 35,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                                  "name": "Legend: Tenacity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 48,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6054dc49089750c7d576b8e157228f29.png",
                                  "name": "Bone Plating",
                                  "type": "slot2"
                                },
                                {
                                  "id": 49,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
                                  "name": "Overgrowth",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 167744,
                            "dealt_percentage": 23.94,
                            "dealt_to_champions": 24992,
                            "dealt_to_champions_percentage": 32.99,
                            "taken": 17557
                          },
                          "total_heal": 11155,
                          "total_time_crowd_control_dealt": 220,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 3391,
                            "dealt_percentage": 12.1,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 3305
                          },
                          "wards": {
                            "placed": 9,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 6
                          },
                          "wards_placed": 9
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 3175,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/499d8d59-146b-43de-a271-0198158b887a.png",
                            "name": "Renata Glasc",
                            "slug": "Renata"
                          },
                          "creep_score": 29,
                          "cs_at_14": 13,
                          "cs_diff_at_14": 6,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239289,
                          "gold_earned": 7410,
                          "gold_percentage": 13.53,
                          "gold_spent": 6110,
                          "items": [
                            {
                              "id": 2460,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0f07d995a4de9dc12ffaf8c403658755.png",
                              "is_trinket": false,
                              "name": "Amplifying Tome"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2512,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1e29f7f8a099017ed7b1a6333a9357b1.png",
                              "is_trinket": false,
                              "name": "Kindlegem"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 3007,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a53f4c97c8d30ad58cb978e397107463.png",
                              "is_trinket": false,
                              "name": "Chemtech Putrifier"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 0,
                            "players": 1,
                            "turrets": 2,
                            "wards": 12
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
                          "level": 12,
                          "magic_damage": {
                            "dealt": 22951,
                            "dealt_percentage": 7.71,
                            "dealt_to_champions": 3978,
                            "dealt_to_champions_percentage": 12.44,
                            "taken": 2577
                          },
                          "masteries": [],
                          "minions_killed": 29,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 7545,
                            "dealt_percentage": 2.01,
                            "dealt_to_champions": 1402,
                            "dealt_to_champions_percentage": 3.63,
                            "taken": 4982
                          },
                          "player": {
                            "active": true,
                            "age": 28,
                            "birthday": "1997-04-01",
                            "first_name": "Cho",
                            "id": 15425,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/15425/drx_bery_l_2022_split_2.png",
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
                            "primary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "keystone": {
                                "id": 42,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ded20bb65d8b80ffaf6408be45136628.png",
                                "name": "Guardian",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 45,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/592200e1a39d2281977fc92d788cacd1.png",
                                  "name": "Shield Bash",
                                  "type": "slot1"
                                },
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 51,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                                  "name": "Unflinching",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 1,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                              "lesser_runes": [
                                {
                                  "id": 6,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/faae66d46ae5bc177a56890342087ac2.png",
                                  "name": "Taste of Blood",
                                  "type": "slot1"
                                },
                                {
                                  "id": 13,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/623d21bc9acd874af4f1c2150bdd7150.png",
                                  "name": "Relentless Hunter",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Domination",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 31613,
                            "dealt_percentage": 4.51,
                            "dealt_to_champions": 6496,
                            "dealt_to_champions_percentage": 8.58,
                            "taken": 7560
                          },
                          "total_heal": 1182,
                          "total_time_crowd_control_dealt": 225,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 1116,
                            "dealt_percentage": 3.98,
                            "dealt_to_champions": 1116,
                            "dealt_to_champions_percentage": 21.81,
                            "taken": 0
                          },
                          "wards": {
                            "placed": 42,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 13
                          },
                          "wards_placed": 42
                        },
                        {
                          "assists": 3,
                          "champion": {
                            "id": 3188,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/b7b35ce1-2691-4cff-aaa4-0ca086b30d26.png",
                            "name": "Kalista",
                            "slug": "Kalista"
                          },
                          "creep_score": 287,
                          "cs_at_14": 125,
                          "cs_diff_at_14": 4,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239289,
                          "gold_earned": 10833,
                          "gold_percentage": 23.36,
                          "gold_spent": 10850,
                          "items": [
                            {
                              "id": 2544,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/924cb9f122b90bf1ee29b9650c092524.png",
                              "is_trinket": false,
                              "name": "Guinsoo's Rageblade"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2699,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0f33f102856e8d40f6d38ff057856e1d.png",
                              "is_trinket": false,
                              "name": "Immortal Shieldbow"
                            },
                            {
                              "id": 2820,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/82133cdb92c1ca86e27b1e021faa84e9.png",
                              "is_trinket": false,
                              "name": "Lord Dominik's Regards"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 24,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 24,
                            "players": 0,
                            "turrets": 1,
                            "wards": 7
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 247,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 14,
                          "magic_damage": {
                            "dealt": 4045,
                            "dealt_percentage": 2.47,
                            "dealt_to_champions": 754,
                            "dealt_to_champions_percentage": 4.54,
                            "taken": 5163
                          },
                          "masteries": [],
                          "minions_killed": 287,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 156378,
                            "dealt_percentage": 43.14,
                            "dealt_to_champions": 7332,
                            "dealt_to_champions_percentage": 37.81,
                            "taken": 8434
                          },
                          "player": {
                            "active": true,
                            "age": 24,
                            "birthday": "2002-02-06",
                            "first_name": "Lee",
                            "id": 19285,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/19285/t1_gumayusi_2023_split_2.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 28,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d11f16420cc7a65ce1f1253d0adf5459.png",
                                "name": "Lethal Tempo",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 31,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/e8a57b03d6f13c42c79c579254920a11.png",
                                  "name": "Overheal",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 37,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6c94f0110a44559cdcab24911a21b452.png",
                                  "name": "Coup de Grace",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 23,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/65eea722a1fc79fb6469e7246eb0afb8.png",
                              "name": "Cleanse"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 162348,
                            "dealt_percentage": 29.54,
                            "dealt_to_champions": 8283,
                            "dealt_to_champions_percentage": 20.5,
                            "taken": 14302
                          },
                          "total_heal": 201,
                          "total_time_crowd_control_dealt": 390,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 1924,
                            "dealt_percentage": 8.29,
                            "dealt_to_champions": 196,
                            "dealt_to_champions_percentage": 4.46,
                            "taken": 704
                          },
                          "wards": {
                            "placed": 14,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 6
                          },
                          "wards_placed": 14
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 3053,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/d8cee56dc327f130e470caf9871b2654.png",
                            "name": "Maokai",
                            "slug": "Maokai"
                          },
                          "creep_score": 118,
                          "cs_at_14": 70,
                          "cs_diff_at_14": -25,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239289,
                          "gold_earned": 9114,
                          "gold_percentage": 16.65,
                          "gold_spent": 8275,
                          "items": [
                            {
                              "id": 2512,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1e29f7f8a099017ed7b1a6333a9357b1.png",
                              "is_trinket": false,
                              "name": "Kindlegem"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2830,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/4a236638d83dc2546184646200a5042a.png",
                              "is_trinket": false,
                              "name": "Frozen Heart"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 3019,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/5c65145d1a8bab82316337cd7e27cd6c.png",
                              "is_trinket": false,
                              "name": "Frostfire Gauntlet"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 101,
                            "neutral_minions_enemy_jungle": 8,
                            "neutral_minions_team_jungle": 57,
                            "players": 4,
                            "turrets": 1,
                            "wards": 8
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
                          "level": 13,
                          "magic_damage": {
                            "dealt": 81209,
                            "dealt_percentage": 27.28,
                            "dealt_to_champions": 8013,
                            "dealt_to_champions_percentage": 25.06,
                            "taken": 3721
                          },
                          "masteries": [],
                          "minions_killed": 118,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 15179,
                            "dealt_percentage": 4.05,
                            "dealt_to_champions": 648,
                            "dealt_to_champions_percentage": 1.68,
                            "taken": 11450
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-03-21",
                            "first_name": "Hong",
                            "id": 24996,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/24996/tl_pyosik_2023_split_1.png",
                            "last_name": "Chang-hyeon",
                            "modified_at": "2026-02-08T13:14:45Z",
                            "name": "Pyosik",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "pyosik"
                          },
                          "player_id": 24996,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 54,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4ee4739ae4a9cbf7be59650f92009edc.png",
                                "name": "Phase Rush",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 57,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/59ba46a95f8b51739d4eb2179654cf7e.png",
                                  "name": "Nimbus Cloak",
                                  "type": "slot1"
                                },
                                {
                                  "id": 58,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/632a47c2a88802029838e383a866feb1.png",
                                  "name": "Transcendence",
                                  "type": "slot2"
                                },
                                {
                                  "id": 62,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/abb0332095ac959dacaa1ed0ad4ad5e2.png",
                                  "name": "Waterwalking",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                },
                                {
                                  "id": 21,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/032d8f7fe2b24e22e8740bcca4e4d84c.png",
                                  "name": "Future's Market",
                                  "type": "slot2"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 108520,
                            "dealt_percentage": 15.49,
                            "dealt_to_champions": 9600,
                            "dealt_to_champions_percentage": 12.67,
                            "taken": 15454
                          },
                          "total_heal": 9294,
                          "total_time_crowd_control_dealt": 869,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 12131,
                            "dealt_percentage": 43.27,
                            "dealt_to_champions": 938,
                            "dealt_to_champions_percentage": 18.33,
                            "taken": 282
                          },
                          "wards": {
                            "placed": 13,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 12
                          },
                          "wards_placed": 13
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 2991,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/baf32ee97457437ea20c42ba23003e0c.png",
                            "name": "Azir",
                            "slug": "Azir"
                          },
                          "creep_score": 291,
                          "cs_at_14": 140,
                          "cs_diff_at_14": 9,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239289,
                          "gold_earned": 11996,
                          "gold_percentage": 21.91,
                          "gold_spent": 10825,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2908,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/e6408582a9edbfc6d6896b3dc2631cd7.png",
                              "is_trinket": false,
                              "name": "Crown of the Shattered Queen"
                            },
                            {
                              "id": 2909,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/7ec8f413ab83b109852d5c3fd7c5b197.png",
                              "is_trinket": false,
                              "name": "Shadowflame"
                            },
                            {
                              "id": 3012,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/67ee113a533a1e443672e237d45f0043.png",
                              "is_trinket": false,
                              "name": "Morellonomicon"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 30,
                            "neutral_minions_enemy_jungle": 8,
                            "neutral_minions_team_jungle": 22,
                            "players": 1,
                            "turrets": 2,
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
                          "level": 17,
                          "magic_damage": {
                            "dealt": 167935,
                            "dealt_percentage": 56.41,
                            "dealt_to_champions": 15690,
                            "dealt_to_champions_percentage": 49.07,
                            "taken": 6253
                          },
                          "masteries": [],
                          "minions_killed": 291,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 10078,
                            "dealt_percentage": 2.69,
                            "dealt_to_champions": 873,
                            "dealt_to_champions_percentage": 2.26,
                            "taken": 7446
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-11-28",
                            "first_name": "Kim",
                            "id": 25391,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/25391/drx_zeka_2022_split_2.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 33,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                                  "name": "Presence of Mind",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 37,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6c94f0110a44559cdcab24911a21b452.png",
                                  "name": "Coup de Grace",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "lesser_runes": [
                                {
                                  "id": 56,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                  "name": "Manaflow Band",
                                  "type": "slot1"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 180108,
                            "dealt_percentage": 25.71,
                            "dealt_to_champions": 16564,
                            "dealt_to_champions_percentage": 21.87,
                            "taken": 14526
                          },
                          "total_heal": 957,
                          "total_time_crowd_control_dealt": 244,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 2095,
                            "dealt_percentage": 7.47,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 826
                          },
                          "wards": {
                            "placed": 16,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 9
                          },
                          "wards_placed": 16
                        },
                        {
                          "assists": 1,
                          "champion": {
                            "id": 3010,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/021d3dbf409641c5de3ec1aa8c9d2eae.png",
                            "name": "Fiora",
                            "slug": "Fiora"
                          },
                          "creep_score": 237,
                          "cs_at_14": 110,
                          "cs_diff_at_14": -14,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239289,
                          "gold_earned": 11341,
                          "gold_percentage": 24.45,
                          "gold_spent": 11300,
                          "items": [
                            {
                              "id": 2454,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d1be217640f29b7c6b5edc638d1c47d5.png",
                              "is_trinket": false,
                              "name": "Long Sword"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2928,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6a940e698e30b4298a0e176358d10a66.png",
                              "is_trinket": false,
                              "name": "Ravenous Hydra"
                            },
                            {
                              "id": 2933,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/9eb16adb98fcdc9c9ae35eabe19c322f.png",
                              "is_trinket": false,
                              "name": "Maw of Malmortius"
                            },
                            {
                              "id": 2937,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0085138b38b1f85411988b1db668bc94.png",
                              "is_trinket": false,
                              "name": "Divine Sunderer"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 2,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 2,
                            "players": 1,
                            "turrets": 3,
                            "wards": 4
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 546,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 2174,
                            "dealt_percentage": 1.33,
                            "dealt_to_champions": 544,
                            "dealt_to_champions_percentage": 3.27,
                            "taken": 6682
                          },
                          "masteries": [],
                          "minions_killed": 237,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 119662,
                            "dealt_percentage": 33.01,
                            "dealt_to_champions": 6856,
                            "dealt_to_champions_percentage": 35.35,
                            "taken": 13937
                          },
                          "player": {
                            "active": true,
                            "age": 22,
                            "birthday": "2004-01-31",
                            "first_name": "Choi",
                            "id": 31391,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31391/t1_zeus_2023_split_2.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 29,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d7dee9f79afc995429521e2b586aae87.png",
                                "name": "Fleet Footwork",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 35,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                                  "name": "Legend: Tenacity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 19,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                  "name": "Magical Footwear",
                                  "type": "slot1"
                                },
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 29,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/58955cb861c3b51375948a05e260996a.png",
                              "name": "Ghost"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 129827,
                            "dealt_percentage": 23.62,
                            "dealt_to_champions": 10306,
                            "dealt_to_champions_percentage": 25.5,
                            "taken": 21487
                          },
                          "total_heal": 8201,
                          "total_time_crowd_control_dealt": 87,
                          "total_units_healed": 2,
                          "true_damage": {
                            "dealt": 7990,
                            "dealt_percentage": 34.42,
                            "dealt_to_champions": 2905,
                            "dealt_to_champions_percentage": 66.13,
                            "taken": 868
                          },
                          "wards": {
                            "placed": 10,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 2
                          },
                          "wards_placed": 10
                        },
                        {
                          "assists": 2,
                          "champion": {
                            "id": 3085,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/334bbb28d99b00df03f7c28e929457ce.png",
                            "name": "Sejuani",
                            "slug": "Sejuani"
                          },
                          "creep_score": 144,
                          "cs_at_14": 95,
                          "cs_diff_at_14": 25,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239289,
                          "gold_earned": 8346,
                          "gold_percentage": 17.99,
                          "gold_spent": 8100,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2862,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/cd94b3bb54d41475f8a5e68c262f8c9c.png",
                              "is_trinket": false,
                              "name": "Bramble Vest"
                            },
                            {
                              "id": 2879,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d972aa4ca80a36d145c4e1cb7de00b45.png",
                              "is_trinket": false,
                              "name": "Anathema's Chains"
                            },
                            {
                              "id": 3019,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/5c65145d1a8bab82316337cd7e27cd6c.png",
                              "is_trinket": false,
                              "name": "Frostfire Gauntlet"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 125,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 88,
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
                          "level": 12,
                          "magic_damage": {
                            "dealt": 39170,
                            "dealt_percentage": 23.89,
                            "dealt_to_champions": 3134,
                            "dealt_to_champions_percentage": 18.86,
                            "taken": 5739
                          },
                          "masteries": [],
                          "minions_killed": 144,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 64804,
                            "dealt_percentage": 17.88,
                            "dealt_to_champions": 3166,
                            "dealt_to_champions_percentage": 16.33,
                            "taken": 17057
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-12-24",
                            "first_name": "Moon",
                            "id": 31392,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                            "last_name": "Hyeon-joon",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "Oner",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "oner"
                          },
                          "player_id": 31392,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 54,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4ee4739ae4a9cbf7be59650f92009edc.png",
                                "name": "Phase Rush",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 57,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/59ba46a95f8b51739d4eb2179654cf7e.png",
                                  "name": "Nimbus Cloak",
                                  "type": "slot1"
                                },
                                {
                                  "id": 59,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/732d4e2a7fdf6ecc3ec8e42504a111b9.png",
                                  "name": "Celerity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 62,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/abb0332095ac959dacaa1ed0ad4ad5e2.png",
                                  "name": "Waterwalking",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 21,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/032d8f7fe2b24e22e8740bcca4e4d84c.png",
                                  "name": "Future's Market",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 116596,
                            "dealt_percentage": 21.21,
                            "dealt_to_champions": 6916,
                            "dealt_to_champions_percentage": 17.11,
                            "taken": 23671
                          },
                          "total_heal": 6438,
                          "total_time_crowd_control_dealt": 474,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 12621,
                            "dealt_percentage": 54.37,
                            "dealt_to_champions": 615,
                            "dealt_to_champions_percentage": 14,
                            "taken": 874
                          },
                          "wards": {
                            "placed": 9,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 8
                          },
                          "wards_placed": 9
                        }
                      ],
                      "position": 4,
                      "status": "finished",
                      "teams": [
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3040,
                            3156,
                            3120,
                            3131,
                            3020
                          ],
                          "baron_kills": 0,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 0,
                          "color": "red",
                          "dragon_kills": 1,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": false,
                          "first_blood": true,
                          "first_dragon": true,
                          "first_herald": true,
                          "first_inhibitor": false,
                          "first_tower": false,
                          "first_voidgrub": null,
                          "gold_earned": 46383,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 1,
                          "inhibitor_kills": 0,
                          "kills": 4,
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
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "tower_kills": 3,
                          "voidgrub_kills": null
                        },
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3152,
                            3121,
                            2989,
                            3129,
                            3083
                          ],
                          "baron_kills": 1,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 1,
                          "color": "blue",
                          "dragon_kills": 3,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": true,
                          "first_blood": false,
                          "first_dragon": false,
                          "first_herald": false,
                          "first_inhibitor": true,
                          "first_tower": true,
                          "first_voidgrub": null,
                          "gold_earned": 54750,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 2,
                          "kills": 14,
                          "mountain_drake_kills": 2,
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
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "tower_kills": 9,
                          "voidgrub_kills": null
                        }
                      ],
                      "winner": {
                        "id": 126370,
                        "type": "Team"
                      },
                      "winner_type": "Team"
                    },
                    {
                      "begin_at": "2022-11-06T02:52:59Z",
                      "complete": true,
                      "detailed_stats": true,
                      "end_at": "2022-11-06T03:29:56Z",
                      "finished": true,
                      "forfeit": false,
                      "id": 239288,
                      "length": 1931,
                      "match_id": 651268,
                      "players": [
                        {
                          "assists": 1,
                          "champion": {
                            "id": 2991,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/baf32ee97457437ea20c42ba23003e0c.png",
                            "name": "Azir",
                            "slug": "Azir"
                          },
                          "creep_score": 252,
                          "cs_at_14": 137,
                          "cs_diff_at_14": 7,
                          "deaths": 5,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239288,
                          "gold_earned": 12707,
                          "gold_percentage": 21.15,
                          "gold_spent": 12650,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2642,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d3c7dce8ed50a8553198bdefbacac855.png",
                              "is_trinket": false,
                              "name": "Needlessly Large Rod"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2871,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/8cef60e74adf20cb8372afd4aa49cde9.png",
                              "is_trinket": false,
                              "name": "Liandry's Anguish"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2909,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/7ec8f413ab83b109852d5c3fd7c5b197.png",
                              "is_trinket": false,
                              "name": "Shadowflame"
                            }
                          ],
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 20,
                            "neutral_minions_enemy_jungle": 6,
                            "neutral_minions_team_jungle": 12,
                            "players": 3,
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
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 144733,
                            "dealt_percentage": 48.79,
                            "dealt_to_champions": 20874,
                            "dealt_to_champions_percentage": 41.04,
                            "taken": 7957
                          },
                          "masteries": [],
                          "minions_killed": 252,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 13194,
                            "dealt_percentage": 3.43,
                            "dealt_to_champions": 884,
                            "dealt_to_champions_percentage": 2.92,
                            "taken": 10830
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-05-07",
                            "first_name": "Lee",
                            "id": 585,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                            "last_name": "Sang-hyeok",
                            "modified_at": "2026-02-01T11:19:16Z",
                            "name": "Faker",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "faker"
                          },
                          "player_id": 585,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 33,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                                  "name": "Presence of Mind",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 38,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/08f4edce2a6f85edbfea701c04314cb9.png",
                                  "name": "Cut Down",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "lesser_runes": [
                                {
                                  "id": 56,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                  "name": "Manaflow Band",
                                  "type": "slot1"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 157927,
                            "dealt_percentage": 22.06,
                            "dealt_to_champions": 21759,
                            "dealt_to_champions_percentage": 26.14,
                            "taken": 19600
                          },
                          "total_heal": 1681,
                          "total_time_crowd_control_dealt": 212,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 0,
                            "dealt_percentage": 0,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 813
                          },
                          "wards": {
                            "placed": 18,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 10
                          },
                          "wards_placed": 18
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3188,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/b7b35ce1-2691-4cff-aaa4-0ca086b30d26.png",
                            "name": "Kalista",
                            "slug": "Kalista"
                          },
                          "creep_score": 242,
                          "cs_at_14": 88,
                          "cs_diff_at_14": -44,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": true,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239288,
                          "gold_earned": 12754,
                          "gold_percentage": 23.7,
                          "gold_spent": 10875,
                          "items": [
                            {
                              "id": 2544,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/924cb9f122b90bf1ee29b9650c092524.png",
                              "is_trinket": false,
                              "name": "Guinsoo's Rageblade"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2930,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/5bc313a2ec67cebd731e4cf0549cb077.png",
                              "is_trinket": false,
                              "name": "Wit's End"
                            },
                            {
                              "id": 2976,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/9cf8cfb0-e301-4426-817d-0eb0ee274d4b.png",
                              "is_trinket": false,
                              "name": "Bloodward"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 13,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 12,
                            "players": 4,
                            "turrets": 1,
                            "wards": 8
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 223,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 14,
                          "magic_damage": {
                            "dealt": 12118,
                            "dealt_percentage": 4.01,
                            "dealt_to_champions": 2042,
                            "dealt_to_champions_percentage": 5.98,
                            "taken": 6147
                          },
                          "masteries": [],
                          "minions_killed": 242,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 150309,
                            "dealt_percentage": 45.67,
                            "dealt_to_champions": 7922,
                            "dealt_to_champions_percentage": 34.78,
                            "taken": 8129
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-10-23",
                            "first_name": "Kim",
                            "id": 2169,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/2169/ezgif_3_4d5729796f.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 28,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d11f16420cc7a65ce1f1253d0adf5459.png",
                                "name": "Lethal Tempo",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 23,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/65eea722a1fc79fb6469e7246eb0afb8.png",
                              "name": "Cleanse"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 167108,
                            "dealt_percentage": 25.16,
                            "dealt_to_champions": 9964,
                            "dealt_to_champions_percentage": 15.07,
                            "taken": 14622
                          },
                          "total_heal": 346,
                          "total_time_crowd_control_dealt": 354,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 4681,
                            "dealt_percentage": 14.05,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 346
                          },
                          "wards": {
                            "placed": 15,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 5
                          },
                          "wards_placed": 15
                        },
                        {
                          "assists": 8,
                          "champion": {
                            "id": 3032,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/cee9e33f3ea3f3b989bcbb342730e231.png",
                            "name": "Karma",
                            "slug": "Karma"
                          },
                          "creep_score": 34,
                          "cs_at_14": 8,
                          "cs_diff_at_14": -1,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": true,
                            "first_tower_kill": false
                          },
                          "game_id": 239288,
                          "gold_earned": 10168,
                          "gold_percentage": 16.92,
                          "gold_spent": 8400,
                          "items": [
                            {
                              "id": 2534,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/73578d8f7a2a451b61696009016c134a.png",
                              "is_trinket": false,
                              "name": "Fiendish Codex"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2761,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b4754269-dc0f-474a-a3b4-c181b7d6d26c.png",
                              "is_trinket": false,
                              "name": "Shurelya's Battlesong"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 3007,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a53f4c97c8d30ad58cb978e397107463.png",
                              "is_trinket": false,
                              "name": "Chemtech Putrifier"
                            }
                          ],
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 4,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 4,
                            "players": 3,
                            "turrets": 0,
                            "wards": 8
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
                          "level": 14,
                          "magic_damage": {
                            "dealt": 51505,
                            "dealt_percentage": 17.36,
                            "dealt_to_champions": 10313,
                            "dealt_to_champions_percentage": 20.27,
                            "taken": 4272
                          },
                          "masteries": [],
                          "minions_killed": 34,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 5015,
                            "dealt_percentage": 1.3,
                            "dealt_to_champions": 997,
                            "dealt_to_champions_percentage": 3.29,
                            "taken": 5541
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-10-14",
                            "first_name": "Ryu",
                            "id": 8158,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                            "last_name": "Min-seok",
                            "modified_at": "2026-02-01T11:19:16Z",
                            "name": "Keria",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "keria"
                          },
                          "player_id": 8158,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 53,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/b8282c680e5d022dc564c54937a20a26.png",
                                "name": "Arcane Comet",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 57,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/59ba46a95f8b51739d4eb2179654cf7e.png",
                                  "name": "Nimbus Cloak",
                                  "type": "slot1"
                                },
                                {
                                  "id": 60,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/0103e35a695d637b86f7d6344653009b.png",
                                  "name": "Absolute Focus",
                                  "type": "slot2"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 57375,
                            "dealt_percentage": 8.01,
                            "dealt_to_champions": 12164,
                            "dealt_to_champions_percentage": 14.61,
                            "taken": 9958
                          },
                          "total_heal": 3013,
                          "total_time_crowd_control_dealt": 270,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 854,
                            "dealt_percentage": 2.5,
                            "dealt_to_champions": 854,
                            "dealt_to_champions_percentage": 41.42,
                            "taken": 144
                          },
                          "wards": {
                            "placed": 47,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 16
                          },
                          "wards_placed": 47
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3068,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/c85a85ae33a47512d18da2cf10d65a90.png",
                            "name": "Ornn",
                            "slug": "Ornn"
                          },
                          "creep_score": 200,
                          "cs_at_14": 103,
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
                          "game_id": 239288,
                          "gold_earned": 9004,
                          "gold_percentage": 16.73,
                          "gold_spent": 8250,
                          "items": [
                            {
                              "id": 2452,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/39be7228685c0a558c743c21dfc078f9.png",
                              "is_trinket": false,
                              "name": "Null-Magic Mantle"
                            },
                            {
                              "id": 2640,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/178aee5eaa5e7a70f6a05155b7dcf3e2.png",
                              "is_trinket": false,
                              "name": "Doran's Shield"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2830,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/4a236638d83dc2546184646200a5042a.png",
                              "is_trinket": false,
                              "name": "Frozen Heart"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 3023,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/88ccb778-dc32-46ff-85d2-65f2f7c5158a.png",
                              "is_trinket": false,
                              "name": "Rimeforged Grasp"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 4,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 4,
                            "players": 0,
                            "turrets": 0,
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
                          "largest_multi_kill": 0,
                          "level": 14,
                          "magic_damage": {
                            "dealt": 71954,
                            "dealt_percentage": 23.84,
                            "dealt_to_champions": 8744,
                            "dealt_to_champions_percentage": 25.6,
                            "taken": 15006
                          },
                          "masteries": [],
                          "minions_killed": 200,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 41859,
                            "dealt_percentage": 12.72,
                            "dealt_to_champions": 4110,
                            "dealt_to_champions_percentage": 18.04,
                            "taken": 10409
                          },
                          "player": {
                            "active": true,
                            "age": 26,
                            "birthday": "2000-03-11",
                            "first_name": "Hwang",
                            "id": 8172,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/8172/drx_kingen_2022_split_2.png",
                            "last_name": "Seong-hoon",
                            "modified_at": "2026-02-01T11:16:32Z",
                            "name": "Kingen",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "kingen"
                          },
                          "player_id": 8172,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "keystone": {
                                "id": 40,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/5ccdfe9ed87cb8935b6a387a885410a8.png",
                                "name": "Grasp of the Undying",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 43,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/95b7572a3073bdf1640d7132365b01c8.png",
                                  "name": "Demolish",
                                  "type": "slot1"
                                },
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 49,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
                                  "name": "Overgrowth",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 66,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/95271ed6-8b6c-4fe2-9a41-bef3646114ea.png",
                                "name": "Health Scaling",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 117253,
                            "dealt_percentage": 17.65,
                            "dealt_to_champions": 16294,
                            "dealt_to_champions_percentage": 24.64,
                            "taken": 29490
                          },
                          "total_heal": 1291,
                          "total_time_crowd_control_dealt": 1166,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 3439,
                            "dealt_percentage": 10.32,
                            "dealt_to_champions": 3439,
                            "dealt_to_champions_percentage": 37.41,
                            "taken": 4073
                          },
                          "wards": {
                            "placed": 22,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 12
                          },
                          "wards_placed": 22
                        },
                        {
                          "assists": 11,
                          "champion": {
                            "id": 3175,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/499d8d59-146b-43de-a271-0198158b887a.png",
                            "name": "Renata Glasc",
                            "slug": "Renata"
                          },
                          "creep_score": 32,
                          "cs_at_14": 9,
                          "cs_diff_at_14": 1,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239288,
                          "gold_earned": 7865,
                          "gold_percentage": 14.62,
                          "gold_spent": 7600,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2761,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b4754269-dc0f-474a-a3b4-c181b7d6d26c.png",
                              "is_trinket": false,
                              "name": "Shurelya's Battlesong"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 3007,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a53f4c97c8d30ad58cb978e397107463.png",
                              "is_trinket": false,
                              "name": "Chemtech Putrifier"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 0,
                            "players": 1,
                            "turrets": 0,
                            "wards": 19
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
                            "dealt": 22345,
                            "dealt_percentage": 7.4,
                            "dealt_to_champions": 3840,
                            "dealt_to_champions_percentage": 11.24,
                            "taken": 7258
                          },
                          "masteries": [],
                          "minions_killed": 32,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 7838,
                            "dealt_percentage": 2.38,
                            "dealt_to_champions": 1136,
                            "dealt_to_champions_percentage": 4.99,
                            "taken": 6979
                          },
                          "player": {
                            "active": true,
                            "age": 28,
                            "birthday": "1997-04-01",
                            "first_name": "Cho",
                            "id": 15425,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/15425/drx_bery_l_2022_split_2.png",
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
                            "primary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "keystone": {
                                "id": 42,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ded20bb65d8b80ffaf6408be45136628.png",
                                "name": "Guardian",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 45,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/592200e1a39d2281977fc92d788cacd1.png",
                                  "name": "Shield Bash",
                                  "type": "slot1"
                                },
                                {
                                  "id": 48,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6054dc49089750c7d576b8e157228f29.png",
                                  "name": "Bone Plating",
                                  "type": "slot2"
                                },
                                {
                                  "id": 51,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                                  "name": "Unflinching",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 1,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                              "lesser_runes": [
                                {
                                  "id": 6,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/faae66d46ae5bc177a56890342087ac2.png",
                                  "name": "Taste of Blood",
                                  "type": "slot1"
                                },
                                {
                                  "id": 13,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/623d21bc9acd874af4f1c2150bdd7150.png",
                                  "name": "Relentless Hunter",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Domination",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 33182,
                            "dealt_percentage": 5,
                            "dealt_to_champions": 7121,
                            "dealt_to_champions_percentage": 10.77,
                            "taken": 15733
                          },
                          "total_heal": 1352,
                          "total_time_crowd_control_dealt": 290,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 2999,
                            "dealt_percentage": 9,
                            "dealt_to_champions": 2144,
                            "dealt_to_champions_percentage": 23.32,
                            "taken": 1496
                          },
                          "wards": {
                            "placed": 46,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 16
                          },
                          "wards_placed": 46
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3177,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/bf77b476-a4b2-4433-a896-13d082b51644.png",
                            "name": "Varus",
                            "slug": "Varus"
                          },
                          "creep_score": 285,
                          "cs_at_14": 132,
                          "cs_diff_at_14": 44,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": true
                          },
                          "game_id": 239288,
                          "gold_earned": 13881,
                          "gold_percentage": 23.1,
                          "gold_spent": 12125,
                          "items": [
                            {
                              "id": 2544,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/924cb9f122b90bf1ee29b9650c092524.png",
                              "is_trinket": false,
                              "name": "Guinsoo's Rageblade"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2699,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0f33f102856e8d40f6d38ff057856e1d.png",
                              "is_trinket": false,
                              "name": "Immortal Shieldbow"
                            },
                            {
                              "id": 2930,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/5bc313a2ec67cebd731e4cf0549cb077.png",
                              "is_trinket": false,
                              "name": "Wit's End"
                            },
                            {
                              "id": 3043,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3c9dee81-cfff-4920-87ad-e0516ac0fc92.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 44,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 34,
                            "players": 2,
                            "turrets": 4,
                            "wards": 5
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 239,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 26683,
                            "dealt_percentage": 8.99,
                            "dealt_to_champions": 5016,
                            "dealt_to_champions_percentage": 9.86,
                            "taken": 2239
                          },
                          "masteries": [],
                          "minions_killed": 285,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 169786,
                            "dealt_percentage": 44.1,
                            "dealt_to_champions": 11713,
                            "dealt_to_champions_percentage": 38.63,
                            "taken": 4692
                          },
                          "player": {
                            "active": true,
                            "age": 24,
                            "birthday": "2002-02-06",
                            "first_name": "Lee",
                            "id": 19285,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/19285/t1_gumayusi_2023_split_2.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 28,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d11f16420cc7a65ce1f1253d0adf5459.png",
                                "name": "Lethal Tempo",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 31,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/e8a57b03d6f13c42c79c579254920a11.png",
                                  "name": "Overheal",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 37,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6c94f0110a44559cdcab24911a21b452.png",
                                  "name": "Coup de Grace",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 30,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/62cc94a564835cd3abd80d74346c35da.png",
                              "name": "Heal"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 207506,
                            "dealt_percentage": 28.99,
                            "dealt_to_champions": 17365,
                            "dealt_to_champions_percentage": 20.86,
                            "taken": 7134
                          },
                          "total_heal": 1706,
                          "total_time_crowd_control_dealt": 399,
                          "total_units_healed": 4,
                          "true_damage": {
                            "dealt": 11036,
                            "dealt_percentage": 32.27,
                            "dealt_to_champions": 634,
                            "dealt_to_champions_percentage": 30.75,
                            "taken": 202
                          },
                          "wards": {
                            "placed": 17,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 8
                          },
                          "wards_placed": 17
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 3120,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/cbc53ec5b2ef342a710ba2c56ca13915.png",
                            "name": "Viego",
                            "slug": "Viego"
                          },
                          "creep_score": 180,
                          "cs_at_14": 89,
                          "cs_diff_at_14": -12,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239288,
                          "gold_earned": 10335,
                          "gold_percentage": 19.21,
                          "gold_spent": 10200,
                          "items": [
                            {
                              "id": 2451,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/7c23780ddc70d6db6bdbaff941acf146.png",
                              "is_trinket": false,
                              "name": "Chain Vest"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2537,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                              "is_trinket": false,
                              "name": "Mercury's Treads"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2927,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a3d78560d3945a73d66da14f28d6b759.png",
                              "is_trinket": false,
                              "name": "Black Cleaver"
                            },
                            {
                              "id": 2937,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0085138b38b1f85411988b1db668bc94.png",
                              "is_trinket": false,
                              "name": "Divine Sunderer"
                            },
                            {
                              "id": 3044,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d0e13016-50c3-4bf8-926c-a502cced78c4.png",
                              "is_trinket": false,
                              "name": "Broken Stopwatch"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 136,
                            "neutral_minions_enemy_jungle": 10,
                            "neutral_minions_team_jungle": 84,
                            "players": 2,
                            "turrets": 0,
                            "wards": 17
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
                            "dealt": 16987,
                            "dealt_percentage": 5.63,
                            "dealt_to_champions": 1700,
                            "dealt_to_champions_percentage": 4.98,
                            "taken": 10971
                          },
                          "masteries": [],
                          "minions_killed": 180,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 122584,
                            "dealt_percentage": 37.24,
                            "dealt_to_champions": 9232,
                            "dealt_to_champions_percentage": 40.53,
                            "taken": 14472
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-03-21",
                            "first_name": "Hong",
                            "id": 24996,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/24996/tl_pyosik_2023_split_1.png",
                            "last_name": "Chang-hyeon",
                            "modified_at": "2026-02-08T13:14:45Z",
                            "name": "Pyosik",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "pyosik"
                          },
                          "player_id": 24996,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 35,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                                  "name": "Legend: Tenacity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 37,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6c94f0110a44559cdcab24911a21b452.png",
                                  "name": "Coup de Grace",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 19,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                  "name": "Magical Footwear",
                                  "type": "slot1"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 155467,
                            "dealt_percentage": 23.4,
                            "dealt_to_champions": 12022,
                            "dealt_to_champions_percentage": 18.18,
                            "taken": 25693
                          },
                          "total_heal": 13393,
                          "total_time_crowd_control_dealt": 245,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 15895,
                            "dealt_percentage": 47.72,
                            "dealt_to_champions": 1089,
                            "dealt_to_champions_percentage": 11.85,
                            "taken": 250
                          },
                          "wards": {
                            "placed": 14,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 20
                          },
                          "wards_placed": 14
                        },
                        {
                          "assists": 3,
                          "champion": {
                            "id": 3185,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/73d079e4-ba42-48a1-8a29-dae7f95b9587.png",
                            "name": "Sylas",
                            "slug": "Sylas"
                          },
                          "creep_score": 277,
                          "cs_at_14": 130,
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
                          "game_id": 239288,
                          "gold_earned": 13849,
                          "gold_percentage": 25.74,
                          "gold_spent": 13650,
                          "items": [
                            {
                              "id": 2534,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/73578d8f7a2a451b61696009016c134a.png",
                              "is_trinket": false,
                              "name": "Fiendish Codex"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2814,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                              "is_trinket": false,
                              "name": "Rabadon's Deathcap"
                            },
                            {
                              "id": 2909,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/7ec8f413ab83b109852d5c3fd7c5b197.png",
                              "is_trinket": false,
                              "name": "Shadowflame"
                            },
                            {
                              "id": 2910,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a8377226b797197fdb941b2fad4123cb.png",
                              "is_trinket": false,
                              "name": "Everfrost"
                            },
                            {
                              "id": 3044,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d0e13016-50c3-4bf8-926c-a502cced78c4.png",
                              "is_trinket": false,
                              "name": "Broken Stopwatch"
                            }
                          ],
                          "kills": 5,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 23,
                            "neutral_minions_enemy_jungle": 4,
                            "neutral_minions_team_jungle": 18,
                            "players": 5,
                            "turrets": 2,
                            "wards": 8
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
                          "level": 16,
                          "magic_damage": {
                            "dealt": 178421,
                            "dealt_percentage": 59.11,
                            "dealt_to_champions": 17836,
                            "dealt_to_champions_percentage": 52.21,
                            "taken": 14010
                          },
                          "masteries": [],
                          "minions_killed": 277,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 6553,
                            "dealt_percentage": 1.99,
                            "dealt_to_champions": 377,
                            "dealt_to_champions_percentage": 1.66,
                            "taken": 12659
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-11-28",
                            "first_name": "Kim",
                            "id": 25391,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/25391/drx_zeka_2022_split_2.png",
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
                            "primary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "keystone": {
                                "id": 65,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/13598521aebb0be68b52982d46aa1b1c.png",
                                "name": "First Strike",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 19,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                  "name": "Magical Footwear",
                                  "type": "slot1"
                                },
                                {
                                  "id": 22,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/11c92222e3b798ce1ff524d34b3297f1.png",
                                  "name": "Minion Dematerializer",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 49,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
                                  "name": "Overgrowth",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 191270,
                            "dealt_percentage": 28.79,
                            "dealt_to_champions": 20733,
                            "dealt_to_champions_percentage": 31.35,
                            "taken": 29122
                          },
                          "total_heal": 4462,
                          "total_time_crowd_control_dealt": 510,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 6295,
                            "dealt_percentage": 18.9,
                            "dealt_to_champions": 2520,
                            "dealt_to_champions_percentage": 27.42,
                            "taken": 2451
                          },
                          "wards": {
                            "placed": 12,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 11
                          },
                          "wards_placed": 12
                        },
                        {
                          "assists": 7,
                          "champion": {
                            "id": 3016,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/e7eb3fb357e71d7673434cef9ca1ffe2.png",
                            "name": "Gragas",
                            "slug": "Gragas"
                          },
                          "creep_score": 150,
                          "cs_at_14": 96,
                          "cs_diff_at_14": -7,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239288,
                          "gold_earned": 10766,
                          "gold_percentage": 17.92,
                          "gold_spent": 9200,
                          "items": [
                            {
                              "id": 2465,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/167abf5d0dc59292a78b79ceadffcc99.png",
                              "is_trinket": false,
                              "name": "Negatron Cloak"
                            },
                            {
                              "id": 2659,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/afe5e3df08a76a4c10753ecd5da4273d.png",
                              "is_trinket": false,
                              "name": "Winged Moonplate"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2830,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/4a236638d83dc2546184646200a5042a.png",
                              "is_trinket": false,
                              "name": "Frozen Heart"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 3019,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/5c65145d1a8bab82316337cd7e27cd6c.png",
                              "is_trinket": false,
                              "name": "Frostfire Gauntlet"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 0,
                            "players": 2,
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
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 64497,
                            "dealt_percentage": 21.74,
                            "dealt_to_champions": 13729,
                            "dealt_to_champions_percentage": 26.99,
                            "taken": 11242
                          },
                          "masteries": [],
                          "minions_killed": 150,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 18725,
                            "dealt_percentage": 4.86,
                            "dealt_to_champions": 1813,
                            "dealt_to_champions_percentage": 5.98,
                            "taken": 15049
                          },
                          "player": {
                            "active": true,
                            "age": 22,
                            "birthday": "2004-01-31",
                            "first_name": "Choi",
                            "id": 31391,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31391/t1_zeus_2023_split_2.png",
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
                            "primary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "keystone": {
                                "id": 40,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/5ccdfe9ed87cb8935b6a387a885410a8.png",
                                "name": "Grasp of the Undying",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 43,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/95b7572a3073bdf1640d7132365b01c8.png",
                                  "name": "Demolish",
                                  "type": "slot1"
                                },
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 51,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                                  "name": "Unflinching",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 92881,
                            "dealt_percentage": 12.97,
                            "dealt_to_champions": 15762,
                            "dealt_to_champions_percentage": 18.93,
                            "taken": 27155
                          },
                          "total_heal": 15822,
                          "total_time_crowd_control_dealt": 919,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 9658,
                            "dealt_percentage": 28.24,
                            "dealt_to_champions": 218,
                            "dealt_to_champions_percentage": 10.57,
                            "taken": 863
                          },
                          "wards": {
                            "placed": 15,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 10
                          },
                          "wards_placed": 15
                        },
                        {
                          "assists": 2,
                          "champion": {
                            "id": 3017,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/839eb7d1426303e65005ce5348fca00d.png",
                            "name": "Graves",
                            "slug": "Graves"
                          },
                          "creep_score": 243,
                          "cs_at_14": 101,
                          "cs_diff_at_14": 12,
                          "deaths": 4,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239288,
                          "gold_earned": 12570,
                          "gold_percentage": 20.92,
                          "gold_spent": 11850,
                          "items": [
                            {
                              "id": 2450,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/5ff4236356a2fc30dd646724b53a5354.png",
                              "is_trinket": false,
                              "name": "Cloth Armor"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2927,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a3d78560d3945a73d66da14f28d6b759.png",
                              "is_trinket": false,
                              "name": "Black Cleaver"
                            },
                            {
                              "id": 2935,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97032f4cae42f011b132d0bca2438e8b.png",
                              "is_trinket": false,
                              "name": "Goredrinker"
                            },
                            {
                              "id": 2963,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b024e8ca8cf9873201744933ec14c30c.png",
                              "is_trinket": false,
                              "name": "Umbral Glaive"
                            },
                            {
                              "id": 3044,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d0e13016-50c3-4bf8-926c-a502cced78c4.png",
                              "is_trinket": false,
                              "name": "Broken Stopwatch"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 148,
                            "neutral_minions_enemy_jungle": 22,
                            "neutral_minions_team_jungle": 84,
                            "players": 2,
                            "turrets": 3,
                            "wards": 25
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
                          "level": 15,
                          "magic_damage": {
                            "dealt": 9225,
                            "dealt_percentage": 3.11,
                            "dealt_to_champions": 934,
                            "dealt_to_champions_percentage": 1.84,
                            "taken": 10792
                          },
                          "masteries": [],
                          "minions_killed": 243,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 178283,
                            "dealt_percentage": 46.31,
                            "dealt_to_champions": 14911,
                            "dealt_to_champions_percentage": 49.18,
                            "taken": 9479
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-12-24",
                            "first_name": "Moon",
                            "id": 31392,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                            "last_name": "Hyeon-joon",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "Oner",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "oner"
                          },
                          "player_id": 31392,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 29,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d7dee9f79afc995429521e2b586aae87.png",
                                "name": "Fleet Footwork",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 1,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                              "lesser_runes": [
                                {
                                  "id": 8,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a5317349f8ce3e0923fe970e5232bf30.png",
                                  "name": "Zombie Ward",
                                  "type": "slot2"
                                },
                                {
                                  "id": 11,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/569a1e7d3c46d9731392616eccebdd9c.png",
                                  "name": "Treasure Hunter",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Domination",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 200161,
                            "dealt_percentage": 27.96,
                            "dealt_to_champions": 16201,
                            "dealt_to_champions_percentage": 19.46,
                            "taken": 20887
                          },
                          "total_heal": 9107,
                          "total_time_crowd_control_dealt": 476,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 12652,
                            "dealt_percentage": 36.99,
                            "dealt_to_champions": 356,
                            "dealt_to_champions_percentage": 17.26,
                            "taken": 615
                          },
                          "wards": {
                            "placed": 37,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 9
                          },
                          "wards_placed": 37
                        }
                      ],
                      "position": 3,
                      "status": "finished",
                      "teams": [
                        {
                          "atakhan_kills": null,
                          "bans": [
                            2982,
                            3166,
                            3085,
                            3040,
                            2989
                          ],
                          "baron_kills": 2,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 2,
                          "color": "blue",
                          "dragon_kills": 3,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": true,
                          "first_blood": false,
                          "first_dragon": false,
                          "first_herald": false,
                          "first_inhibitor": true,
                          "first_tower": true,
                          "first_voidgrub": null,
                          "gold_earned": 60092,
                          "herald_kills": 0,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 2,
                          "kills": 12,
                          "mountain_drake_kills": 0,
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
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "tower_kills": 10,
                          "voidgrub_kills": null
                        },
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3129,
                            3131,
                            3189,
                            3152,
                            3156
                          ],
                          "baron_kills": 0,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 1,
                          "color": "red",
                          "dragon_kills": 2,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": false,
                          "first_blood": true,
                          "first_dragon": true,
                          "first_herald": true,
                          "first_inhibitor": false,
                          "first_tower": false,
                          "first_voidgrub": null,
                          "gold_earned": 53807,
                          "herald_kills": 2,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 0,
                          "kills": 12,
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
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "tower_kills": 3,
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
                      "begin_at": "2022-11-06T01:45:11Z",
                      "complete": true,
                      "detailed_stats": true,
                      "end_at": "2022-11-06T02:37:39Z",
                      "finished": true,
                      "forfeit": false,
                      "id": 239287,
                      "length": 2771,
                      "match_id": 651268,
                      "players": [
                        {
                          "assists": 2,
                          "champion": {
                            "id": 3121,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/1a602e7dc475be3ca9ccba41689c71d3.png",
                            "name": "Viktor",
                            "slug": "Viktor"
                          },
                          "creep_score": 406,
                          "cs_at_14": 111,
                          "cs_diff_at_14": -27,
                          "deaths": 5,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239287,
                          "gold_earned": 19088,
                          "gold_percentage": 23.99,
                          "gold_spent": 18025,
                          "items": [
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2814,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                              "is_trinket": false,
                              "name": "Rabadon's Deathcap"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2908,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/e6408582a9edbfc6d6896b3dc2631cd7.png",
                              "is_trinket": false,
                              "name": "Crown of the Shattered Queen"
                            },
                            {
                              "id": 2923,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f0afeb951bcd89aa997e963f075bae83.png",
                              "is_trinket": false,
                              "name": "Lich Bane"
                            },
                            {
                              "id": 3048,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/e8bca3b0-24da-479e-9fa7-13f2021cc106.png",
                              "is_trinket": false,
                              "name": "Zhonya's Hourglass"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 29,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 27,
                            "players": 4,
                            "turrets": 2,
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
                          "level": 18,
                          "magic_damage": {
                            "dealt": 340173,
                            "dealt_percentage": 82.77,
                            "dealt_to_champions": 41078,
                            "dealt_to_champions_percentage": 75.06,
                            "taken": 10312
                          },
                          "masteries": [],
                          "minions_killed": 406,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 17306,
                            "dealt_percentage": 2.13,
                            "dealt_to_champions": 1251,
                            "dealt_to_champions_percentage": 2.14,
                            "taken": 13584
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-05-07",
                            "first_name": "Lee",
                            "id": 585,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                            "last_name": "Sang-hyeok",
                            "modified_at": "2026-02-01T11:19:16Z",
                            "name": "Faker",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "faker"
                          },
                          "player_id": 585,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "keystone": {
                                "id": 65,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/13598521aebb0be68b52982d46aa1b1c.png",
                                "name": "First Strike",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 20,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a32387cef55cc07757a3175348d9dff3.png",
                                  "name": "Triple Tonic",
                                  "type": "slot1"
                                },
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "lesser_runes": [
                                {
                                  "id": 56,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                  "name": "Manaflow Band",
                                  "type": "slot1"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 367575,
                            "dealt_percentage": 28.87,
                            "dealt_to_champions": 43895,
                            "dealt_to_champions_percentage": 37.23,
                            "taken": 24425
                          },
                          "total_heal": 4698,
                          "total_time_crowd_control_dealt": 573,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 10094,
                            "dealt_percentage": 20.19,
                            "dealt_to_champions": 1564,
                            "dealt_to_champions_percentage": 32.99,
                            "taken": 528
                          },
                          "wards": {
                            "placed": 28,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 13
                          },
                          "wards_placed": 28
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 3177,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/bf77b476-a4b2-4433-a896-13d082b51644.png",
                            "name": "Varus",
                            "slug": "Varus"
                          },
                          "creep_score": 391,
                          "cs_at_14": 102,
                          "cs_diff_at_14": -15,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": true,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239287,
                          "gold_earned": 19904,
                          "gold_percentage": 24.72,
                          "gold_spent": 16925,
                          "items": [
                            {
                              "id": 2580,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/8017be65dd3b762a53bf8f5efbb4eaef.png",
                              "is_trinket": false,
                              "name": "Edge of Night"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2768,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/ae4031f648750bf108e58bbf8e97959a.png",
                              "is_trinket": false,
                              "name": "Serpent's Fang"
                            },
                            {
                              "id": 2811,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/28719589de63ed2332d29dd334b368e0.png",
                              "is_trinket": false,
                              "name": "Muramana"
                            },
                            {
                              "id": 2825,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3a6f184fabcf0b060a35cfe67ac8a530.png",
                              "is_trinket": false,
                              "name": "Serylda's Grudge"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2912,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/eaef5f4c2f6f2d5fcf13f287c321e59b.png",
                              "is_trinket": false,
                              "name": "Eclipse"
                            }
                          ],
                          "kills": 6,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 33,
                            "neutral_minions_enemy_jungle": 1,
                            "neutral_minions_team_jungle": 27,
                            "players": 6,
                            "turrets": 2,
                            "wards": 12
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 6,
                          "largest_multi_kill": 2,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 16994,
                            "dealt_percentage": 4.5,
                            "dealt_to_champions": 3868,
                            "dealt_to_champions_percentage": 9.27,
                            "taken": 7226
                          },
                          "masteries": [],
                          "minions_killed": 391,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 365574,
                            "dealt_percentage": 51.13,
                            "dealt_to_champions": 36424,
                            "dealt_to_champions_percentage": 63.97,
                            "taken": 10559
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-10-23",
                            "first_name": "Kim",
                            "id": 2169,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/2169/ezgif_3_4d5729796f.png",
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
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 53,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/b8282c680e5d022dc564c54937a20a26.png",
                                "name": "Arcane Comet",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 56,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                  "name": "Manaflow Band",
                                  "type": "slot1"
                                },
                                {
                                  "id": 58,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/632a47c2a88802029838e383a866feb1.png",
                                  "name": "Transcendence",
                                  "type": "slot2"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 19,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                  "name": "Magical Footwear",
                                  "type": "slot1"
                                },
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 23,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/65eea722a1fc79fb6469e7246eb0afb8.png",
                              "name": "Cleanse"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 390020,
                            "dealt_percentage": 32.83,
                            "dealt_to_champions": 41044,
                            "dealt_to_champions_percentage": 37.12,
                            "taken": 18172
                          },
                          "total_heal": 8316,
                          "total_time_crowd_control_dealt": 718,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 7451,
                            "dealt_percentage": 7.8,
                            "dealt_to_champions": 751,
                            "dealt_to_champions_percentage": 6.31,
                            "taken": 386
                          },
                          "wards": {
                            "placed": 26,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 9
                          },
                          "wards_placed": 26
                        },
                        {
                          "assists": 10,
                          "champion": {
                            "id": 3050,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/448b64984852009cfb8f0224aa7c4889.png",
                            "name": "Lux",
                            "slug": "Lux"
                          },
                          "creep_score": 32,
                          "cs_at_14": 7,
                          "cs_diff_at_14": 1,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239287,
                          "gold_earned": 10658,
                          "gold_percentage": 13.39,
                          "gold_spent": 10000,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2566,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/e09b668319c871385af2c51023e7e0f9.png",
                              "is_trinket": false,
                              "name": "Mikael's Blessing"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2910,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a8377226b797197fdb941b2fad4123cb.png",
                              "is_trinket": false,
                              "name": "Everfrost"
                            },
                            {
                              "id": 3016,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b4e5bb16fbc4368c43c9712a2a154e6f.png",
                              "is_trinket": false,
                              "name": "Oblivion Orb"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 2,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 2,
                            "players": 1,
                            "turrets": 0,
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
                          "largest_multi_kill": 1,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 57023,
                            "dealt_percentage": 13.88,
                            "dealt_to_champions": 10176,
                            "dealt_to_champions_percentage": 18.59,
                            "taken": 4674
                          },
                          "masteries": [],
                          "minions_killed": 32,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 7563,
                            "dealt_percentage": 0.93,
                            "dealt_to_champions": 605,
                            "dealt_to_champions_percentage": 1.04,
                            "taken": 8147
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-10-14",
                            "first_name": "Ryu",
                            "id": 8158,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                            "last_name": "Min-seok",
                            "modified_at": "2026-02-01T11:19:16Z",
                            "name": "Keria",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "keria"
                          },
                          "player_id": 8158,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "keystone": {
                                "id": 65,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/13598521aebb0be68b52982d46aa1b1c.png",
                                "name": "First Strike",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 20,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a32387cef55cc07757a3175348d9dff3.png",
                                  "name": "Triple Tonic",
                                  "type": "slot1"
                                },
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "lesser_runes": [
                                {
                                  "id": 56,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                  "name": "Manaflow Band",
                                  "type": "slot1"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 66392,
                            "dealt_percentage": 5.22,
                            "dealt_to_champions": 12588,
                            "dealt_to_champions_percentage": 10.68,
                            "taken": 14536
                          },
                          "total_heal": 2837,
                          "total_time_crowd_control_dealt": 488,
                          "total_units_healed": 4,
                          "true_damage": {
                            "dealt": 1806,
                            "dealt_percentage": 3.61,
                            "dealt_to_champions": 1806,
                            "dealt_to_champions_percentage": 38.09,
                            "taken": 1714
                          },
                          "wards": {
                            "placed": 83,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 28
                          },
                          "wards_placed": 83
                        },
                        {
                          "assists": 10,
                          "champion": {
                            "id": 2997,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/985146cb1fb2beef0affd8d5fadc7451.png",
                            "name": "Camille",
                            "slug": "Camille"
                          },
                          "creep_score": 350,
                          "cs_at_14": 119,
                          "cs_diff_at_14": 8,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239287,
                          "gold_earned": 17288,
                          "gold_percentage": 21.47,
                          "gold_spent": 14400,
                          "items": [
                            {
                              "id": 2465,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/167abf5d0dc59292a78b79ceadffcc99.png",
                              "is_trinket": false,
                              "name": "Negatron Cloak"
                            },
                            {
                              "id": 2502,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c2f632ddae06a3c43e2a15a173c2229f.png",
                              "is_trinket": false,
                              "name": "Phage"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2928,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6a940e698e30b4298a0e176358d10a66.png",
                              "is_trinket": false,
                              "name": "Ravenous Hydra"
                            },
                            {
                              "id": 2937,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0085138b38b1f85411988b1db668bc94.png",
                              "is_trinket": false,
                              "name": "Divine Sunderer"
                            },
                            {
                              "id": 3047,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f45da294-c8ab-4d20-9216-d887579dc26d.png",
                              "is_trinket": false,
                              "name": "Guardian Angel"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 37,
                            "neutral_minions_enemy_jungle": 11,
                            "neutral_minions_team_jungle": 20,
                            "players": 4,
                            "turrets": 3,
                            "wards": 24
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 3,
                          "largest_multi_kill": 1,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 1210,
                            "dealt_percentage": 0.32,
                            "dealt_to_champions": 1210,
                            "dealt_to_champions_percentage": 2.9,
                            "taken": 15541
                          },
                          "masteries": [],
                          "minions_killed": 350,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 190660,
                            "dealt_percentage": 26.67,
                            "dealt_to_champions": 11908,
                            "dealt_to_champions_percentage": 20.91,
                            "taken": 29705
                          },
                          "player": {
                            "active": true,
                            "age": 26,
                            "birthday": "2000-03-11",
                            "first_name": "Hwang",
                            "id": 8172,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/8172/drx_kingen_2022_split_2.png",
                            "last_name": "Seong-hoon",
                            "modified_at": "2026-02-01T11:16:32Z",
                            "name": "Kingen",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "kingen"
                          },
                          "player_id": 8172,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "keystone": {
                                "id": 40,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/5ccdfe9ed87cb8935b6a387a885410a8.png",
                                "name": "Grasp of the Undying",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 45,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/592200e1a39d2281977fc92d788cacd1.png",
                                  "name": "Shield Bash",
                                  "type": "slot1"
                                },
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 49,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
                                  "name": "Overgrowth",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 240712,
                            "dealt_percentage": 20.26,
                            "dealt_to_champions": 19714,
                            "dealt_to_champions_percentage": 17.83,
                            "taken": 46490
                          },
                          "total_heal": 21956,
                          "total_time_crowd_control_dealt": 236,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 48841,
                            "dealt_percentage": 51.14,
                            "dealt_to_champions": 6595,
                            "dealt_to_champions_percentage": 55.41,
                            "taken": 1243
                          },
                          "wards": {
                            "placed": 16,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 16
                          },
                          "wards_placed": 16
                        },
                        {
                          "assists": 8,
                          "champion": {
                            "id": 3020,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/fde39f7fc210740c1c136b9d7af54de4.png",
                            "name": "Heimerdinger",
                            "slug": "Heimerdinger"
                          },
                          "creep_score": 65,
                          "cs_at_14": 6,
                          "cs_diff_at_14": -1,
                          "deaths": 4,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239287,
                          "gold_earned": 11288,
                          "gold_percentage": 14.02,
                          "gold_spent": 10275,
                          "items": [
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2871,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/8cef60e74adf20cb8372afd4aa49cde9.png",
                              "is_trinket": false,
                              "name": "Liandry's Anguish"
                            },
                            {
                              "id": 2924,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d4fde29e50e7ed8472b31f4a78134063.png",
                              "is_trinket": false,
                              "name": "Rylai's Crystal Scepter"
                            },
                            {
                              "id": 3016,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b4e5bb16fbc4368c43c9712a2a154e6f.png",
                              "is_trinket": false,
                              "name": "Oblivion Orb"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 18,
                            "neutral_minions_enemy_jungle": 4,
                            "neutral_minions_team_jungle": 6,
                            "players": 1,
                            "turrets": 0,
                            "wards": 23
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
                            "dealt": 56978,
                            "dealt_percentage": 15.09,
                            "dealt_to_champions": 14167,
                            "dealt_to_champions_percentage": 33.94,
                            "taken": 9543
                          },
                          "masteries": [],
                          "minions_killed": 65,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 4686,
                            "dealt_percentage": 0.66,
                            "dealt_to_champions": 247,
                            "dealt_to_champions_percentage": 0.43,
                            "taken": 12142
                          },
                          "player": {
                            "active": true,
                            "age": 28,
                            "birthday": "1997-04-01",
                            "first_name": "Cho",
                            "id": 15425,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/15425/drx_bery_l_2022_split_2.png",
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
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 53,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/b8282c680e5d022dc564c54937a20a26.png",
                                "name": "Arcane Comet",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 56,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                  "name": "Manaflow Band",
                                  "type": "slot1"
                                },
                                {
                                  "id": 59,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/732d4e2a7fdf6ecc3ec8e42504a111b9.png",
                                  "name": "Celerity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 1,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                              "lesser_runes": [
                                {
                                  "id": 6,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/faae66d46ae5bc177a56890342087ac2.png",
                                  "name": "Taste of Blood",
                                  "type": "slot1"
                                },
                                {
                                  "id": 11,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/569a1e7d3c46d9731392616eccebdd9c.png",
                                  "name": "Treasure Hunter",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Domination",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 65452,
                            "dealt_percentage": 5.51,
                            "dealt_to_champions": 16778,
                            "dealt_to_champions_percentage": 15.17,
                            "taken": 22587
                          },
                          "total_heal": 7214,
                          "total_time_crowd_control_dealt": 201,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 3788,
                            "dealt_percentage": 3.97,
                            "dealt_to_champions": 2363,
                            "dealt_to_champions_percentage": 19.85,
                            "taken": 901
                          },
                          "wards": {
                            "placed": 79,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 25
                          },
                          "wards_placed": 79
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 2989,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/4c292dfc73999728a4e0d2d339587781.png",
                            "name": "Ashe",
                            "slug": "Ashe"
                          },
                          "creep_score": 364,
                          "cs_at_14": 117,
                          "cs_diff_at_14": 15,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239287,
                          "gold_earned": 16027,
                          "gold_percentage": 20.14,
                          "gold_spent": 14850,
                          "items": [
                            {
                              "id": 2637,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f3b2568b72a4c1fe05c69d2ac8aaf653.png",
                              "is_trinket": false,
                              "name": "Pickaxe"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2699,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0f33f102856e8d40f6d38ff057856e1d.png",
                              "is_trinket": false,
                              "name": "Immortal Shieldbow"
                            },
                            {
                              "id": 2763,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1a0dab15964871b507375c342d5536bc.png",
                              "is_trinket": false,
                              "name": "Runaan's Hurricane"
                            },
                            {
                              "id": 2820,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/82133cdb92c1ca86e27b1e021faa84e9.png",
                              "is_trinket": false,
                              "name": "Lord Dominik's Regards"
                            },
                            {
                              "id": 3047,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f45da294-c8ab-4d20-9216-d887579dc26d.png",
                              "is_trinket": false,
                              "name": "Guardian Angel"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 23,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 24,
                            "players": 1,
                            "turrets": 1,
                            "wards": 15
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 455,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 17,
                          "magic_damage": {
                            "dealt": 2958,
                            "dealt_percentage": 0.72,
                            "dealt_to_champions": 2505,
                            "dealt_to_champions_percentage": 4.58,
                            "taken": 6760
                          },
                          "masteries": [],
                          "minions_killed": 364,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 243648,
                            "dealt_percentage": 30,
                            "dealt_to_champions": 11999,
                            "dealt_to_champions_percentage": 20.54,
                            "taken": 13880
                          },
                          "player": {
                            "active": true,
                            "age": 24,
                            "birthday": "2002-02-06",
                            "first_name": "Lee",
                            "id": 19285,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/19285/t1_gumayusi_2023_split_2.png",
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
                            "primary_path": {
                              "id": 1,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                              "keystone": {
                                "id": 4,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1ab13ffc6925224014ace2e7e298000b.png",
                                "name": "Hail of Blades",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 6,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/faae66d46ae5bc177a56890342087ac2.png",
                                  "name": "Taste of Blood",
                                  "type": "slot1"
                                },
                                {
                                  "id": 8,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a5317349f8ce3e0923fe970e5232bf30.png",
                                  "name": "Zombie Ward",
                                  "type": "slot2"
                                },
                                {
                                  "id": 14,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c9305f3dcdc9b6711f90df9e6e0c849c.png",
                                  "name": "Ultimate Hunter",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Domination",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 25,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a4255e601a7f222a442803bca6f088cf.png",
                                  "name": "Approach Velocity",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 23,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/65eea722a1fc79fb6469e7246eb0afb8.png",
                              "name": "Cleanse"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 257478,
                            "dealt_percentage": 20.23,
                            "dealt_to_champions": 14569,
                            "dealt_to_champions_percentage": 12.36,
                            "taken": 20830
                          },
                          "total_heal": 4039,
                          "total_time_crowd_control_dealt": 1083,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 10872,
                            "dealt_percentage": 21.75,
                            "dealt_to_champions": 64,
                            "dealt_to_champions_percentage": 1.35,
                            "taken": 189
                          },
                          "wards": {
                            "placed": 35,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 9
                          },
                          "wards_placed": 35
                        },
                        {
                          "assists": 10,
                          "champion": {
                            "id": 3120,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/cbc53ec5b2ef342a710ba2c56ca13915.png",
                            "name": "Viego",
                            "slug": "Viego"
                          },
                          "creep_score": 222,
                          "cs_at_14": 85,
                          "cs_diff_at_14": -19,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239287,
                          "gold_earned": 13566,
                          "gold_percentage": 16.85,
                          "gold_spent": 12325,
                          "items": [
                            {
                              "id": 2465,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/167abf5d0dc59292a78b79ceadffcc99.png",
                              "is_trinket": false,
                              "name": "Negatron Cloak"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2793,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3e1d3f42c8ef52ed8cc0338eb7873bb4.png",
                              "is_trinket": false,
                              "name": "Mortal Reminder"
                            },
                            {
                              "id": 2937,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0085138b38b1f85411988b1db668bc94.png",
                              "is_trinket": false,
                              "name": "Divine Sunderer"
                            },
                            {
                              "id": 3047,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f45da294-c8ab-4d20-9216-d887579dc26d.png",
                              "is_trinket": false,
                              "name": "Guardian Angel"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 160,
                            "neutral_minions_enemy_jungle": 12,
                            "neutral_minions_team_jungle": 107,
                            "players": 1,
                            "turrets": 2,
                            "wards": 41
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 446,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 17,
                          "magic_damage": {
                            "dealt": 20595,
                            "dealt_percentage": 5.46,
                            "dealt_to_champions": 1346,
                            "dealt_to_champions_percentage": 3.22,
                            "taken": 8504
                          },
                          "masteries": [],
                          "minions_killed": 222,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 145185,
                            "dealt_percentage": 20.31,
                            "dealt_to_champions": 8359,
                            "dealt_to_champions_percentage": 14.68,
                            "taken": 22240
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-03-21",
                            "first_name": "Hong",
                            "id": 24996,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/24996/tl_pyosik_2023_split_1.png",
                            "last_name": "Chang-hyeon",
                            "modified_at": "2026-02-08T13:14:45Z",
                            "name": "Pyosik",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "pyosik"
                          },
                          "player_id": 24996,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 35,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                                  "name": "Legend: Tenacity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 37,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6c94f0110a44559cdcab24911a21b452.png",
                                  "name": "Coup de Grace",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 19,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                  "name": "Magical Footwear",
                                  "type": "slot1"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 181740,
                            "dealt_percentage": 15.3,
                            "dealt_to_champions": 10773,
                            "dealt_to_champions_percentage": 9.74,
                            "taken": 32021
                          },
                          "total_heal": 17843,
                          "total_time_crowd_control_dealt": 243,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 15959,
                            "dealt_percentage": 16.71,
                            "dealt_to_champions": 1067,
                            "dealt_to_champions_percentage": 8.96,
                            "taken": 1276
                          },
                          "wards": {
                            "placed": 20,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 22
                          },
                          "wards_placed": 20
                        },
                        {
                          "assists": 2,
                          "champion": {
                            "id": 3185,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/73d079e4-ba42-48a1-8a29-dae7f95b9587.png",
                            "name": "Sylas",
                            "slug": "Sylas"
                          },
                          "creep_score": 415,
                          "cs_at_14": 138,
                          "cs_diff_at_14": 27,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239287,
                          "gold_earned": 18461,
                          "gold_percentage": 22.93,
                          "gold_spent": 18660,
                          "items": [
                            {
                              "id": 2537,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                              "is_trinket": false,
                              "name": "Mercury's Treads"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2814,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                              "is_trinket": false,
                              "name": "Rabadon's Deathcap"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2900,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3845e3fb0a405f681825dba02a138ff3.png",
                              "is_trinket": false,
                              "name": "Hextech Alternator"
                            },
                            {
                              "id": 2910,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a8377226b797197fdb941b2fad4123cb.png",
                              "is_trinket": false,
                              "name": "Everfrost"
                            },
                            {
                              "id": 3048,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/e8bca3b0-24da-479e-9fa7-13f2021cc106.png",
                              "is_trinket": false,
                              "name": "Zhonya's Hourglass"
                            }
                          ],
                          "kills": 5,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 33,
                            "neutral_minions_enemy_jungle": 2,
                            "neutral_minions_team_jungle": 28,
                            "players": 5,
                            "turrets": 2,
                            "wards": 25
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
                          "level": 18,
                          "magic_damage": {
                            "dealt": 281691,
                            "dealt_percentage": 74.63,
                            "dealt_to_champions": 21146,
                            "dealt_to_champions_percentage": 50.66,
                            "taken": 18910
                          },
                          "masteries": [],
                          "minions_killed": 415,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 8907,
                            "dealt_percentage": 1.25,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 20070
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-11-28",
                            "first_name": "Kim",
                            "id": 25391,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/25391/drx_zeka_2022_split_2.png",
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
                            "primary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "keystone": {
                                "id": 65,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/13598521aebb0be68b52982d46aa1b1c.png",
                                "name": "First Strike",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 19,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                  "name": "Magical Footwear",
                                  "type": "slot1"
                                },
                                {
                                  "id": 22,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/11c92222e3b798ce1ff524d34b3297f1.png",
                                  "name": "Minion Dematerializer",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 49,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
                                  "name": "Overgrowth",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 310060,
                            "dealt_percentage": 26.1,
                            "dealt_to_champions": 22273,
                            "dealt_to_champions_percentage": 20.14,
                            "taken": 39998
                          },
                          "total_heal": 12219,
                          "total_time_crowd_control_dealt": 624,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 19460,
                            "dealt_percentage": 20.38,
                            "dealt_to_champions": 1126,
                            "dealt_to_champions_percentage": 9.46,
                            "taken": 1018
                          },
                          "wards": {
                            "placed": 7,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 5
                          },
                          "wards_placed": 7
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3166,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/cad8d209-bda9-43f3-a7fa-cebce483ec37.png",
                            "name": "Aatrox",
                            "slug": "Aatrox"
                          },
                          "creep_score": 328,
                          "cs_at_14": 111,
                          "cs_diff_at_14": -8,
                          "deaths": 5,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239287,
                          "gold_earned": 16348,
                          "gold_percentage": 20.54,
                          "gold_spent": 15455,
                          "items": [
                            {
                              "id": 2504,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2912,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/eaef5f4c2f6f2d5fcf13f287c321e59b.png",
                              "is_trinket": false,
                              "name": "Eclipse"
                            },
                            {
                              "id": 2933,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/9eb16adb98fcdc9c9ae35eabe19c322f.png",
                              "is_trinket": false,
                              "name": "Maw of Malmortius"
                            },
                            {
                              "id": 2934,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6f38d2d2845b0958a9cf0c03b8d592a2.png",
                              "is_trinket": false,
                              "name": "Death's Dance"
                            },
                            {
                              "id": 3036,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f0f00af3-5f04-41c9-a24b-1d3d9439199f.png",
                              "is_trinket": false,
                              "name": "Chempunk Chainsword"
                            },
                            {
                              "id": 3043,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3c9dee81-cfff-4920-87ad-e0516ac0fc92.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            }
                          ],
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 44,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 29,
                            "players": 3,
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
                          "level": 18,
                          "magic_damage": {
                            "dealt": 0,
                            "dealt_percentage": 0,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 10851
                          },
                          "masteries": [],
                          "minions_killed": 328,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 248560,
                            "dealt_percentage": 30.61,
                            "dealt_to_champions": 20795,
                            "dealt_to_champions_percentage": 35.59,
                            "taken": 17207
                          },
                          "player": {
                            "active": true,
                            "age": 22,
                            "birthday": "2004-01-31",
                            "first_name": "Choi",
                            "id": 31391,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31391/t1_zeus_2023_split_2.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 35,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                                  "name": "Legend: Tenacity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 48,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6054dc49089750c7d576b8e157228f29.png",
                                  "name": "Bone Plating",
                                  "type": "slot2"
                                },
                                {
                                  "id": 51,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                                  "name": "Unflinching",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 256455,
                            "dealt_percentage": 20.15,
                            "dealt_to_champions": 20795,
                            "dealt_to_champions_percentage": 17.64,
                            "taken": 36282
                          },
                          "total_heal": 17611,
                          "total_time_crowd_control_dealt": 259,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 7895,
                            "dealt_percentage": 15.79,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 8224
                          },
                          "wards": {
                            "placed": 12,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 11
                          },
                          "wards_placed": 12
                        },
                        {
                          "assists": 7,
                          "champion": {
                            "id": 3017,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/839eb7d1426303e65005ce5348fca00d.png",
                            "name": "Graves",
                            "slug": "Graves"
                          },
                          "creep_score": 346,
                          "cs_at_14": 104,
                          "cs_diff_at_14": 19,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": true,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239287,
                          "gold_earned": 17455,
                          "gold_percentage": 21.94,
                          "gold_spent": 15825,
                          "items": [
                            {
                              "id": 2504,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2927,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a3d78560d3945a73d66da14f28d6b759.png",
                              "is_trinket": false,
                              "name": "Black Cleaver"
                            },
                            {
                              "id": 2933,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/9eb16adb98fcdc9c9ae35eabe19c322f.png",
                              "is_trinket": false,
                              "name": "Maw of Malmortius"
                            },
                            {
                              "id": 2935,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97032f4cae42f011b132d0bca2438e8b.png",
                              "is_trinket": false,
                              "name": "Goredrinker"
                            },
                            {
                              "id": 2963,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b024e8ca8cf9873201744933ec14c30c.png",
                              "is_trinket": false,
                              "name": "Umbral Glaive"
                            },
                            {
                              "id": 3043,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3c9dee81-cfff-4920-87ad-e0516ac0fc92.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 208,
                            "neutral_minions_enemy_jungle": 16,
                            "neutral_minions_team_jungle": 137,
                            "players": 4,
                            "turrets": 0,
                            "wards": 54
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 3,
                          "largest_multi_kill": 1,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 10811,
                            "dealt_percentage": 2.63,
                            "dealt_to_champions": 969,
                            "dealt_to_champions_percentage": 1.77,
                            "taken": 10502
                          },
                          "masteries": [],
                          "minions_killed": 346,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 294997,
                            "dealt_percentage": 36.33,
                            "dealt_to_champions": 23781,
                            "dealt_to_champions_percentage": 40.7,
                            "taken": 24888
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-12-24",
                            "first_name": "Moon",
                            "id": 31392,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                            "last_name": "Hyeon-joon",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "Oner",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "oner"
                          },
                          "player_id": 31392,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 29,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d7dee9f79afc995429521e2b586aae87.png",
                                "name": "Fleet Footwork",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 1,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                              "lesser_runes": [
                                {
                                  "id": 8,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a5317349f8ce3e0923fe970e5232bf30.png",
                                  "name": "Zombie Ward",
                                  "type": "slot2"
                                },
                                {
                                  "id": 11,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/569a1e7d3c46d9731392616eccebdd9c.png",
                                  "name": "Treasure Hunter",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Domination",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 325139,
                            "dealt_percentage": 25.54,
                            "dealt_to_champions": 26059,
                            "dealt_to_champions_percentage": 22.1,
                            "taken": 37436
                          },
                          "total_heal": 21694,
                          "total_time_crowd_control_dealt": 488,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 19329,
                            "dealt_percentage": 38.66,
                            "dealt_to_champions": 1307,
                            "dealt_to_champions_percentage": 27.57,
                            "taken": 2045
                          },
                          "wards": {
                            "placed": 72,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 13
                          },
                          "wards_placed": 72
                        }
                      ],
                      "position": 2,
                      "status": "finished",
                      "teams": [
                        {
                          "atakhan_kills": null,
                          "bans": [
                            2982,
                            3131,
                            3040,
                            3156,
                            3085
                          ],
                          "baron_kills": 0,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 1,
                          "color": "red",
                          "dragon_kills": 4,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": false,
                          "first_blood": true,
                          "first_dragon": true,
                          "first_herald": true,
                          "first_inhibitor": false,
                          "first_tower": true,
                          "first_voidgrub": null,
                          "gold_earned": 79576,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 0,
                          "kills": 13,
                          "mountain_drake_kills": 0,
                          "ocean_drake_kills": 3,
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
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "tower_kills": 4,
                          "voidgrub_kills": null
                        },
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3152,
                            3191,
                            3083,
                            2991,
                            3175
                          ],
                          "baron_kills": 1,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 0,
                          "color": "blue",
                          "dragon_kills": 3,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": true,
                          "first_blood": false,
                          "first_dragon": false,
                          "first_herald": false,
                          "first_inhibitor": true,
                          "first_tower": false,
                          "first_voidgrub": null,
                          "gold_earned": 80507,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 1,
                          "kills": 17,
                          "mountain_drake_kills": 1,
                          "ocean_drake_kills": 2,
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
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "tower_kills": 9,
                          "voidgrub_kills": null
                        }
                      ],
                      "winner": {
                        "id": 126370,
                        "type": "Team"
                      },
                      "winner_type": "Team"
                    },
                    {
                      "begin_at": "2022-11-06T00:52:58Z",
                      "complete": true,
                      "detailed_stats": true,
                      "end_at": "2022-11-06T01:29:47Z",
                      "finished": true,
                      "forfeit": false,
                      "id": 239286,
                      "length": 1870,
                      "match_id": 651268,
                      "players": [
                        {
                          "assists": 4,
                          "champion": {
                            "id": 2991,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/baf32ee97457437ea20c42ba23003e0c.png",
                            "name": "Azir",
                            "slug": "Azir"
                          },
                          "creep_score": 306,
                          "cs_at_14": 138,
                          "cs_diff_at_14": 12,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": true,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239286,
                          "gold_earned": 15006,
                          "gold_percentage": 24.42,
                          "gold_spent": 14125,
                          "items": [
                            {
                              "id": 2651,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2814,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                              "is_trinket": false,
                              "name": "Rabadon's Deathcap"
                            },
                            {
                              "id": 2898,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                              "is_trinket": false,
                              "name": "Void Staff"
                            },
                            {
                              "id": 2908,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/e6408582a9edbfc6d6896b3dc2631cd7.png",
                              "is_trinket": false,
                              "name": "Crown of the Shattered Queen"
                            },
                            {
                              "id": 3012,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/67ee113a533a1e443672e237d45f0043.png",
                              "is_trinket": false,
                              "name": "Morellonomicon"
                            }
                          ],
                          "kills": 6,
                          "kills_counters": {
                            "inhibitors": 2,
                            "neutral_minions": 44,
                            "neutral_minions_enemy_jungle": 9,
                            "neutral_minions_team_jungle": 22,
                            "players": 6,
                            "turrets": 4,
                            "wards": 8
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 6,
                          "largest_multi_kill": 1,
                          "level": 18,
                          "magic_damage": {
                            "dealt": 210751,
                            "dealt_percentage": 63.26,
                            "dealt_to_champions": 24869,
                            "dealt_to_champions_percentage": 66.28,
                            "taken": 4884
                          },
                          "masteries": [],
                          "minions_killed": 306,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 13981,
                            "dealt_percentage": 3.13,
                            "dealt_to_champions": 1006,
                            "dealt_to_champions_percentage": 3.42,
                            "taken": 9670
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-05-07",
                            "first_name": "Lee",
                            "id": 585,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                            "last_name": "Sang-hyeok",
                            "modified_at": "2026-02-01T11:19:16Z",
                            "name": "Faker",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "faker"
                          },
                          "player_id": 585,
                          "role": "mid",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 33,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                                  "name": "Presence of Mind",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 38,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/08f4edce2a6f85edbfea701c04314cb9.png",
                                  "name": "Cut Down",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "lesser_runes": [
                                {
                                  "id": 56,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                  "name": "Manaflow Band",
                                  "type": "slot1"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 228568,
                            "dealt_percentage": 28.39,
                            "dealt_to_champions": 26017,
                            "dealt_to_champions_percentage": 35.95,
                            "taken": 15122
                          },
                          "total_heal": 3782,
                          "total_time_crowd_control_dealt": 261,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 3835,
                            "dealt_percentage": 15.03,
                            "dealt_to_champions": 140,
                            "dealt_to_champions_percentage": 2.59,
                            "taken": 566
                          },
                          "wards": {
                            "placed": 19,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 9
                          },
                          "wards_placed": 19
                        },
                        {
                          "assists": 1,
                          "champion": {
                            "id": 3184,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/1a8a9e41-d361-4a0e-9360-a129b30d9c3e.png",
                            "name": "Sivir",
                            "slug": "Sivir"
                          },
                          "creep_score": 358,
                          "cs_at_14": 123,
                          "cs_diff_at_14": -23,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239286,
                          "gold_earned": 13085,
                          "gold_percentage": 25.97,
                          "gold_spent": 12125,
                          "items": [
                            {
                              "id": 2446,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0421f84dc8dd53dcb0e9d5a525145979.png",
                              "is_trinket": false,
                              "name": "Cloak of Agility"
                            },
                            {
                              "id": 2494,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/fcd28e708879aa54037da3539604b1c4.png",
                              "is_trinket": false,
                              "name": "Infinity Edge"
                            },
                            {
                              "id": 2652,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0e05c6ca936978b4f09ade82914b7e39.png",
                              "is_trinket": false,
                              "name": "Last Whisper"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2698,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1cc8c818e8f80cb70ec9a2e324c95632.png",
                              "is_trinket": false,
                              "name": "Kraken Slayer"
                            },
                            {
                              "id": 2772,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a66155c26e91b606800dab91e16272ac.png",
                              "is_trinket": false,
                              "name": "Phantom Dancer"
                            },
                            {
                              "id": 2790,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a900946a4d19c740a092b344807dcb7e.png",
                              "is_trinket": false,
                              "name": "Slightly Magical Footwear"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 23,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 18,
                            "players": 1,
                            "turrets": 1,
                            "wards": 9
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 585,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 0,
                            "dealt_percentage": 0,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 4049
                          },
                          "masteries": [],
                          "minions_killed": 358,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 237701,
                            "dealt_percentage": 51.39,
                            "dealt_to_champions": 12240,
                            "dealt_to_champions_percentage": 39.24,
                            "taken": 8501
                          },
                          "player": {
                            "active": true,
                            "age": 29,
                            "birthday": "1996-10-23",
                            "first_name": "Kim",
                            "id": 2169,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/2169/ezgif_3_4d5729796f.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 28,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d11f16420cc7a65ce1f1253d0adf5459.png",
                                "name": "Lethal Tempo",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 33,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                                  "name": "Presence of Mind",
                                  "type": "slot1"
                                },
                                {
                                  "id": 36,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/078fa7db48ed5384e9933f535f0b986a.png",
                                  "name": "Legend: Bloodline",
                                  "type": "slot2"
                                },
                                {
                                  "id": 38,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/08f4edce2a6f85edbfea701c04314cb9.png",
                                  "name": "Cut Down",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 19,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                  "name": "Magical Footwear",
                                  "type": "slot1"
                                },
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 30,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/62cc94a564835cd3abd80d74346c35da.png",
                              "name": "Heal"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 265284,
                            "dealt_percentage": 35.42,
                            "dealt_to_champions": 12733,
                            "dealt_to_champions_percentage": 23.87,
                            "taken": 12794
                          },
                          "total_heal": 2082,
                          "total_time_crowd_control_dealt": 64,
                          "total_units_healed": 3,
                          "true_damage": {
                            "dealt": 27583,
                            "dealt_percentage": 37.89,
                            "dealt_to_champions": 493,
                            "dealt_to_champions_percentage": 26.35,
                            "taken": 243
                          },
                          "wards": {
                            "placed": 14,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 5
                          },
                          "wards_placed": 14
                        },
                        {
                          "assists": 7,
                          "champion": {
                            "id": 3175,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/499d8d59-146b-43de-a271-0198158b887a.png",
                            "name": "Renata Glasc",
                            "slug": "Renata"
                          },
                          "creep_score": 16,
                          "cs_at_14": 7,
                          "cs_diff_at_14": -4,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239286,
                          "gold_earned": 8473,
                          "gold_percentage": 13.79,
                          "gold_spent": 7625,
                          "items": [
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2721,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/26bd61f1a9d4395d2fa1a491945a90ce.png",
                              "is_trinket": false,
                              "name": "Bandleglass Mirror"
                            },
                            {
                              "id": 2761,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b4754269-dc0f-474a-a3b4-c181b7d6d26c.png",
                              "is_trinket": false,
                              "name": "Shurelya's Battlesong"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 3016,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b4e5bb16fbc4368c43c9712a2a154e6f.png",
                              "is_trinket": false,
                              "name": "Oblivion Orb"
                            }
                          ],
                          "kills": 2,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 1,
                            "neutral_minions_enemy_jungle": 1,
                            "neutral_minions_team_jungle": 0,
                            "players": 2,
                            "turrets": 0,
                            "wards": 8
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
                            "dealt": 21317,
                            "dealt_percentage": 6.4,
                            "dealt_to_champions": 2694,
                            "dealt_to_champions_percentage": 7.18,
                            "taken": 4681
                          },
                          "masteries": [],
                          "minions_killed": 16,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 8781,
                            "dealt_percentage": 1.97,
                            "dealt_to_champions": 846,
                            "dealt_to_champions_percentage": 2.87,
                            "taken": 4594
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-10-14",
                            "first_name": "Ryu",
                            "id": 8158,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                            "last_name": "Min-seok",
                            "modified_at": "2026-02-01T11:19:16Z",
                            "name": "Keria",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "keria"
                          },
                          "player_id": 8158,
                          "role": "sup",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "keystone": {
                                "id": 42,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ded20bb65d8b80ffaf6408be45136628.png",
                                "name": "Guardian",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 45,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/592200e1a39d2281977fc92d788cacd1.png",
                                  "name": "Shield Bash",
                                  "type": "slot1"
                                },
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 51,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                                  "name": "Unflinching",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 1,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                              "lesser_runes": [
                                {
                                  "id": 6,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/faae66d46ae5bc177a56890342087ac2.png",
                                  "name": "Taste of Blood",
                                  "type": "slot1"
                                },
                                {
                                  "id": 13,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/623d21bc9acd874af4f1c2150bdd7150.png",
                                  "name": "Relentless Hunter",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Domination",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 31677,
                            "dealt_percentage": 3.93,
                            "dealt_to_champions": 5119,
                            "dealt_to_champions_percentage": 7.07,
                            "taken": 10685
                          },
                          "total_heal": 1348,
                          "total_time_crowd_control_dealt": 247,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 1578,
                            "dealt_percentage": 6.18,
                            "dealt_to_champions": 1578,
                            "dealt_to_champions_percentage": 29.23,
                            "taken": 1408
                          },
                          "wards": {
                            "placed": 62,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 23
                          },
                          "wards_placed": 62
                        },
                        {
                          "assists": 1,
                          "champion": {
                            "id": 3166,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/cad8d209-bda9-43f3-a7fa-cebce483ec37.png",
                            "name": "Aatrox",
                            "slug": "Aatrox"
                          },
                          "creep_score": 219,
                          "cs_at_14": 119,
                          "cs_diff_at_14": -15,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239286,
                          "gold_earned": 10355,
                          "gold_percentage": 20.55,
                          "gold_spent": 10225,
                          "items": [
                            {
                              "id": 2451,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/7c23780ddc70d6db6bdbaff941acf146.png",
                              "is_trinket": false,
                              "name": "Chain Vest"
                            },
                            {
                              "id": 2465,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/167abf5d0dc59292a78b79ceadffcc99.png",
                              "is_trinket": false,
                              "name": "Negatron Cloak"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2912,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/eaef5f4c2f6f2d5fcf13f287c321e59b.png",
                              "is_trinket": false,
                              "name": "Eclipse"
                            },
                            {
                              "id": 2934,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6f38d2d2845b0958a9cf0c03b8d592a2.png",
                              "is_trinket": false,
                              "name": "Death's Dance"
                            }
                          ],
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 0,
                            "players": 3,
                            "turrets": 0,
                            "wards": 7
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
                          "level": 15,
                          "magic_damage": {
                            "dealt": 0,
                            "dealt_percentage": 0,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 5762
                          },
                          "masteries": [],
                          "minions_killed": 219,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 124269,
                            "dealt_percentage": 26.87,
                            "dealt_to_champions": 12762,
                            "dealt_to_champions_percentage": 40.92,
                            "taken": 11669
                          },
                          "player": {
                            "active": true,
                            "age": 26,
                            "birthday": "2000-03-11",
                            "first_name": "Hwang",
                            "id": 8172,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/8172/drx_kingen_2022_split_2.png",
                            "last_name": "Seong-hoon",
                            "modified_at": "2026-02-01T11:16:32Z",
                            "name": "Kingen",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "kingen"
                          },
                          "player_id": 8172,
                          "role": "top",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 49,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
                                  "name": "Overgrowth",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 131444,
                            "dealt_percentage": 17.55,
                            "dealt_to_champions": 12762,
                            "dealt_to_champions_percentage": 23.92,
                            "taken": 20355
                          },
                          "total_heal": 8082,
                          "total_time_crowd_control_dealt": 136,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 7175,
                            "dealt_percentage": 9.86,
                            "dealt_to_champions": 0,
                            "dealt_to_champions_percentage": 0,
                            "taken": 2923
                          },
                          "wards": {
                            "placed": 9,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 7
                          },
                          "wards_placed": 9
                        },
                        {
                          "assists": 3,
                          "champion": {
                            "id": 3020,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/fde39f7fc210740c1c136b9d7af54de4.png",
                            "name": "Heimerdinger",
                            "slug": "Heimerdinger"
                          },
                          "creep_score": 40,
                          "cs_at_14": 11,
                          "cs_diff_at_14": 4,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239286,
                          "gold_earned": 6869,
                          "gold_percentage": 13.63,
                          "gold_spent": 6410,
                          "items": [
                            {
                              "id": 2460,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0f07d995a4de9dc12ffaf8c403658755.png",
                              "is_trinket": false,
                              "name": "Amplifying Tome"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2651,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                              "is_trinket": false,
                              "name": "Sorcerer's Shoes"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2800,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                              "is_trinket": false,
                              "name": "Shard of True Ice"
                            },
                            {
                              "id": 2924,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d4fde29e50e7ed8472b31f4a78134063.png",
                              "is_trinket": false,
                              "name": "Rylai's Crystal Scepter"
                            },
                            {
                              "id": 3016,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b4e5bb16fbc4368c43c9712a2a154e6f.png",
                              "is_trinket": false,
                              "name": "Oblivion Orb"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 0,
                            "players": 0,
                            "turrets": 0,
                            "wards": 18
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
                          "level": 12,
                          "magic_damage": {
                            "dealt": 34115,
                            "dealt_percentage": 15.97,
                            "dealt_to_champions": 8986,
                            "dealt_to_champions_percentage": 44.3,
                            "taken": 3822
                          },
                          "masteries": [],
                          "minions_killed": 40,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 4548,
                            "dealt_percentage": 0.98,
                            "dealt_to_champions": 373,
                            "dealt_to_champions_percentage": 1.2,
                            "taken": 7025
                          },
                          "player": {
                            "active": true,
                            "age": 28,
                            "birthday": "1997-04-01",
                            "first_name": "Cho",
                            "id": 15425,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/15425/drx_bery_l_2022_split_2.png",
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
                            "primary_path": {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                              "keystone": {
                                "id": 53,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/b8282c680e5d022dc564c54937a20a26.png",
                                "name": "Arcane Comet",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 56,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                                  "name": "Manaflow Band",
                                  "type": "slot1"
                                },
                                {
                                  "id": 59,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/732d4e2a7fdf6ecc3ec8e42504a111b9.png",
                                  "name": "Celerity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 61,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                                  "name": "Scorch",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Sorcery",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 1,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                              "lesser_runes": [
                                {
                                  "id": 6,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/faae66d46ae5bc177a56890342087ac2.png",
                                  "name": "Taste of Blood",
                                  "type": "slot1"
                                },
                                {
                                  "id": 11,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/569a1e7d3c46d9731392616eccebdd9c.png",
                                  "name": "Treasure Hunter",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Domination",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 26,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                              "name": "Ignite"
                            },
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 39135,
                            "dealt_percentage": 5.23,
                            "dealt_to_champions": 9832,
                            "dealt_to_champions_percentage": 18.43,
                            "taken": 11210
                          },
                          "total_heal": 1319,
                          "total_time_crowd_control_dealt": 200,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 472,
                            "dealt_percentage": 0.65,
                            "dealt_to_champions": 472,
                            "dealt_to_champions_percentage": 25.23,
                            "taken": 361
                          },
                          "wards": {
                            "placed": 38,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 11
                          },
                          "wards_placed": 38
                        },
                        {
                          "assists": 6,
                          "champion": {
                            "id": 3177,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/bf77b476-a4b2-4433-a896-13d082b51644.png",
                            "name": "Varus",
                            "slug": "Varus"
                          },
                          "creep_score": 296,
                          "cs_at_14": 146,
                          "cs_diff_at_14": 23,
                          "deaths": 0,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239286,
                          "gold_earned": 13345,
                          "gold_percentage": 21.72,
                          "gold_spent": 12000,
                          "items": [
                            {
                              "id": 2544,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/924cb9f122b90bf1ee29b9650c092524.png",
                              "is_trinket": false,
                              "name": "Guinsoo's Rageblade"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2678,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                              "is_trinket": true,
                              "name": "Farsight Alteration"
                            },
                            {
                              "id": 2699,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0f33f102856e8d40f6d38ff057856e1d.png",
                              "is_trinket": false,
                              "name": "Immortal Shieldbow"
                            },
                            {
                              "id": 2930,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/5bc313a2ec67cebd731e4cf0549cb077.png",
                              "is_trinket": false,
                              "name": "Wit's End"
                            },
                            {
                              "id": 3043,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3c9dee81-cfff-4920-87ad-e0516ac0fc92.png",
                              "is_trinket": false,
                              "name": "Stopwatch"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 2,
                            "neutral_minions": 41,
                            "neutral_minions_enemy_jungle": 8,
                            "neutral_minions_team_jungle": 23,
                            "players": 0,
                            "turrets": 5,
                            "wards": 11
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 251,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "level": 16,
                          "magic_damage": {
                            "dealt": 32924,
                            "dealt_percentage": 9.88,
                            "dealt_to_champions": 3858,
                            "dealt_to_champions_percentage": 10.28,
                            "taken": 3200
                          },
                          "masteries": [],
                          "minions_killed": 296,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 163438,
                            "dealt_percentage": 36.6,
                            "dealt_to_champions": 8586,
                            "dealt_to_champions_percentage": 29.15,
                            "taken": 7979
                          },
                          "player": {
                            "active": true,
                            "age": 24,
                            "birthday": "2002-02-06",
                            "first_name": "Lee",
                            "id": 19285,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/19285/t1_gumayusi_2023_split_2.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 28,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d11f16420cc7a65ce1f1253d0adf5459.png",
                                "name": "Lethal Tempo",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 23,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                                  "name": "Biscuit Delivery",
                                  "type": "slot2"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 30,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/62cc94a564835cd3abd80d74346c35da.png",
                              "name": "Heal"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 197805,
                            "dealt_percentage": 24.57,
                            "dealt_to_champions": 12819,
                            "dealt_to_champions_percentage": 17.71,
                            "taken": 11208
                          },
                          "total_heal": 4084,
                          "total_time_crowd_control_dealt": 272,
                          "total_units_healed": 4,
                          "true_damage": {
                            "dealt": 1440,
                            "dealt_percentage": 5.64,
                            "dealt_to_champions": 374,
                            "dealt_to_champions_percentage": 6.93,
                            "taken": 28
                          },
                          "wards": {
                            "placed": 14,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 4
                          },
                          "wards_placed": 14
                        },
                        {
                          "assists": 3,
                          "champion": {
                            "id": 3120,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/cbc53ec5b2ef342a710ba2c56ca13915.png",
                            "name": "Viego",
                            "slug": "Viego"
                          },
                          "creep_score": 143,
                          "cs_at_14": 97,
                          "cs_diff_at_14": 19,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239286,
                          "gold_earned": 8173,
                          "gold_percentage": 16.22,
                          "gold_spent": 7550,
                          "items": [
                            {
                              "id": 2449,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6db62c8691e2f6f35efb0eff6e55df41.png",
                              "is_trinket": false,
                              "name": "Ruby Crystal"
                            },
                            {
                              "id": 2451,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/7c23780ddc70d6db6bdbaff941acf146.png",
                              "is_trinket": false,
                              "name": "Chain Vest"
                            },
                            {
                              "id": 2504,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2659,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/afe5e3df08a76a4c10753ecd5da4273d.png",
                              "is_trinket": false,
                              "name": "Winged Moonplate"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2937,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0085138b38b1f85411988b1db668bc94.png",
                              "is_trinket": false,
                              "name": "Divine Sunderer"
                            }
                          ],
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 124,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 95,
                            "players": 0,
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
                          "largest_multi_kill": 0,
                          "level": 13,
                          "magic_damage": {
                            "dealt": 11712,
                            "dealt_percentage": 5.48,
                            "dealt_to_champions": 295,
                            "dealt_to_champions_percentage": 1.45,
                            "taken": 9079
                          },
                          "masteries": [],
                          "minions_killed": 143,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 87926,
                            "dealt_percentage": 19.01,
                            "dealt_to_champions": 5562,
                            "dealt_to_champions_percentage": 17.83,
                            "taken": 14384
                          },
                          "player": {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-03-21",
                            "first_name": "Hong",
                            "id": 24996,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/24996/tl_pyosik_2023_split_1.png",
                            "last_name": "Chang-hyeon",
                            "modified_at": "2026-02-08T13:14:45Z",
                            "name": "Pyosik",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "pyosik"
                          },
                          "player_id": 24996,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 35,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                                  "name": "Legend: Tenacity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 37,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6c94f0110a44559cdcab24911a21b452.png",
                                  "name": "Coup de Grace",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 19,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                  "name": "Magical Footwear",
                                  "type": "slot1"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 112456,
                            "dealt_percentage": 15.01,
                            "dealt_to_champions": 6425,
                            "dealt_to_champions_percentage": 12.04,
                            "taken": 24395
                          },
                          "total_heal": 9458,
                          "total_time_crowd_control_dealt": 167,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 12817,
                            "dealt_percentage": 17.61,
                            "dealt_to_champions": 566,
                            "dealt_to_champions_percentage": 30.25,
                            "taken": 931
                          },
                          "wards": {
                            "placed": 16,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 15
                          },
                          "wards_placed": 16
                        },
                        {
                          "assists": 3,
                          "champion": {
                            "id": 3185,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/73d079e4-ba42-48a1-8a29-dae7f95b9587.png",
                            "name": "Sylas",
                            "slug": "Sylas"
                          },
                          "creep_score": 285,
                          "cs_at_14": 126,
                          "cs_diff_at_14": -12,
                          "deaths": 4,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": true,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239286,
                          "gold_earned": 11899,
                          "gold_percentage": 23.62,
                          "gold_spent": 11500,
                          "items": [
                            {
                              "id": 2467,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/e914701535346c87ea1cfb1fb159631c.png",
                              "is_trinket": false,
                              "name": "Dark Seal"
                            },
                            {
                              "id": 2474,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                              "is_trinket": false,
                              "name": "Control Ward"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2814,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                              "is_trinket": false,
                              "name": "Rabadon's Deathcap"
                            },
                            {
                              "id": 2832,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                              "is_trinket": false,
                              "name": "Ionian Boots of Lucidity"
                            },
                            {
                              "id": 2910,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a8377226b797197fdb941b2fad4123cb.png",
                              "is_trinket": false,
                              "name": "Everfrost"
                            },
                            {
                              "id": 3048,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/e8bca3b0-24da-479e-9fa7-13f2021cc106.png",
                              "is_trinket": false,
                              "name": "Zhonya's Hourglass"
                            }
                          ],
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 6,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 6,
                            "players": 1,
                            "turrets": 2,
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
                            "dealt": 167781,
                            "dealt_percentage": 78.55,
                            "dealt_to_champions": 11004,
                            "dealt_to_champions_percentage": 54.25,
                            "taken": 17026
                          },
                          "masteries": [],
                          "minions_killed": 285,
                          "opponent": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "physical_damage": {
                            "dealt": 8108,
                            "dealt_percentage": 1.75,
                            "dealt_to_champions": 253,
                            "dealt_to_champions_percentage": 0.81,
                            "taken": 11135
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-11-28",
                            "first_name": "Kim",
                            "id": 25391,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/25391/drx_zeka_2022_split_2.png",
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
                            "primary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "keystone": {
                                "id": 65,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/13598521aebb0be68b52982d46aa1b1c.png",
                                "name": "First Strike",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                },
                                {
                                  "id": 19,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                  "name": "Magical Footwear",
                                  "type": "slot1"
                                },
                                {
                                  "id": 22,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/11c92222e3b798ce1ff524d34b3297f1.png",
                                  "name": "Minion Dematerializer",
                                  "type": "slot2"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 49,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
                                  "name": "Overgrowth",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 68,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                                "name": "Magic Resist",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "total_damage": {
                            "dealt": 200642,
                            "dealt_percentage": 26.79,
                            "dealt_to_champions": 11598,
                            "dealt_to_champions_percentage": 21.74,
                            "taken": 28832
                          },
                          "total_heal": 3974,
                          "total_time_crowd_control_dealt": 490,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 24752,
                            "dealt_percentage": 34,
                            "dealt_to_champions": 340,
                            "dealt_to_champions_percentage": 18.17,
                            "taken": 670
                          },
                          "wards": {
                            "placed": 6,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 6
                          },
                          "wards_placed": 6
                        },
                        {
                          "assists": 5,
                          "champion": {
                            "id": 3129,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/5b5006046d300b532887aa8c26e1df0c.png",
                            "name": "Yone",
                            "slug": "Yone"
                          },
                          "creep_score": 274,
                          "cs_at_14": 134,
                          "cs_diff_at_14": 15,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "game_id": 239286,
                          "gold_earned": 14176,
                          "gold_percentage": 23.07,
                          "gold_spent": 12250,
                          "items": [
                            {
                              "id": 2494,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/fcd28e708879aa54037da3539604b1c4.png",
                              "is_trinket": false,
                              "name": "Infinity Edge"
                            },
                            {
                              "id": 2649,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1fd6e92b28dd5cf2e50f94c2b112b2dd.png",
                              "is_trinket": false,
                              "name": "Berserker's Greaves"
                            },
                            {
                              "id": 2679,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                              "is_trinket": true,
                              "name": "Oracle Lens"
                            },
                            {
                              "id": 2699,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0f33f102856e8d40f6d38ff057856e1d.png",
                              "is_trinket": false,
                              "name": "Immortal Shieldbow"
                            },
                            {
                              "id": 2793,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3e1d3f42c8ef52ed8cc0338eb7873bb4.png",
                              "is_trinket": false,
                              "name": "Mortal Reminder"
                            },
                            {
                              "id": 3044,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d0e13016-50c3-4bf8-926c-a502cced78c4.png",
                              "is_trinket": false,
                              "name": "Broken Stopwatch"
                            }
                          ],
                          "kills": 4,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 12,
                            "neutral_minions_enemy_jungle": 0,
                            "neutral_minions_team_jungle": 6,
                            "players": 4,
                            "turrets": 1,
                            "wards": 2
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 639,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 2,
                          "level": 17,
                          "magic_damage": {
                            "dealt": 27706,
                            "dealt_percentage": 8.32,
                            "dealt_to_champions": 4569,
                            "dealt_to_champions_percentage": 12.18,
                            "taken": 2978
                          },
                          "masteries": [],
                          "minions_killed": 274,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 164641,
                            "dealt_percentage": 36.87,
                            "dealt_to_champions": 11503,
                            "dealt_to_champions_percentage": 39.06,
                            "taken": 13820
                          },
                          "player": {
                            "active": true,
                            "age": 22,
                            "birthday": "2004-01-31",
                            "first_name": "Choi",
                            "id": 31391,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31391/t1_zeus_2023_split_2.png",
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
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 28,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d11f16420cc7a65ce1f1253d0adf5459.png",
                                "name": "Lethal Tempo",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 34,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                                  "name": "Legend: Alacrity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 39,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                                  "name": "Last Stand",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 4,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                              "lesser_runes": [
                                {
                                  "id": 47,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                                  "name": "Second Wind",
                                  "type": "slot2"
                                },
                                {
                                  "id": 49,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
                                  "name": "Overgrowth",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Resolve",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                              "name": "Teleport"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 194977,
                            "dealt_percentage": 24.21,
                            "dealt_to_champions": 18702,
                            "dealt_to_champions_percentage": 25.84,
                            "taken": 17125
                          },
                          "total_heal": 2636,
                          "total_time_crowd_control_dealt": 122,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 2629,
                            "dealt_percentage": 10.3,
                            "dealt_to_champions": 2629,
                            "dealt_to_champions_percentage": 48.69,
                            "taken": 326
                          },
                          "wards": {
                            "placed": 11,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 6
                          },
                          "wards_placed": 11
                        },
                        {
                          "assists": 7,
                          "champion": {
                            "id": 3189,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/4fa161b0-c18a-456c-a6eb-e5812430d153.png",
                            "name": "Lee Sin",
                            "slug": "LeeSin"
                          },
                          "creep_score": 155,
                          "cs_at_14": 78,
                          "cs_diff_at_14": -19,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": true
                          },
                          "game_id": 239286,
                          "gold_earned": 10450,
                          "gold_percentage": 17.01,
                          "gold_spent": 8700,
                          "items": [
                            {
                              "id": 2504,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                              "is_trinket": false,
                              "name": "Plated Steelcaps"
                            },
                            {
                              "id": 2677,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d764e2dad4b185bbbbc86ca2998d5313.png",
                              "is_trinket": true,
                              "name": "Stealth Ward"
                            },
                            {
                              "id": 2933,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/9eb16adb98fcdc9c9ae35eabe19c322f.png",
                              "is_trinket": false,
                              "name": "Maw of Malmortius"
                            },
                            {
                              "id": 2935,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97032f4cae42f011b132d0bca2438e8b.png",
                              "is_trinket": false,
                              "name": "Goredrinker"
                            },
                            {
                              "id": 3044,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d0e13016-50c3-4bf8-926c-a502cced78c4.png",
                              "is_trinket": false,
                              "name": "Broken Stopwatch"
                            }
                          ],
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 129,
                            "neutral_minions_enemy_jungle": 17,
                            "neutral_minions_team_jungle": 84,
                            "players": 3,
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
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "level": 15,
                          "magic_damage": {
                            "dealt": 40447,
                            "dealt_percentage": 12.14,
                            "dealt_to_champions": 1530,
                            "dealt_to_champions_percentage": 4.08,
                            "taken": 7028
                          },
                          "masteries": [],
                          "minions_killed": 155,
                          "opponent": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          },
                          "physical_damage": {
                            "dealt": 95710,
                            "dealt_percentage": 21.43,
                            "dealt_to_champions": 7511,
                            "dealt_to_champions_percentage": 25.5,
                            "taken": 12927
                          },
                          "player": {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-12-24",
                            "first_name": "Moon",
                            "id": 31392,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                            "last_name": "Hyeon-joon",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "Oner",
                            "nationality": "KR",
                            "role": "jun",
                            "slug": "oner"
                          },
                          "player_id": 31392,
                          "role": "jun",
                          "runes": [],
                          "runes_reforged": {
                            "primary_path": {
                              "id": 3,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                              "keystone": {
                                "id": 30,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                                "name": "Conqueror",
                                "type": "keystone"
                              },
                              "lesser_runes": [
                                {
                                  "id": 32,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                                  "name": "Triumph",
                                  "type": "slot1"
                                },
                                {
                                  "id": 35,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                                  "name": "Legend: Tenacity",
                                  "type": "slot2"
                                },
                                {
                                  "id": 37,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6c94f0110a44559cdcab24911a21b452.png",
                                  "name": "Coup de Grace",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Precision",
                              "type": "path"
                            },
                            "secondary_path": {
                              "id": 2,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                              "lesser_runes": [
                                {
                                  "id": 19,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                                  "name": "Magical Footwear",
                                  "type": "slot1"
                                },
                                {
                                  "id": 24,
                                  "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                                  "name": "Cosmic Insight",
                                  "type": "slot3"
                                }
                              ],
                              "name": "Inspiration",
                              "type": "path"
                            },
                            "shards": {
                              "defense": {
                                "id": 67,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                                "name": "Armor",
                                "type": "shard"
                              },
                              "flex": {
                                "id": 71,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                                "name": "Adaptative Force",
                                "type": "shard"
                              },
                              "offense": {
                                "id": 69,
                                "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                                "name": "Attack Speed",
                                "type": "shard"
                              }
                            }
                          },
                          "spells": [
                            {
                              "id": 28,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                              "name": "Flash"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                              "name": "Smite"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "total_damage": {
                            "dealt": 152191,
                            "dealt_percentage": 18.9,
                            "dealt_to_champions": 9720,
                            "dealt_to_champions_percentage": 13.43,
                            "taken": 20447
                          },
                          "total_heal": 11751,
                          "total_time_crowd_control_dealt": 506,
                          "total_units_healed": 1,
                          "true_damage": {
                            "dealt": 16033,
                            "dealt_percentage": 62.84,
                            "dealt_to_champions": 678,
                            "dealt_to_champions_percentage": 12.56,
                            "taken": 491
                          },
                          "wards": {
                            "placed": 16,
                            "sight_wards_bought_in_game": 0,
                            "vision_wards_bought_in_game": 6
                          },
                          "wards_placed": 16
                        }
                      ],
                      "position": 1,
                      "status": "finished",
                      "teams": [
                        {
                          "atakhan_kills": null,
                          "bans": [
                            2982,
                            3077,
                            3085,
                            3008,
                            2989
                          ],
                          "baron_kills": 2,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 1,
                          "color": "blue",
                          "dragon_kills": 4,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": true,
                          "first_blood": false,
                          "first_dragon": true,
                          "first_herald": false,
                          "first_inhibitor": true,
                          "first_tower": true,
                          "first_voidgrub": null,
                          "gold_earned": 61450,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 5,
                          "kills": 15,
                          "mountain_drake_kills": 1,
                          "ocean_drake_kills": 2,
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
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          },
                          "tower_kills": 11,
                          "voidgrub_kills": null
                        },
                        {
                          "atakhan_kills": null,
                          "bans": [
                            3083,
                            3131,
                            3017,
                            3152,
                            3156
                          ],
                          "baron_kills": 0,
                          "chemtech_drake_kills": 0,
                          "cloud_drake_kills": 0,
                          "color": "red",
                          "dragon_kills": 1,
                          "elder_drake_kills": 0,
                          "first_atakhan": null,
                          "first_baron": false,
                          "first_blood": true,
                          "first_dragon": false,
                          "first_herald": true,
                          "first_inhibitor": false,
                          "first_tower": false,
                          "first_voidgrub": null,
                          "gold_earned": 50381,
                          "herald_kills": 1,
                          "hextech_drake_kills": 0,
                          "infernal_drake_kills": 0,
                          "inhibitor_kills": 0,
                          "kills": 5,
                          "mountain_drake_kills": 0,
                          "ocean_drake_kills": 1,
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
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
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
                  "modified_at": "2026-02-01T11:19:17Z",
                  "most_banned": [
                    {
                      "count": 6,
                      "name": "Aatrox",
                      "slug": "Aatrox"
                    },
                    {
                      "count": 6,
                      "name": "Sejuani",
                      "slug": "Sejuani"
                    },
                    {
                      "count": 6,
                      "name": "Yuumi",
                      "slug": "Yuumi"
                    },
                    {
                      "count": 4,
                      "name": "Akali",
                      "slug": "Akali"
                    },
                    {
                      "count": 4,
                      "name": "Kindred",
                      "slug": "Kindred"
                    },
                    {
                      "count": 3,
                      "name": "Ashe",
                      "slug": "Ashe"
                    },
                    {
                      "count": 3,
                      "name": "Lissandra",
                      "slug": "Lissandra"
                    },
                    {
                      "count": 3,
                      "name": "Taliyah",
                      "slug": "Taliyah"
                    },
                    {
                      "count": 2,
                      "name": "Caitlyn",
                      "slug": "Caitlyn"
                    },
                    {
                      "count": 2,
                      "name": "Fiora",
                      "slug": "Fiora"
                    },
                    {
                      "count": 2,
                      "name": "Galio",
                      "slug": "Galio"
                    },
                    {
                      "count": 2,
                      "name": "Graves",
                      "slug": "Graves"
                    },
                    {
                      "count": 2,
                      "name": "Heimerdinger",
                      "slug": "Heimerdinger"
                    },
                    {
                      "count": 2,
                      "name": "Renekton",
                      "slug": "Renekton"
                    },
                    {
                      "count": 2,
                      "name": "Viego",
                      "slug": "Viego"
                    },
                    {
                      "count": 1,
                      "name": "Aphelios",
                      "slug": "Aphelios"
                    },
                    {
                      "count": 1,
                      "name": "Ezreal",
                      "slug": "Ezreal"
                    },
                    {
                      "count": 1,
                      "name": "Jax",
                      "slug": "Jax"
                    },
                    {
                      "count": 1,
                      "name": "Kai'Sa",
                      "slug": "Kaisa"
                    },
                    {
                      "count": 1,
                      "name": "Lucian",
                      "slug": "Lucian"
                    },
                    {
                      "count": 1,
                      "name": "Ornn",
                      "slug": "Ornn"
                    },
                    {
                      "count": 1,
                      "name": "Rell",
                      "slug": "Rell"
                    },
                    {
                      "count": 1,
                      "name": "Renata Glasc",
                      "slug": "Renata"
                    },
                    {
                      "count": 1,
                      "name": "Sylas",
                      "slug": "Sylas"
                    },
                    {
                      "count": 1,
                      "name": "Tristana",
                      "slug": "Tristana"
                    },
                    {
                      "count": 1,
                      "name": "Vi",
                      "slug": "Vi"
                    }
                  ],
                  "most_banned_against": [
                    {
                      "count": 9,
                      "name": "Caitlyn",
                      "slug": "Caitlyn"
                    },
                    {
                      "count": 7,
                      "name": "Lucian",
                      "slug": "Lucian"
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
                      "count": 4,
                      "name": "Lee Sin",
                      "slug": "LeeSin"
                    },
                    {
                      "count": 4,
                      "name": "Ryze",
                      "slug": "Ryze"
                    },
                    {
                      "count": 4,
                      "name": "Yone",
                      "slug": "Yone"
                    },
                    {
                      "count": 2,
                      "name": "Fiora",
                      "slug": "Fiora"
                    },
                    {
                      "count": 2,
                      "name": "LeBlanc",
                      "slug": "Leblanc"
                    },
                    {
                      "count": 2,
                      "name": "Renata Glasc",
                      "slug": "Renata"
                    },
                    {
                      "count": 2,
                      "name": "Viktor",
                      "slug": "Viktor"
                    },
                    {
                      "count": 1,
                      "name": "Aatrox",
                      "slug": "Aatrox"
                    },
                    {
                      "count": 1,
                      "name": "Akali",
                      "slug": "Akali"
                    },
                    {
                      "count": 1,
                      "name": "Ashe",
                      "slug": "Ashe"
                    },
                    {
                      "count": 1,
                      "name": "Azir",
                      "slug": "Azir"
                    },
                    {
                      "count": 1,
                      "name": "Camille",
                      "slug": "Camille"
                    },
                    {
                      "count": 1,
                      "name": "Heimerdinger",
                      "slug": "Heimerdinger"
                    },
                    {
                      "count": 1,
                      "name": "Jayce",
                      "slug": "Jayce"
                    },
                    {
                      "count": 1,
                      "name": "Lux",
                      "slug": "Lux"
                    },
                    {
                      "count": 1,
                      "name": "Nocturne",
                      "slug": "Nocturne"
                    },
                    {
                      "count": 1,
                      "name": "Sejuani",
                      "slug": "Sejuani"
                    },
                    {
                      "count": 1,
                      "name": "Sylas",
                      "slug": "Sylas"
                    },
                    {
                      "count": 1,
                      "name": "Tahm Kench",
                      "slug": "TahmKench"
                    },
                    {
                      "count": 1,
                      "name": "Thresh",
                      "slug": "Thresh"
                    }
                  ],
                  "most_picked": [
                    {
                      "count": 5,
                      "games_lost": 1,
                      "games_won": 4,
                      "name": "Varus",
                      "slug": "Varus"
                    },
                    {
                      "count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Akali",
                      "slug": "Akali"
                    },
                    {
                      "count": 3,
                      "games_lost": 0,
                      "games_won": 3,
                      "name": "Azir",
                      "slug": "Azir"
                    },
                    {
                      "count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Graves",
                      "slug": "Graves"
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
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Nami",
                      "slug": "Nami"
                    },
                    {
                      "count": 3,
                      "games_lost": 0,
                      "games_won": 3,
                      "name": "Renata Glasc",
                      "slug": "Renata"
                    },
                    {
                      "count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "name": "Viego",
                      "slug": "Viego"
                    },
                    {
                      "count": 3,
                      "games_lost": 2,
                      "games_won": 1,
                      "name": "Viktor",
                      "slug": "Viktor"
                    },
                    {
                      "count": 3,
                      "games_lost": 0,
                      "games_won": 3,
                      "name": "Yone",
                      "slug": "Yone"
                    },
                    {
                      "count": 2,
                      "games_lost": 1,
                      "games_won": 1,
                      "name": "Ashe",
                      "slug": "Ashe"
                    },
                    {
                      "count": 2,
                      "games_lost": 1,
                      "games_won": 1,
                      "name": "Camille",
                      "slug": "Camille"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Gragas",
                      "slug": "Gragas"
                    },
                    {
                      "count": 2,
                      "games_lost": 1,
                      "games_won": 1,
                      "name": "Karma",
                      "slug": "Karma"
                    },
                    {
                      "count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "name": "Ryze",
                      "slug": "Ryze"
                    },
                    {
                      "count": 2,
                      "games_lost": 1,
                      "games_won": 1,
                      "name": "Sejuani",
                      "slug": "Sejuani"
                    },
                    {
                      "count": 1,
                      "games_lost": 1,
                      "games_won": 0,
                      "name": "Aatrox",
                      "slug": "Aatrox"
                    },
                    {
                      "count": 1,
                      "games_lost": 1,
                      "games_won": 0,
                      "name": "Fiora",
                      "slug": "Fiora"
                    },
                    {
                      "count": 1,
                      "games_lost": 1,
                      "games_won": 0,
                      "name": "Galio",
                      "slug": "Galio"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Gangplank",
                      "slug": "Gangplank"
                    },
                    {
                      "count": 1,
                      "games_lost": 1,
                      "games_won": 0,
                      "name": "Gwen",
                      "slug": "Gwen"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Heimerdinger",
                      "slug": "Heimerdinger"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Jayce",
                      "slug": "Jayce"
                    },
                    {
                      "count": 1,
                      "games_lost": 1,
                      "games_won": 0,
                      "name": "Kalista",
                      "slug": "Kalista"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Lee Sin",
                      "slug": "LeeSin"
                    },
                    {
                      "count": 1,
                      "games_lost": 1,
                      "games_won": 0,
                      "name": "Lux",
                      "slug": "Lux"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Nocturne",
                      "slug": "Nocturne"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Poppy",
                      "slug": "Poppy"
                    },
                    {
                      "count": 1,
                      "games_lost": 1,
                      "games_won": 0,
                      "name": "Soraka",
                      "slug": "Soraka"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Tahm Kench",
                      "slug": "TahmKench"
                    },
                    {
                      "count": 1,
                      "games_lost": 1,
                      "games_won": 0,
                      "name": "Vi",
                      "slug": "Vi"
                    },
                    {
                      "count": 1,
                      "games_lost": 0,
                      "games_won": 1,
                      "name": "Xayah",
                      "slug": "Xayah"
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
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                      "last_name": "Sang-hyeok",
                      "modified_at": "2026-02-01T11:19:16Z",
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
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                      "last_name": "Min-seok",
                      "modified_at": "2026-02-01T11:19:16Z",
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
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/19282/gen_doran_2023_split_2.png",
                      "last_name": "Hyeon-joon",
                      "modified_at": "2026-02-01T11:19:16Z",
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
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                      "last_name": "Hyeon-joon",
                      "modified_at": "2026-02-01T11:19:17Z",
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
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/38351/jdg_peyz_2025_split_1.png",
                      "last_name": "Su-hwan",
                      "modified_at": "2026-02-01T11:19:17Z",
                      "name": "Peyz",
                      "nationality": "KR",
                      "role": "adc",
                      "slug": "peyz"
                    }
                  ],
                  "slug": "t1",
                  "stats": {
                    "averages": {
                      "assists": 36.5,
                      "atakhan_kills": null,
                      "baron_kills": 1.33,
                      "deaths": 13.33,
                      "dragon_kills": 2.58,
                      "game_length": 2084,
                      "gold_earned": 65669.08,
                      "herald_kill": 0.83,
                      "inhibitor_kills": 1.75,
                      "kills": 16.08,
                      "ratios": {
                        "first_atakhan": null,
                        "first_baron": 0.83,
                        "first_blood": 0.42,
                        "first_dragon": 0.67,
                        "first_herald": 0.33,
                        "first_inhibitor": 0.67,
                        "first_tower": 0.58,
                        "first_voidgrub": null,
                        "win": 0.67
                      },
                      "total_minions_killed": 1100.92,
                      "tower_kills": 8.17,
                      "voidgrub_kills": null,
                      "wards_placed": 128.5
                    },
                    "games_count": 12,
                    "totals": {
                      "assists": 438,
                      "atakhan_kills": null,
                      "baron_kills": 16,
                      "blue_games_lost": 2,
                      "blue_games_won": 4,
                      "chemtech_drake_kills": 0,
                      "cloud_drake_kills": 6,
                      "deaths": 160,
                      "dragon_kills": 31,
                      "elder_drake_kills": 1,
                      "games_lost": 4,
                      "games_played": 12,
                      "games_won": 8,
                      "herald_kill": 10,
                      "hextech_drake_kills": 3,
                      "infernal_drake_kills": 5,
                      "inhibitor_kills": 21,
                      "kills": 193,
                      "matches_lost": 1,
                      "matches_played": 3,
                      "matches_won": 2,
                      "mountain_drake_kills": 3,
                      "ocean_drake_kills": 13,
                      "red_games_lost": 2,
                      "red_games_won": 4,
                      "tower_kills": 98,
                      "voidgrub_kills": null,
                      "wards_placed": 1542
                    },
                    "tournament": {
                      "begin_at": "2022-10-20T21:00:00Z",
                      "country": null,
                      "detailed_stats": true,
                      "end_at": "2022-11-06T05:25:00Z",
                      "expected_roster": [
                        {
                          "players": [
                            {
                              "active": true,
                              "age": 28,
                              "birthday": "1998-01-28",
                              "first_name": "Yuanhao",
                              "id": 429,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/429/wbg_xiaohu_2025_split_1.png",
                              "last_name": "Li",
                              "modified_at": "2026-02-11T13:59:27Z",
                              "name": "Xiaohu",
                              "nationality": "CN",
                              "role": "mid",
                              "slug": "xiaohu"
                            },
                            {
                              "active": true,
                              "age": 27,
                              "birthday": "1998-12-22",
                              "first_name": "Senming",
                              "id": 1584,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/1584/rng_ming_2024_split_1.png",
                              "last_name": "Shi",
                              "modified_at": "2024-12-21T09:36:23Z",
                              "name": "Ming",
                              "nationality": "CN",
                              "role": "sup",
                              "slug": "ming"
                            },
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2001-02-19",
                              "first_name": "Chen",
                              "id": 18448,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/18448/wbg_breathe_2025_split_1.png",
                              "last_name": "Chen",
                              "modified_at": "2025-10-09T11:48:59Z",
                              "name": "Breathe",
                              "nationality": "CN",
                              "role": "top",
                              "slug": "curse"
                            },
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2001-02-14",
                              "first_name": "Wei",
                              "id": 19316,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/19316/ig_gala_2025_split_1.png",
                              "last_name": "Chen",
                              "modified_at": "2026-03-08T14:51:06Z",
                              "name": "GALA",
                              "nationality": "CN",
                              "role": "adc",
                              "slug": "gala-a397ecf2-0505-4f6f-a93a-c608491b89ea"
                            },
                            {
                              "active": true,
                              "age": 23,
                              "birthday": "2002-11-09",
                              "first_name": "Yangwei",
                              "id": 21978,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/21978/ig_wei_2025_split_3.png",
                              "last_name": "Yan",
                              "modified_at": "2026-02-11T13:59:29Z",
                              "name": "Wei",
                              "nationality": "CN",
                              "role": "jun",
                              "slug": "wei"
                            }
                          ],
                          "team": {
                            "acronym": "RNG",
                            "dark_mode_image_url": null,
                            "id": 74,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/74/royal-never-give-up-cyacqft1.png",
                            "location": "CN",
                            "modified_at": "2025-12-11T22:45:26Z",
                            "name": "Royal Never Give Up",
                            "slug": "royal-never-give-up"
                          }
                        },
                        {
                          "players": [
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2000-09-29",
                              "first_name": "Jie",
                              "id": 8962,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/8962/al_hope_msi_2025.png",
                              "last_name": "Wang",
                              "modified_at": "2026-02-11T13:59:29Z",
                              "name": "Hope",
                              "nationality": "CN",
                              "role": "adc",
                              "slug": "hopezz"
                            },
                            {
                              "active": false,
                              "age": 27,
                              "birthday": "1998-10-19",
                              "first_name": "Qi",
                              "id": 8969,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/8969/jdg_yagao_2024_split_1.png",
                              "last_name": "Zeng",
                              "modified_at": "2025-12-30T11:47:26Z",
                              "name": "Yagao",
                              "nationality": "CN",
                              "role": "mid",
                              "slug": "yagao"
                            },
                            {
                              "active": true,
                              "age": 24,
                              "birthday": "2001-05-26",
                              "first_name": "Yunfeng",
                              "id": 15224,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/15224/jdg_missing_2023_split_1.png",
                              "last_name": "Lou",
                              "modified_at": "2026-02-07T14:44:47Z",
                              "name": "Missing",
                              "nationality": "CN",
                              "role": "sup",
                              "slug": "missing"
                            },
                            {
                              "active": true,
                              "age": 24,
                              "birthday": "2001-07-12",
                              "first_name": "Jiahao",
                              "id": 18472,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/18472/tes_369_2025_split_1.png",
                              "last_name": "Bai",
                              "modified_at": "2026-02-11T13:59:25Z",
                              "name": "369",
                              "nationality": "CN",
                              "role": "top",
                              "slug": "player-369"
                            },
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2000-11-02",
                              "first_name": "Jinhhyeok",
                              "id": 20290,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/20290/tes_kanavi_2025_split_1.png",
                              "last_name": "Seo",
                              "modified_at": "2026-01-06T07:15:50Z",
                              "name": "Kanavi",
                              "nationality": "KR",
                              "role": "jun",
                              "slug": "kanavi"
                            }
                          ],
                          "team": {
                            "acronym": "JDG",
                            "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/318/746px_jd_gaming_2021_full_allmode.png",
                            "id": 318,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/318/746px_jd_gaming_2021_full_allmode.png",
                            "location": "CN",
                            "modified_at": "2026-03-08T14:51:07Z",
                            "name": "JD Gaming",
                            "slug": "qg-reapers"
                          }
                        },
                        {
                          "players": [
                            {
                              "active": true,
                              "age": 27,
                              "birthday": "1998-08-28",
                              "first_name": "Xuanjun",
                              "id": 371,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/371/al_flandre_msi_2025.png",
                              "last_name": "Li",
                              "modified_at": "2026-02-11T13:59:29Z",
                              "name": "Flandre",
                              "nationality": "CN",
                              "role": "top",
                              "slug": "flandre"
                            },
                            {
                              "active": true,
                              "age": 28,
                              "birthday": "1998-03-14",
                              "first_name": "Lee",
                              "id": 839,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/839/jdg_scout_2025_split_1.png",
                              "last_name": "Ye-chan",
                              "modified_at": "2026-02-01T11:16:32Z",
                              "name": "Scout",
                              "nationality": "KR",
                              "role": "mid",
                              "slug": "scout"
                            },
                            {
                              "active": true,
                              "age": 27,
                              "birthday": "1998-06-06",
                              "first_name": "Ye",
                              "id": 2170,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/2170/ig_meiko_2025_split_1.png",
                              "last_name": "Tian",
                              "modified_at": "2026-01-03T08:07:03Z",
                              "name": "Meiko",
                              "nationality": "CN",
                              "role": "sup",
                              "slug": "meiko"
                            },
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2000-10-19",
                              "first_name": "Park",
                              "id": 8176,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/8176/edg_viper_2022_worlds.png",
                              "last_name": "Do-hyeon",
                              "modified_at": "2026-03-08T14:48:43Z",
                              "name": "Viper",
                              "nationality": "KR",
                              "role": "adc",
                              "slug": "viper-309f5be7-0007-492a-8d90-854914e5563d"
                            },
                            {
                              "active": true,
                              "age": 24,
                              "birthday": "2001-10-27",
                              "first_name": "Lijie",
                              "id": 21867,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/21867/fpx_jiejie_2025_split_3.png",
                              "last_name": "Zhao",
                              "modified_at": "2026-02-11T13:59:27Z",
                              "name": "Jiejie",
                              "nationality": "CN",
                              "role": "jun",
                              "slug": "jiejie"
                            }
                          ],
                          "team": {
                            "acronym": "EDG",
                            "dark_mode_image_url": null,
                            "id": 405,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/405/900px_e_dward_gaming_2017_lightmode.png",
                            "location": "CN",
                            "modified_at": "2026-02-07T14:44:44Z",
                            "name": "EDward Gaming",
                            "slug": "edward-gaming"
                          }
                        },
                        {
                          "players": [
                            {
                              "active": false,
                              "age": 28,
                              "birthday": "1998-02-03",
                              "first_name": "Han",
                              "id": 520,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/520/gen_peanut_2023_split_2.png",
                              "last_name": "Wang-ho",
                              "modified_at": "2025-12-30T11:43:51Z",
                              "name": "Peanut",
                              "nationality": "KR",
                              "role": "jun",
                              "slug": "peanut"
                            },
                            {
                              "active": true,
                              "age": 27,
                              "birthday": "1998-12-29",
                              "first_name": "Park",
                              "id": 1121,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/1121/jdg_ruler_2024_split_1.png",
                              "last_name": "Jae-hyuk",
                              "modified_at": "2026-03-08T14:51:09Z",
                              "name": "Ruler",
                              "nationality": "KR",
                              "role": "adc",
                              "slug": "ruler"
                            },
                            {
                              "active": true,
                              "age": 27,
                              "birthday": "1998-12-24",
                              "first_name": "Son",
                              "id": 1210,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/1210/kt_lehends_2023_split_2.png",
                              "last_name": "Si-woo",
                              "modified_at": "2026-02-01T11:16:32Z",
                              "name": "Lehends",
                              "nationality": "KR",
                              "role": "sup",
                              "slug": "lehends"
                            },
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2001-03-03",
                              "first_name": "Jeong",
                              "id": 15000,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/15000/gen_chovy_2023_split_2.png",
                              "last_name": "Ji-hoon",
                              "modified_at": "2026-03-08T14:51:08Z",
                              "name": "Chovy",
                              "nationality": "KR",
                              "role": "mid",
                              "slug": "chovy"
                            },
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2000-07-22",
                              "first_name": "Choi",
                              "id": 19282,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/19282/gen_doran_2023_split_2.png",
                              "last_name": "Hyeon-joon",
                              "modified_at": "2026-02-01T11:19:16Z",
                              "name": "Doran",
                              "nationality": "KR",
                              "role": "top",
                              "slug": "doran-2686e2c9-bd34-47fb-9d17-87debb7be1b6"
                            }
                          ],
                          "team": {
                            "acronym": "GEN",
                            "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/2882/499px_gen.g_esports_2019_full_darkmode.png",
                            "id": 2882,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/2882/500px_gen.g_esports_2019_full_lightmode.png",
                            "location": "KR",
                            "modified_at": "2026-03-08T14:51:09Z",
                            "name": "Gen.G",
                            "slug": "geng"
                          }
                        },
                        {
                          "players": [
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2000-03-30",
                              "first_name": "Emil",
                              "id": 1429,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/1429/rge_larssen_2024_split_1.png",
                              "last_name": "Larsson",
                              "modified_at": "2025-07-29T07:48:15Z",
                              "name": "Larssen",
                              "nationality": "SE",
                              "role": "mid",
                              "slug": "larssen"
                            },
                            {
                              "active": false,
                              "age": 31,
                              "birthday": "1995-01-18",
                              "first_name": "Andrei",
                              "id": 2159,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/2159/gx_odoamne_2024_split_1.png",
                              "last_name": "Pascu",
                              "modified_at": "2025-12-30T10:19:06Z",
                              "name": "Odoamne",
                              "nationality": "RO",
                              "role": "top",
                              "slug": "odoamne"
                            },
                            {
                              "active": true,
                              "age": 26,
                              "birthday": "2000-02-09",
                              "first_name": "Kim",
                              "id": 2538,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/2538/navi_malrang_2025_split_3.png",
                              "last_name": "Geun-seong",
                              "modified_at": "2025-12-30T16:22:49Z",
                              "name": "Malrang",
                              "nationality": "KR",
                              "role": "sup",
                              "slug": "malrang"
                            },
                            {
                              "active": true,
                              "age": 24,
                              "birthday": "2001-12-20",
                              "first_name": "Markos",
                              "id": 21577,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/21577/m8_comp_2025_split_2.png",
                              "last_name": "Stamkopoulos",
                              "modified_at": "2026-02-23T14:25:31Z",
                              "name": "Comp",
                              "nationality": "GR",
                              "role": "adc",
                              "slug": "comp"
                            },
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2000-10-20",
                              "first_name": "Adrian",
                              "id": 22950,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/22950/vks_trymbi_2025_split_3.png",
                              "last_name": "Trybus",
                              "modified_at": "2025-12-21T12:19:02Z",
                              "name": "Trymbi",
                              "nationality": "PL",
                              "role": "sup",
                              "slug": "trymbi"
                            }
                          ],
                          "team": {
                            "acronym": "RGE",
                            "dark_mode_image_url": null,
                            "id": 3983,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/3983/rogue__28_european_team_29logo_square.png",
                            "location": "US",
                            "modified_at": "2025-06-13T15:00:24Z",
                            "name": "Rogue",
                            "slug": "rogue"
                          }
                        },
                        {
                          "players": [
                            {
                              "active": true,
                              "age": 29,
                              "birthday": "1996-05-07",
                              "first_name": "Lee",
                              "id": 585,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                              "last_name": "Sang-hyeok",
                              "modified_at": "2026-02-01T11:19:16Z",
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
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/8158/t1_keria_2023_split_2.png",
                              "last_name": "Min-seok",
                              "modified_at": "2026-02-01T11:19:16Z",
                              "name": "Keria",
                              "nationality": "KR",
                              "role": "sup",
                              "slug": "keria"
                            },
                            {
                              "active": true,
                              "age": 24,
                              "birthday": "2002-02-06",
                              "first_name": "Lee",
                              "id": 19285,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/19285/t1_gumayusi_2023_split_2.png",
                              "last_name": "Min-hyeon",
                              "modified_at": "2026-01-06T07:15:49Z",
                              "name": "Gumayusi",
                              "nationality": "KR",
                              "role": "adc",
                              "slug": "gumayusi"
                            },
                            {
                              "active": true,
                              "age": 22,
                              "birthday": "2004-01-31",
                              "first_name": "Choi",
                              "id": 31391,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/31391/t1_zeus_2023_split_2.png",
                              "last_name": "Woo-je",
                              "modified_at": "2026-01-06T07:15:50Z",
                              "name": "Zeus",
                              "nationality": "KR",
                              "role": "top",
                              "slug": "zeus-choi-woo-je"
                            },
                            {
                              "active": true,
                              "age": 23,
                              "birthday": "2002-12-24",
                              "first_name": "Moon",
                              "id": 31392,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/31392/t1_oner_2023_split_2.png",
                              "last_name": "Hyeon-joon",
                              "modified_at": "2026-02-01T11:19:17Z",
                              "name": "Oner",
                              "nationality": "KR",
                              "role": "jun",
                              "slug": "oner"
                            }
                          ],
                          "team": {
                            "acronym": "T1",
                            "dark_mode_image_url": null,
                            "id": 126061,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                            "location": "KR",
                            "modified_at": "2026-02-01T11:19:17Z",
                            "name": "T1",
                            "slug": "t1"
                          }
                        },
                        {
                          "players": [
                            {
                              "active": true,
                              "age": 29,
                              "birthday": "1996-10-23",
                              "first_name": "Kim",
                              "id": 2169,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/2169/ezgif_3_4d5729796f.png",
                              "last_name": "Hyuk-kyu",
                              "modified_at": "2024-10-29T18:44:18Z",
                              "name": "Deft",
                              "nationality": "KR",
                              "role": "adc",
                              "slug": "deft"
                            },
                            {
                              "active": true,
                              "age": 26,
                              "birthday": "2000-03-11",
                              "first_name": "Hwang",
                              "id": 8172,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/8172/drx_kingen_2022_split_2.png",
                              "last_name": "Seong-hoon",
                              "modified_at": "2026-02-01T11:16:32Z",
                              "name": "Kingen",
                              "nationality": "KR",
                              "role": "top",
                              "slug": "kingen"
                            },
                            {
                              "active": true,
                              "age": 28,
                              "birthday": "1997-04-01",
                              "first_name": "Cho",
                              "id": 15425,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/15425/drx_bery_l_2022_split_2.png",
                              "last_name": "Geon-hee",
                              "modified_at": "2025-12-30T12:27:51Z",
                              "name": "BeryL",
                              "nationality": "KR",
                              "role": "sup",
                              "slug": "beryl"
                            },
                            {
                              "active": true,
                              "age": 24,
                              "birthday": "2001-08-31",
                              "first_name": "Lee",
                              "id": 22991,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/22991/ezgif_3_5240227326.png",
                              "last_name": "Ju-han",
                              "modified_at": "2026-02-07T14:44:45Z",
                              "name": "Juhan",
                              "nationality": "KR",
                              "role": "jun",
                              "slug": "salix"
                            },
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2000-03-21",
                              "first_name": "Hong",
                              "id": 24996,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/24996/tl_pyosik_2023_split_1.png",
                              "last_name": "Chang-hyeon",
                              "modified_at": "2026-02-08T13:14:45Z",
                              "name": "Pyosik",
                              "nationality": "KR",
                              "role": "jun",
                              "slug": "pyosik"
                            },
                            {
                              "active": true,
                              "age": 23,
                              "birthday": "2002-11-28",
                              "first_name": "Kim",
                              "id": 25391,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/25391/drx_zeka_2022_split_2.png",
                              "last_name": "Geon-woo",
                              "modified_at": "2026-01-06T07:15:50Z",
                              "name": "Zeka",
                              "nationality": "KR",
                              "role": "mid",
                              "slug": "zeka"
                            }
                          ],
                          "team": {
                            "acronym": "DRX",
                            "dark_mode_image_url": null,
                            "id": 126370,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                            "location": "KR",
                            "modified_at": "2026-02-08T13:14:48Z",
                            "name": "DRX",
                            "slug": "dragonx"
                          }
                        },
                        {
                          "players": [
                            {
                              "active": false,
                              "age": 26,
                              "birthday": "1999-07-17",
                              "first_name": "Jang",
                              "id": 8143,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/8143/fpx_nuguri_2021_split_2.png",
                              "last_name": "Ha-gwon",
                              "modified_at": "2025-12-30T12:26:41Z",
                              "name": "Nuguri",
                              "nationality": "KR",
                              "role": "top",
                              "slug": "nuguri"
                            },
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2000-07-22",
                              "first_name": "Heo",
                              "id": 8166,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/8166/dk_show_maker_2023_split_2.png",
                              "last_name": "Su",
                              "modified_at": "2026-02-08T13:14:46Z",
                              "name": "ShowMaker",
                              "nationality": "KR",
                              "role": "mid",
                              "slug": "showmaker"
                            },
                            {
                              "active": true,
                              "age": 24,
                              "birthday": "2001-06-18",
                              "first_name": "Kim",
                              "id": 18112,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/18112/dk_canyon_2023_split_2.png",
                              "last_name": "Geon-bu",
                              "modified_at": "2026-03-08T14:51:07Z",
                              "name": "Canyon",
                              "nationality": "KR",
                              "role": "jun",
                              "slug": "canyon"
                            },
                            {
                              "active": true,
                              "age": 25,
                              "birthday": "2001-02-01",
                              "first_name": "Kim",
                              "id": 19302,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/19302/dk_kellin_2023_split_2.png",
                              "last_name": "Hyeong-gyu",
                              "modified_at": "2026-03-08T14:48:43Z",
                              "name": "Kellin",
                              "nationality": "KR",
                              "role": "sup",
                              "slug": "kellin"
                            },
                            {
                              "active": true,
                              "age": 26,
                              "birthday": "2000-02-25",
                              "first_name": "Seo",
                              "id": 22959,
                              "image_url": "https://cdn-api.pandascore.co/images/player/image/22959/fpx_deokdam_2024_split_1.png",
                              "last_name": "Dae-gil",
                              "modified_at": "2026-02-08T13:14:45Z",
                              "name": "deokdam",
                              "nationality": "KR",
                              "role": "adc",
                              "slug": "feiz"
                            }
                          ],
                          "team": {
                            "acronym": "DK",
                            "dark_mode_image_url": null,
                            "id": 128409,
                            "image_url": "https://cdn-api.pandascore.co/images/team/image/128409/dwg_ki_alogo_square.png",
                            "location": "KR",
                            "modified_at": "2023-01-09T17:17:56Z",
                            "name": "DWG KIA",
                            "slug": "dwg-kia"
                          }
                        }
                      ],
                      "has_bracket": true,
                      "id": 9049,
                      "league": {
                        "id": 297,
                        "image_url": "https://cdn-api.pandascore.co/images/league/image/297/worlds-png",
                        "modified_at": "2023-12-06T15:53:28Z",
                        "name": "Worlds",
                        "slug": "league-of-legends-world-championship",
                        "url": null
                      },
                      "league_id": 297,
                      "live_supported": true,
                      "matches": [
                        {
                          "begin_at": "2022-10-20T21:07:23Z",
                          "detailed_stats": true,
                          "draw": false,
                          "end_at": "2022-10-20T23:28:55Z",
                          "forfeit": false,
                          "game_advantage": null,
                          "id": 651262,
                          "live": {
                            "opens_at": "2022-10-20T20:52:23.000000Z",
                            "supported": true,
                            "url": "wss://live.pandascore.co/matches/651262"
                          },
                          "match_type": "best_of",
                          "modified_at": "2022-10-24T14:09:07Z",
                          "name": "Quarterfinal 1: JDG vs RGE",
                          "number_of_games": 5,
                          "original_scheduled_at": "2022-10-20T21:00:00Z",
                          "rescheduled": false,
                          "scheduled_at": "2022-10-20T21:00:00Z",
                          "slug": "2022-10-20-0870dc33-031f-4f03-bd2a-148cc897b99e",
                          "status": "finished",
                          "streams_list": [
                            {
                              "embed_url": "https://player.twitch.tv/?channel=otplol_",
                              "language": "fr",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/otplol_"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=lvpes",
                              "language": "es",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/lvpes"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=riotgames",
                              "language": "en",
                              "main": true,
                              "official": true,
                              "raw_url": "https://www.twitch.tv/riotgames"
                            }
                          ],
                          "tournament_id": 9049,
                          "winner_id": 318,
                          "winner_type": "Team"
                        },
                        {
                          "begin_at": "2022-10-21T21:07:42Z",
                          "detailed_stats": true,
                          "draw": false,
                          "end_at": "2022-10-21T23:45:39Z",
                          "forfeit": false,
                          "game_advantage": null,
                          "id": 651263,
                          "live": {
                            "opens_at": "2022-10-21T20:52:42.000000Z",
                            "supported": true,
                            "url": "wss://live.pandascore.co/matches/651263"
                          },
                          "match_type": "best_of",
                          "modified_at": "2022-10-24T14:09:05Z",
                          "name": "Quarterfinal 2: T1 vs RNG",
                          "number_of_games": 5,
                          "original_scheduled_at": "2022-10-21T21:00:00Z",
                          "rescheduled": false,
                          "scheduled_at": "2022-10-21T21:00:00Z",
                          "slug": "2022-10-21-60f37d18-eab0-4f05-87f0-9478b23a2395",
                          "status": "finished",
                          "streams_list": [
                            {
                              "embed_url": "https://player.twitch.tv/?channel=otplol_",
                              "language": "fr",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/otplol_"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=lvpes",
                              "language": "es",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/lvpes"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=riotgames",
                              "language": "en",
                              "main": true,
                              "official": true,
                              "raw_url": "https://www.twitch.tv/riotgames"
                            }
                          ],
                          "tournament_id": 9049,
                          "winner_id": 126061,
                          "winner_type": "Team"
                        },
                        {
                          "begin_at": "2022-10-22T21:11:10Z",
                          "detailed_stats": true,
                          "draw": false,
                          "end_at": "2022-10-23T01:34:43Z",
                          "forfeit": false,
                          "game_advantage": null,
                          "id": 651264,
                          "live": {
                            "opens_at": "2022-10-22T20:56:10.000000Z",
                            "supported": true,
                            "url": "wss://live.pandascore.co/matches/651264"
                          },
                          "match_type": "best_of",
                          "modified_at": "2022-10-24T14:09:00Z",
                          "name": "Quarterfinal 3: GEN vs DK",
                          "number_of_games": 5,
                          "original_scheduled_at": "2022-10-22T21:00:00Z",
                          "rescheduled": false,
                          "scheduled_at": "2022-10-22T21:00:00Z",
                          "slug": "2022-10-22-3579f36c-e4cd-4207-97cc-82a79eb8c600",
                          "status": "finished",
                          "streams_list": [
                            {
                              "embed_url": "https://player.twitch.tv/?channel=otplol_",
                              "language": "fr",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/otplol_"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=lvpes",
                              "language": "es",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/lvpes"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=riotgames",
                              "language": "en",
                              "main": true,
                              "official": true,
                              "raw_url": "https://www.twitch.tv/riotgames"
                            }
                          ],
                          "tournament_id": 9049,
                          "winner_id": 2882,
                          "winner_type": "Team"
                        },
                        {
                          "begin_at": "2022-10-23T21:07:59Z",
                          "detailed_stats": true,
                          "draw": false,
                          "end_at": "2022-10-24T02:11:52Z",
                          "forfeit": false,
                          "game_advantage": null,
                          "id": 651265,
                          "live": {
                            "opens_at": "2022-10-23T20:52:59.000000Z",
                            "supported": true,
                            "url": "wss://live.pandascore.co/matches/651265"
                          },
                          "match_type": "best_of",
                          "modified_at": "2022-10-24T14:08:53Z",
                          "name": "Quarterfinal 4: DRX vs EDG",
                          "number_of_games": 5,
                          "original_scheduled_at": "2022-10-23T21:00:00Z",
                          "rescheduled": false,
                          "scheduled_at": "2022-10-23T21:00:00Z",
                          "slug": "2022-10-23-89552266-f928-4e17-b4ac-d9d15d20d9a5",
                          "status": "finished",
                          "streams_list": [
                            {
                              "embed_url": "https://player.twitch.tv/?channel=otplol_",
                              "language": "fr",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/otplol_"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=lvpes",
                              "language": "es",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/lvpes"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=riotgames",
                              "language": "en",
                              "main": true,
                              "official": true,
                              "raw_url": "https://www.twitch.tv/riotgames"
                            }
                          ],
                          "tournament_id": 9049,
                          "winner_id": 126370,
                          "winner_type": "Team"
                        },
                        {
                          "begin_at": "2022-10-29T21:12:20Z",
                          "detailed_stats": true,
                          "draw": false,
                          "end_at": "2022-10-30T00:36:05Z",
                          "forfeit": false,
                          "game_advantage": null,
                          "id": 651266,
                          "live": {
                            "opens_at": "2022-10-29T20:57:20.000000Z",
                            "supported": true,
                            "url": "wss://live.pandascore.co/matches/651266"
                          },
                          "match_type": "best_of",
                          "modified_at": "2022-10-30T00:46:30Z",
                          "name": "Semifinal 1: JDG vs T1",
                          "number_of_games": 5,
                          "original_scheduled_at": "2022-10-29T21:00:00Z",
                          "rescheduled": false,
                          "scheduled_at": "2022-10-29T21:00:00Z",
                          "slug": "jd-gaming-2022-10-29",
                          "status": "finished",
                          "streams_list": [
                            {
                              "embed_url": "https://player.twitch.tv/?channel=otplol_",
                              "language": "fr",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/otplol_"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=lvpes",
                              "language": "es",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/lvpes"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=riotgames",
                              "language": "en",
                              "main": true,
                              "official": true,
                              "raw_url": "https://www.twitch.tv/riotgames"
                            }
                          ],
                          "tournament_id": 9049,
                          "winner_id": 126061,
                          "winner_type": "Team"
                        },
                        {
                          "begin_at": "2022-10-30T21:08:52Z",
                          "detailed_stats": true,
                          "draw": false,
                          "end_at": "2022-10-31T00:42:32Z",
                          "forfeit": false,
                          "game_advantage": null,
                          "id": 651267,
                          "live": {
                            "opens_at": "2022-10-30T20:53:52.000000Z",
                            "supported": true,
                            "url": "wss://live.pandascore.co/matches/651267"
                          },
                          "match_type": "best_of",
                          "modified_at": "2022-10-31T00:56:03Z",
                          "name": "Semifinal 2: GEN vs DRX",
                          "number_of_games": 5,
                          "original_scheduled_at": "2022-10-30T21:00:00Z",
                          "rescheduled": false,
                          "scheduled_at": "2022-10-30T21:00:00Z",
                          "slug": "gen-g-2022-10-30",
                          "status": "finished",
                          "streams_list": [
                            {
                              "embed_url": "https://player.twitch.tv/?channel=otplol_",
                              "language": "fr",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/otplol_"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=lvpes",
                              "language": "es",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/lvpes"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=riotgames",
                              "language": "en",
                              "main": true,
                              "official": true,
                              "raw_url": "https://www.twitch.tv/riotgames"
                            }
                          ],
                          "tournament_id": 9049,
                          "winner_id": 126370,
                          "winner_type": "Team"
                        },
                        {
                          "begin_at": "2022-11-06T00:52:58Z",
                          "detailed_stats": true,
                          "draw": false,
                          "end_at": "2022-11-06T05:25:23Z",
                          "forfeit": false,
                          "game_advantage": null,
                          "id": 651268,
                          "live": {
                            "opens_at": "2022-11-06T00:37:58.000000Z",
                            "supported": true,
                            "url": "wss://live.pandascore.co/matches/651268"
                          },
                          "match_type": "best_of",
                          "modified_at": "2022-11-06T05:37:47Z",
                          "name": "Grand final: T1 vs DRX",
                          "number_of_games": 5,
                          "original_scheduled_at": "2022-11-06T00:00:00Z",
                          "rescheduled": true,
                          "scheduled_at": "2022-11-06T00:55:00Z",
                          "slug": "t1-2022-11-06",
                          "status": "finished",
                          "streams_list": [
                            {
                              "embed_url": "https://www.bilibili.com/blackboard/live/live-activity-player.html?cid=6",
                              "language": "zh",
                              "main": false,
                              "official": false,
                              "raw_url": "https://live.bilibili.com/6"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=riotgamesturkish",
                              "language": "tr",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/riotgamesturkish"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=cblol",
                              "language": "pt",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/cblol"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=polsatgames",
                              "language": "pl",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/polsatgames"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=hitpointcz",
                              "language": "cs",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/hitpointcz"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=lck_korea",
                              "language": "ko",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/lck_korea"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=summonersinnlive",
                              "language": "de",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/summonersinnlive"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=otplol_",
                              "language": "fr",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/otplol_"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=lvpes",
                              "language": "es",
                              "main": false,
                              "official": false,
                              "raw_url": "https://www.twitch.tv/lvpes"
                            },
                            {
                              "embed_url": "https://player.twitch.tv/?channel=riotgames",
                              "language": "en",
                              "main": true,
                              "official": true,
                              "raw_url": "https://www.twitch.tv/riotgames"
                            }
                          ],
                          "tournament_id": 9049,
                          "winner_id": 126370,
                          "winner_type": "Team"
                        }
                      ],
                      "modified_at": "2023-04-25T16:27:42Z",
                      "name": "Playoffs",
                      "prizepool": "2225000 United States Dollar",
                      "region": null,
                      "serie": {
                        "begin_at": "2022-09-28T22:00:00Z",
                        "end_at": "2022-11-06T05:25:00Z",
                        "full_name": "2022",
                        "id": 5065,
                        "league_id": 297,
                        "modified_at": "2022-11-08T16:14:11Z",
                        "name": null,
                        "season": null,
                        "slug": "league-of-legends-world-championship-2022",
                        "winner_id": 126370,
                        "winner_type": "Team",
                        "year": 2022
                      },
                      "serie_id": 5065,
                      "slug": "league-of-legends-world-championship-2022-playoffs",
                      "teams": [
                        {
                          "acronym": "RNG",
                          "dark_mode_image_url": null,
                          "id": 74,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/74/royal-never-give-up-cyacqft1.png",
                          "location": "CN",
                          "modified_at": "2025-12-11T22:45:26Z",
                          "name": "Royal Never Give Up",
                          "slug": "royal-never-give-up"
                        },
                        {
                          "acronym": "JDG",
                          "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/318/746px_jd_gaming_2021_full_allmode.png",
                          "id": 318,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/318/746px_jd_gaming_2021_full_allmode.png",
                          "location": "CN",
                          "modified_at": "2026-03-08T14:51:07Z",
                          "name": "JD Gaming",
                          "slug": "qg-reapers"
                        },
                        {
                          "acronym": "EDG",
                          "dark_mode_image_url": null,
                          "id": 405,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/405/900px_e_dward_gaming_2017_lightmode.png",
                          "location": "CN",
                          "modified_at": "2026-02-07T14:44:44Z",
                          "name": "EDward Gaming",
                          "slug": "edward-gaming"
                        },
                        {
                          "acronym": "GEN",
                          "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/2882/499px_gen.g_esports_2019_full_darkmode.png",
                          "id": 2882,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/2882/500px_gen.g_esports_2019_full_lightmode.png",
                          "location": "KR",
                          "modified_at": "2026-03-08T14:51:09Z",
                          "name": "Gen.G",
                          "slug": "geng"
                        },
                        {
                          "acronym": "RGE",
                          "dark_mode_image_url": null,
                          "id": 3983,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/3983/rogue__28_european_team_29logo_square.png",
                          "location": "US",
                          "modified_at": "2025-06-13T15:00:24Z",
                          "name": "Rogue",
                          "slug": "rogue"
                        },
                        {
                          "acronym": "T1",
                          "dark_mode_image_url": null,
                          "id": 126061,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/126061/t_oscq04.png",
                          "location": "KR",
                          "modified_at": "2026-02-01T11:19:17Z",
                          "name": "T1",
                          "slug": "t1"
                        },
                        {
                          "acronym": "DRX",
                          "dark_mode_image_url": null,
                          "id": 126370,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                          "location": "KR",
                          "modified_at": "2026-02-08T13:14:48Z",
                          "name": "DRX",
                          "slug": "dragonx"
                        },
                        {
                          "acronym": "DK",
                          "dark_mode_image_url": null,
                          "id": 128409,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/128409/dwg_ki_alogo_square.png",
                          "location": "KR",
                          "modified_at": "2023-01-09T17:17:56Z",
                          "name": "DWG KIA",
                          "slug": "dwg-kia"
                        }
                      ],
                      "tier": "s",
                      "type": null,
                      "videogame": {
                        "id": 1,
                        "name": "LoL",
                        "slug": "league-of-legends"
                      },
                      "videogame_title": null,
                      "winner_id": 126370,
                      "winner_type": "Team"
                    }
                  }
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLStatsForTeamByTournament"
            }
          }
        },
        "description": "Statistics of a League-of-Legends team by tournament\n\nDeprecated fields:\n- last_games[].players[].minions_killed\n"
      }
    },
    "schemas": {
      "LoLStatsForTeamByTournament": {
        "additionalProperties": false,
        "deprecated": false,
        "description": "Team's aggregated statistics for a tournament",
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
            "additionalProperties": false,
            "deprecated": false,
            "description": "Team's statistics for a tournament",
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
              },
              "tournament": {
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
                  "expected_roster": {
                    "items": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
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
                        }
                      },
                      "required": [
                        "players",
                        "team"
                      ],
                      "title": "TournamentRosterItem",
                      "type": "object"
                    },
                    "title": "TournamentRosterItems",
                    "type": "array"
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
                  "live_supported": {
                    "description": "Whether live is supported",
                    "title": "TournamentLiveSupported",
                    "type": "boolean"
                  },
                  "matches": {
                    "items": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "begin_at": {
                          "deprecated": false,
                          "format": "date-time",
                          "minLength": 1,
                          "nullable": true,
                          "title": "MatchBeginAt",
                          "type": "string"
                        },
                        "detailed_stats": {
                          "description": "Whether the match offers full stats",
                          "title": "MatchDetailedStats",
                          "type": "boolean"
                        },
                        "draw": {
                          "description": "Whether result of the match is a draw",
                          "title": "MatchIsDraw",
                          "type": "boolean"
                        },
                        "end_at": {
                          "deprecated": false,
                          "format": "date-time",
                          "minLength": 1,
                          "nullable": true,
                          "title": "MatchEndAt",
                          "type": "string"
                        },
                        "forfeit": {
                          "description": "Whether match was forfeited",
                          "title": "MatchIsForfeit",
                          "type": "boolean"
                        },
                        "game_advantage": {
                          "deprecated": false,
                          "description": "ID of the opponent with a game advantage",
                          "minimum": 1,
                          "nullable": true,
                          "title": "GameAdvantageOpponent",
                          "type": "integer"
                        },
                        "id": {
                          "minimum": 1,
                          "title": "MatchID",
                          "type": "integer"
                        },
                        "live": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "opens_at": {
                              "deprecated": false,
                              "format": "date-time",
                              "minLength": 1,
                              "nullable": true,
                              "title": "MatchLiveOpensAt",
                              "type": "string"
                            },
                            "supported": {
                              "description": "Whether live is supported",
                              "title": "MatchLiveIsSupported",
                              "type": "boolean"
                            },
                            "url": {
                              "deprecated": false,
                              "format": "uri",
                              "nullable": true,
                              "title": "MatchLiveURL",
                              "type": "string"
                            }
                          },
                          "required": [
                            "opens_at",
                            "supported",
                            "url"
                          ],
                          "title": "MatchLive",
                          "type": "object"
                        },
                        "match_type": {
                          "enum": [
                            "all_games_played",
                            "best_of",
                            "custom",
                            "first_to",
                            "ow_best_of",
                            "red_bull_home_ground"
                          ],
                          "title": "MatchType",
                          "type": "string"
                        },
                        "modified_at": {
                          "format": "date-time",
                          "minLength": 1,
                          "title": "MatchModifiedAt",
                          "type": "string"
                        },
                        "name": {
                          "title": "MatchName",
                          "type": "string"
                        },
                        "number_of_games": {
                          "description": "Number of games",
                          "minimum": 0,
                          "title": "GameCount",
                          "type": "integer"
                        },
                        "original_scheduled_at": {
                          "deprecated": false,
                          "format": "date-time",
                          "minLength": 1,
                          "nullable": true,
                          "title": "MatchOriginalScheduledAt",
                          "type": "string"
                        },
                        "rescheduled": {
                          "deprecated": false,
                          "description": "Whether match has been rescheduled",
                          "nullable": true,
                          "title": "MatchIsRescheduled",
                          "type": "boolean"
                        },
                        "scheduled_at": {
                          "deprecated": false,
                          "format": "date-time",
                          "minLength": 1,
                          "nullable": true,
                          "title": "MatchScheduledAt",
                          "type": "string"
                        },
                        "slug": {
                          "deprecated": false,
                          "minLength": 1,
                          "nullable": true,
                          "pattern": "^[ a-zA-Z0-9_-]+$",
                          "title": "MatchSlug",
                          "type": "string"
                        },
                        "status": {
                          "enum": [
                            "canceled",
                            "finished",
                            "not_started",
                            "postponed",
                            "running"
                          ],
                          "title": "MatchStatus",
                          "type": "string"
                        },
                        "streams_list": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "embed_url": {
                                "deprecated": false,
                                "description": "URL to embed in an iframe.",
                                "format": "uri",
                                "nullable": true,
                                "title": "StreamEmbedURL",
                                "type": "string"
                              },
                              "language": {
                                "description": "Language alpha-2 code according to ISO 649-1 standard.",
                                "enum": [
                                  "aa",
                                  "ab",
                                  "ae",
                                  "af",
                                  "ak",
                                  "am",
                                  "an",
                                  "ar",
                                  "as",
                                  "av",
                                  "ay",
                                  "az",
                                  "ba",
                                  "be",
                                  "bg",
                                  "bh",
                                  "bi",
                                  "bm",
                                  "bn",
                                  "bo",
                                  "br",
                                  "bs",
                                  "ca",
                                  "ce",
                                  "ch",
                                  "co",
                                  "cr",
                                  "cs",
                                  "cu",
                                  "cv",
                                  "cy",
                                  "da",
                                  "de",
                                  "dv",
                                  "dz",
                                  "ee",
                                  "el",
                                  "en",
                                  "eo",
                                  "es",
                                  "et",
                                  "eu",
                                  "fa",
                                  "ff",
                                  "fi",
                                  "fj",
                                  "fo",
                                  "fr",
                                  "fy",
                                  "ga",
                                  "gd",
                                  "gl",
                                  "gn",
                                  "gu",
                                  "gv",
                                  "ha",
                                  "he",
                                  "hi",
                                  "ho",
                                  "hr",
                                  "ht",
                                  "hu",
                                  "hy",
                                  "hz",
                                  "ia",
                                  "id",
                                  "ie",
                                  "ig",
                                  "ii",
                                  "ik",
                                  "io",
                                  "is",
                                  "it",
                                  "iu",
                                  "ja",
                                  "jv",
                                  "ka",
                                  "kg",
                                  "ki",
                                  "kj",
                                  "kk",
                                  "kl",
                                  "km",
                                  "kn",
                                  "ko",
                                  "kr",
                                  "ks",
                                  "ku",
                                  "kv",
                                  "kw",
                                  "ky",
                                  "la",
                                  "lb",
                                  "lg",
                                  "li",
                                  "ln",
                                  "lo",
                                  "lt",
                                  "lu",
                                  "lv",
                                  "mg",
                                  "mh",
                                  "mi",
                                  "mk",
                                  "ml",
                                  "mn",
                                  "mr",
                                  "ms",
                                  "mt",
                                  "my",
                                  "na",
                                  "nb",
                                  "nd",
                                  "ne",
                                  "ng",
                                  "nl",
                                  "nn",
                                  "no",
                                  "nr",
                                  "nv",
                                  "ny",
                                  "oc",
                                  "oj",
                                  "om",
                                  "or",
                                  "os",
                                  "pa",
                                  "pi",
                                  "pl",
                                  "ps",
                                  "pt",
                                  "qu",
                                  "rm",
                                  "rn",
                                  "ro",
                                  "ru",
                                  "rw",
                                  "sa",
                                  "sc",
                                  "sd",
                                  "se",
                                  "sg",
                                  "si",
                                  "sk",
                                  "sl",
                                  "sm",
                                  "sn",
                                  "so",
                                  "sq",
                                  "sr",
                                  "ss",
                                  "st",
                                  "su",
                                  "sv",
                                  "sw",
                                  "ta",
                                  "te",
                                  "tg",
                                  "th",
                                  "ti",
                                  "tk",
                                  "tl",
                                  "tn",
                                  "to",
                                  "tr",
                                  "ts",
                                  "tt",
                                  "tw",
                                  "ty",
                                  "ug",
                                  "uk",
                                  "ur",
                                  "uz",
                                  "ve",
                                  "vi",
                                  "vo",
                                  "wa",
                                  "wo",
                                  "xh",
                                  "yi",
                                  "yo",
                                  "za",
                                  "zh",
                                  "zu"
                                ],
                                "title": "StreamLanguage",
                                "type": "string"
                              },
                              "main": {
                                "description": "Whether it is the main stream. Main stream is always official.",
                                "title": "StreamIsMain",
                                "type": "boolean"
                              },
                              "official": {
                                "description": "Whether it is an official broadcast.",
                                "title": "StreamIsOfficial",
                                "type": "boolean"
                              },
                              "raw_url": {
                                "description": "URL to the stream on host website.",
                                "format": "uri",
                                "title": "StreamURL",
                                "type": "string"
                              }
                            },
                            "required": [
                              "embed_url",
                              "language",
                              "main",
                              "official",
                              "raw_url"
                            ],
                            "title": "Stream",
                            "type": "object"
                          },
                          "title": "StreamsList",
                          "type": "array"
                        },
                        "tournament_id": {
                          "minimum": 1,
                          "title": "TournamentID",
                          "type": "integer"
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
                          "enum": [
                            "Player",
                            "Team"
                          ],
                          "title": "MatchWinnerType",
                          "type": "string"
                        }
                      },
                      "required": [
                        "begin_at",
                        "detailed_stats",
                        "draw",
                        "end_at",
                        "forfeit",
                        "game_advantage",
                        "id",
                        "live",
                        "match_type",
                        "modified_at",
                        "name",
                        "number_of_games",
                        "original_scheduled_at",
                        "rescheduled",
                        "scheduled_at",
                        "slug",
                        "status",
                        "streams_list",
                        "tournament_id",
                        "winner_id",
                        "winner_type"
                      ],
                      "title": "BaseMatch",
                      "type": "object"
                    },
                    "title": "BaseMatches",
                    "type": "array"
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
                  "serie": {
                    "additionalProperties": false,
                    "deprecated": false,
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
                      "league_id",
                      "modified_at",
                      "name",
                      "season",
                      "slug",
                      "winner_id",
                      "winner_type",
                      "year"
                    ],
                    "title": "BaseSerie",
                    "type": "object"
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
                  "teams": {
                    "items": {
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
                    "title": "BaseTeams",
                    "type": "array"
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
                  }
                },
                "required": [
                  "begin_at",
                  "country",
                  "detailed_stats",
                  "end_at",
                  "expected_roster",
                  "has_bracket",
                  "id",
                  "league",
                  "league_id",
                  "live_supported",
                  "matches",
                  "modified_at",
                  "name",
                  "prizepool",
                  "region",
                  "serie",
                  "serie_id",
                  "slug",
                  "teams",
                  "tier",
                  "type",
                  "videogame",
                  "videogame_title",
                  "winner_id",
                  "winner_type"
                ],
                "title": "Tournament",
                "type": "object"
              }
            },
            "required": [
              "averages",
              "games_count",
              "totals",
              "tournament"
            ],
            "title": "LoLTeamByTournamentStat",
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
          "stats"
        ],
        "title": "LoLStatsForTeamByTournament",
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
      "TournamentIDOrSlug": {
        "description": "A tournament ID or slug",
        "oneOf": [
          {
            "minimum": 1,
            "title": "TournamentID",
            "type": "integer"
          },
          {
            "minLength": 1,
            "pattern": "^[a-z0-9_-]+$",
            "title": "TournamentSlug",
            "type": "string"
          }
        ],
        "title": "TournamentIDOrSlug"
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
    "/lol/tournaments/{tournament_id_or_slug}/teams/{team_id_or_slug}/stats": {
      "get": {
        "description": "Get detailed statistics of a given League-of-Legends team for the given tournament\n> ℹ️  \n> \n> This endpoint is only available to customers with a historical or real-time data plan",
        "operationId": "get_lol_tournaments_tournamentIdOrSlug_teams_teamIdOrSlug_stats",
        "parameters": [
          {
            "description": "A tournament ID or slug",
            "in": "path",
            "name": "tournament_id_or_slug",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/TournamentIDOrSlug"
            }
          },
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
            "$ref": "#/components/responses/LoLStatsForTeamByTournament"
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
        "summary": "Get stats for LoL team on tournament",
        "tags": [
          "LoL stats"
        ],
        "x-pandascore-plan": "Historical plan",
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/tournaments/{tournament_id_or_slug}/teams/{team_id_or_slug}/stats' \\\n     --header 'accept: application/json'\n",
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