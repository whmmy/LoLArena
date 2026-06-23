> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get past LoL tournaments

List past League of Legends tournaments
> ℹ️  
> 
> This endpoint is available to all customers

# OpenAPI definition

```json
{
  "components": {
    "parameters": {
      "Page": {
        "description": "Pagination in the form of `page=2` or `page[size]=30&page[number]=2`",
        "in": "query",
        "name": "page",
        "required": false,
        "schema": {
          "oneOf": [
            {
              "default": 1,
              "minimum": 1,
              "type": "integer"
            },
            {
              "additionalProperties": false,
              "properties": {
                "number": {
                  "default": 1,
                  "minimum": 1,
                  "type": "integer"
                },
                "size": {
                  "default": 50,
                  "maximum": 100,
                  "minimum": 1,
                  "type": "integer"
                }
              },
              "type": "object"
            }
          ]
        }
      },
      "PerPage": {
        "description": "Equivalent to `page[size]`",
        "example": 5,
        "in": "query",
        "name": "per_page",
        "required": false,
        "schema": {
          "default": 50,
          "maximum": 100,
          "minimum": 1,
          "type": "integer"
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
      "LoLShortTournaments": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/tournaments?page[size]=1": {
                "description": "/lol/tournaments?page[size]=1",
                "value": [
                  {
                    "begin_at": "2026-03-23T16:00:00Z",
                    "country": null,
                    "detailed_stats": true,
                    "end_at": "2026-04-21T20:00:00Z",
                    "expected_roster": [
                      {
                        "players": [
                          {
                            "active": true,
                            "age": 26,
                            "birthday": "1999-11-26",
                            "first_name": "Bartłomiej",
                            "id": 24638,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/24638/mdk_fresskowy_2024_split_1.png",
                            "last_name": "Przewoźnik",
                            "modified_at": "2026-03-16T12:57:14Z",
                            "name": "Fresskowy",
                            "nationality": "PL",
                            "role": "mid",
                            "slug": "fresskowy"
                          },
                          {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-11-06",
                            "first_name": "Tiago",
                            "id": 28760,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/28760/220px_egn_time_2019_split_2.png",
                            "last_name": "Almeida",
                            "modified_at": "2026-03-16T12:57:15Z",
                            "name": "Time",
                            "nationality": "PT",
                            "role": "jun",
                            "slug": "time-tiago-almeida"
                          },
                          {
                            "active": true,
                            "age": 20,
                            "birthday": "2005-10-11",
                            "first_name": "Mohamed",
                            "id": 46985,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/46985/bdsa_myrtus_2025_split_2.png",
                            "last_name": "Rahli",
                            "modified_at": "2026-03-16T12:57:14Z",
                            "name": "Myrtus",
                            "nationality": "FR",
                            "role": "sup",
                            "slug": "myrtus"
                          },
                          {
                            "active": true,
                            "age": 18,
                            "birthday": "2008-01-18",
                            "first_name": "Ivan",
                            "id": 54430,
                            "image_url": null,
                            "last_name": "Bilous",
                            "modified_at": "2026-03-16T12:57:15Z",
                            "name": "NightSlayer",
                            "nationality": "UA",
                            "role": "top",
                            "slug": "slayer3"
                          },
                          {
                            "active": true,
                            "age": 22,
                            "birthday": "2003-06-20",
                            "first_name": "Zayan",
                            "id": 58177,
                            "image_url": null,
                            "last_name": "Taeau",
                            "modified_at": "2026-03-16T12:57:13Z",
                            "name": "13",
                            "nationality": "FR",
                            "role": "adc",
                            "slug": "player-13"
                          }
                        ],
                        "team": {
                          "acronym": "KOI.F",
                          "dark_mode_image_url": null,
                          "id": 363,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/363/movistar_ko_ilogo_square.png",
                          "location": "ES",
                          "modified_at": "2026-03-16T12:57:15Z",
                          "name": "⁠Movistar KOI Fénix",
                          "slug": "movistar-riders"
                        }
                      },
                      {
                        "players": [
                          {
                            "active": true,
                            "age": 26,
                            "birthday": "1999-07-01",
                            "first_name": "Felix",
                            "id": 23604,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/23604/sly_kryze_2025_split_2.png",
                            "last_name": "Hellström",
                            "modified_at": "2026-03-16T12:57:17Z",
                            "name": "Kryze",
                            "nationality": "SE",
                            "role": "top",
                            "slug": "kryze"
                          },
                          {
                            "active": true,
                            "age": 24,
                            "birthday": "2001-12-30",
                            "first_name": "Kang",
                            "id": 25419,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/25419/dp_jool_2023_split_1.png",
                            "last_name": "Dong-soo",
                            "modified_at": "2026-03-16T12:57:17Z",
                            "name": "Jool",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "nasub"
                          },
                          {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-07-15",
                            "first_name": "Kim",
                            "id": 35882,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/35882/kcb_piero_2025_split_2.png",
                            "last_name": "Jeong-hoon",
                            "modified_at": "2026-03-16T12:57:17Z",
                            "name": "Piero",
                            "nationality": "KR",
                            "role": "sup",
                            "slug": "bmxpiero"
                          },
                          {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-05-16",
                            "first_name": "Lanzo",
                            "id": 39877,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/39877/m8_zicssi_2025_split_2.png",
                            "last_name": "Ciajolo",
                            "modified_at": "2026-03-16T12:57:17Z",
                            "name": "Zicssi",
                            "nationality": "FR",
                            "role": "jun",
                            "slug": "zicssiflay"
                          },
                          {
                            "active": true,
                            "age": 20,
                            "birthday": "2005-10-10",
                            "first_name": "Berat",
                            "id": 47380,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/47380/gxp_aetinoth_2024_split_2.png",
                            "last_name": "Tıknazoğlu",
                            "modified_at": "2026-03-16T12:57:16Z",
                            "name": "Aetinoth",
                            "nationality": "TR",
                            "role": "adc",
                            "slug": "aetinoth"
                          }
                        ],
                        "team": {
                          "acronym": "SLY",
                          "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/1449/solary_darkmode.png",
                          "id": 1449,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/1449/123px_solarylogo_square.png",
                          "location": "FR",
                          "modified_at": "2026-03-16T12:57:17Z",
                          "name": "Solary",
                          "slug": "solary"
                        }
                      },
                      {
                        "players": [
                          {
                            "active": true,
                            "age": 27,
                            "birthday": "1998-11-19",
                            "first_name": "Norman",
                            "id": 18037,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/18037/th_kaiser_2024_split_1.png",
                            "last_name": "Kaiser",
                            "modified_at": "2026-03-16T12:53:45Z",
                            "name": "Kaiser",
                            "nationality": "DE",
                            "role": "sup",
                            "slug": "gistick"
                          },
                          {
                            "active": true,
                            "age": 26,
                            "birthday": "2000-01-01",
                            "first_name": "Steven",
                            "id": 25876,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/25876/bds.a_reeker_2024_split_1.png",
                            "last_name": "Chen",
                            "modified_at": "2026-03-16T12:53:45Z",
                            "name": "Reeker",
                            "nationality": "DE",
                            "role": "mid",
                            "slug": "reeker"
                          },
                          {
                            "active": true,
                            "age": 26,
                            "birthday": "1999-06-19",
                            "first_name": "Johannes",
                            "id": 31675,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31675/ross_fun_k3y_2025_split_3.png",
                            "last_name": "Werner",
                            "modified_at": "2026-03-16T12:53:43Z",
                            "name": "Fun K3y",
                            "nationality": "DE",
                            "role": "adc",
                            "slug": "funk3y"
                          },
                          {
                            "active": true,
                            "age": 24,
                            "birthday": "2001-10-22",
                            "first_name": "Joel",
                            "id": 32032,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/32032/bds_irrelevant_2025_split_1.png",
                            "last_name": "Miro Scharoll",
                            "modified_at": "2026-03-16T12:53:45Z",
                            "name": "Irrelevant",
                            "nationality": "DE",
                            "role": "top",
                            "slug": "gw-irrelevant"
                          },
                          {
                            "active": true,
                            "age": null,
                            "birthday": null,
                            "first_name": "Seyit",
                            "id": 42191,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/42191/ezy_habuubu_2021.png",
                            "last_name": "Cüce",
                            "modified_at": "2026-03-16T12:53:45Z",
                            "name": "Habubu",
                            "nationality": "DE",
                            "role": "jun",
                            "slug": "habubu"
                          }
                        ],
                        "team": {
                          "acronym": "BIG",
                          "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/125905/122px_big_2020_darkmode.png",
                          "id": 125905,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/125905/berlin_international_gaminglogo_square.png",
                          "location": "DE",
                          "modified_at": "2026-03-16T12:53:45Z",
                          "name": "BIG",
                          "slug": "big-league-of-legends"
                        }
                      },
                      {
                        "players": [
                          {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-06-06",
                            "first_name": "Linus",
                            "id": 23644,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/23644/ross_royal_kanin_2025_split_1.png",
                            "last_name": "Grönlund",
                            "modified_at": "2026-03-16T12:53:49Z",
                            "name": "RoyalKanin",
                            "nationality": "SE",
                            "role": "mid",
                            "slug": "royalkanin"
                          },
                          {
                            "active": true,
                            "age": 24,
                            "birthday": "2001-07-15",
                            "first_name": "Nikolaj",
                            "id": 27641,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/27641/use_den_voksne_2025_split_1.png",
                            "last_name": "Meilby",
                            "modified_at": "2026-03-16T12:53:48Z",
                            "name": "DenVoksne",
                            "nationality": "DK",
                            "role": "adc",
                            "slug": "denvoksne"
                          },
                          {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-11-02",
                            "first_name": "Elton",
                            "id": 27664,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/27664/gl_twiizt_2025_split_2.png",
                            "last_name": "Richie Garcia Spetsig",
                            "modified_at": "2026-03-16T12:53:49Z",
                            "name": "Twiizt",
                            "nationality": "SE",
                            "role": "sup",
                            "slug": "twiizt"
                          },
                          {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-07-11",
                            "first_name": "Aslan",
                            "id": 39886,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/39886/use_white_2025_split_1.png",
                            "last_name": "Panglose",
                            "modified_at": "2026-03-16T12:53:49Z",
                            "name": "White",
                            "nationality": "FR",
                            "role": "jun",
                            "slug": "white-aslan-panglose"
                          },
                          {
                            "active": true,
                            "age": 22,
                            "birthday": "2003-10-29",
                            "first_name": "Felix",
                            "id": 48047,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/48047/use_fornoreason_2025_split_1.png",
                            "last_name": "Schummel",
                            "modified_at": "2026-03-16T12:53:49Z",
                            "name": "Fornoreason",
                            "nationality": "DE",
                            "role": "top",
                            "slug": "fornoreason"
                          }
                        ],
                        "team": {
                          "acronym": "USE",
                          "dark_mode_image_url": null,
                          "id": 126832,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/126832/220px_unicorns_of_lovelogo_square.png",
                          "location": "DE",
                          "modified_at": "2026-03-16T12:53:49Z",
                          "name": "Unicorns Of Love Sexy Edition",
                          "slug": "unicorns-of-love-sexy-edition"
                        }
                      },
                      {
                        "players": [
                          {
                            "active": true,
                            "age": 26,
                            "birthday": "2000-02-24",
                            "first_name": "Olivier",
                            "id": 20307,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/20307/ijc_prime_2025_split_2.png",
                            "last_name": "Payet",
                            "modified_at": "2026-03-16T12:53:47Z",
                            "name": "Prime",
                            "nationality": "FR",
                            "role": "sup",
                            "slug": "prime-olivier-payet"
                          },
                          {
                            "active": true,
                            "age": 20,
                            "birthday": "2006-02-14",
                            "first_name": "Johnny",
                            "id": 44018,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/44018/kcb_yukino_2025_split_2.png",
                            "last_name": "Dang",
                            "modified_at": "2026-03-16T12:53:47Z",
                            "name": "Yukino",
                            "nationality": "US",
                            "role": "jun",
                            "slug": "yukino"
                          },
                          {
                            "active": true,
                            "age": 20,
                            "birthday": "2005-07-20",
                            "first_name": "Kamil",
                            "id": 47104,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/47104/th_kamiloo_2025_split_3.png",
                            "last_name": "Haudegond",
                            "modified_at": "2026-03-16T12:53:46Z",
                            "name": "Kamiloo",
                            "nationality": "FR",
                            "role": "mid",
                            "slug": "kamiloo"
                          },
                          {
                            "active": true,
                            "age": 18,
                            "birthday": "2007-05-14",
                            "first_name": "Costin",
                            "id": 49298,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/49298/hazel.png",
                            "last_name": "Pestrițu",
                            "modified_at": "2026-03-16T12:53:45Z",
                            "name": "Hazel",
                            "nationality": "RO",
                            "role": "adc",
                            "slug": "hazel-costin-pestri-u"
                          },
                          {
                            "active": true,
                            "age": null,
                            "birthday": null,
                            "first_name": "Xu",
                            "id": 58131,
                            "image_url": null,
                            "last_name": "Hongtao Alessandro",
                            "modified_at": "2026-03-16T12:53:47Z",
                            "name": "Tao",
                            "nationality": "IT",
                            "role": "top",
                            "slug": "tao-xu-hongtao-alessandro"
                          }
                        ],
                        "team": {
                          "acronym": "KCB",
                          "dark_mode_image_url": null,
                          "id": 128268,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/128268/600px_karmine_corp_allmode.png",
                          "location": "FR",
                          "modified_at": "2026-03-16T12:53:47Z",
                          "name": "Karmine Corp Blue",
                          "slug": "karmine-corp"
                        }
                      },
                      {
                        "players": [
                          {
                            "active": true,
                            "age": 28,
                            "birthday": "1997-10-27",
                            "first_name": "Tristan",
                            "id": 62,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/62/eins_power_of_evil_2025_split_1.png",
                            "last_name": "Schrage",
                            "modified_at": "2026-03-16T12:53:42Z",
                            "name": "PowerOfEvil",
                            "nationality": "DE",
                            "role": "mid",
                            "slug": "powerofevil"
                          },
                          {
                            "active": true,
                            "age": 27,
                            "birthday": "1998-12-10",
                            "first_name": "Janik",
                            "id": 1372,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/1372/sk_jnx_2025_split_1.png",
                            "last_name": "Bartels",
                            "modified_at": "2026-03-16T12:53:41Z",
                            "name": "JNX",
                            "nationality": "DE",
                            "role": "top",
                            "slug": "jenax"
                          },
                          {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-10-13",
                            "first_name": "Tim",
                            "id": 21475,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/21475/bds.a_keduii_2024_split_1.png",
                            "last_name": "Willers",
                            "modified_at": "2026-03-16T12:53:42Z",
                            "name": "Keduii",
                            "nationality": "DE",
                            "role": "adc",
                            "slug": "keduii"
                          },
                          {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-12-17",
                            "first_name": "Daniel",
                            "id": 31671,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31671/use_seaz_2025_split_3.png",
                            "last_name": "Binderhofer",
                            "modified_at": "2026-03-16T12:53:42Z",
                            "name": "seaz",
                            "nationality": "AT",
                            "role": "sup",
                            "slug": "seaz"
                          },
                          {
                            "active": true,
                            "age": 22,
                            "birthday": "2004-02-14",
                            "first_name": "Isa Arda ",
                            "id": 45551,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/45551/ross_xagog_2025_split_1.png",
                            "last_name": "Dagli",
                            "modified_at": "2026-03-16T12:53:42Z",
                            "name": "Xagog",
                            "nationality": "DE",
                            "role": "jun",
                            "slug": "xagog"
                          }
                        ],
                        "team": {
                          "acronym": "ES",
                          "dark_mode_image_url": null,
                          "id": 130010,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/130010/eintracht_spandaulogo_square.png",
                          "location": "DE",
                          "modified_at": "2026-03-16T12:53:42Z",
                          "name": "Eintracht Spandau",
                          "slug": "eintracht-spandau"
                        }
                      },
                      {
                        "players": [
                          {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-12-16",
                            "first_name": "Mike",
                            "id": 28599,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/28599/bfr_furuy_2022_split_1.png",
                            "last_name": "Wils",
                            "modified_at": "2026-03-16T12:57:15Z",
                            "name": "Furuy",
                            "nationality": "NL",
                            "role": "mid",
                            "slug": "furuy"
                          },
                          {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-07-03",
                            "first_name": "Petr",
                            "id": 29143,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/29143/esb_bobista_2023_split_2.png",
                            "last_name": "Fojtík",
                            "modified_at": "2026-03-16T12:57:15Z",
                            "name": "bobista",
                            "nationality": "CZ",
                            "role": "top",
                            "slug": "bobiistaa"
                          },
                          {
                            "active": true,
                            "age": 24,
                            "birthday": "2001-12-16",
                            "first_name": "Kevin ",
                            "id": 31776,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31776/bdsa_mishi_2025_split_2.png",
                            "last_name": "Westerbacka",
                            "modified_at": "2026-03-16T12:57:16Z",
                            "name": "Mishi",
                            "nationality": "SE",
                            "role": "adc",
                            "slug": "mishigu"
                          },
                          {
                            "active": true,
                            "age": null,
                            "birthday": null,
                            "first_name": "Lovre",
                            "id": 42561,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/42561/dia_mafro_2022_split_2.png",
                            "last_name": "Čorić",
                            "modified_at": "2026-03-16T12:57:16Z",
                            "name": "Mafro",
                            "nationality": "HR",
                            "role": "jun",
                            "slug": "mafro"
                          },
                          {
                            "active": true,
                            "age": 20,
                            "birthday": "2005-09-10",
                            "first_name": "Guga",
                            "id": 61602,
                            "image_url": null,
                            "last_name": "Tsertsvadze",
                            "modified_at": "2026-03-16T12:57:16Z",
                            "name": "Guggu",
                            "nationality": "GE",
                            "role": "sup",
                            "slug": "guggu"
                          }
                        ],
                        "team": {
                          "acronym": "VDN",
                          "dark_mode_image_url": null,
                          "id": 130202,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/130202/verdantlogo_square.png",
                          "location": "GB",
                          "modified_at": "2026-03-16T12:57:16Z",
                          "name": "Verdant",
                          "slug": "verdant"
                        }
                      },
                      {
                        "players": [
                          {
                            "active": true,
                            "age": 22,
                            "birthday": "2003-05-16",
                            "first_name": "Shin",
                            "id": 38353,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/38353/hle.c_lure_2024_split_2.png",
                            "last_name": "Jae-yoon",
                            "modified_at": "2026-03-16T12:53:48Z",
                            "name": "Lure",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "lure"
                          },
                          {
                            "active": true,
                            "age": 20,
                            "birthday": "2005-06-05",
                            "first_name": "Cengizhan",
                            "id": 39000,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/39000/nsr_merciless_2021_split_1.png",
                            "last_name": "Teker",
                            "modified_at": "2026-03-16T12:53:48Z",
                            "name": "Mercy9",
                            "nationality": "TR",
                            "role": "mid",
                            "slug": "merciless"
                          },
                          {
                            "active": true,
                            "age": 20,
                            "birthday": "2005-10-23",
                            "first_name": "Kacper",
                            "id": 39132,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/39132/vit_daglas_2024_split_1.png",
                            "last_name": "Dagiel",
                            "modified_at": "2026-03-16T12:53:48Z",
                            "name": "Daglas",
                            "nationality": "PL",
                            "role": "jun",
                            "slug": "daglas"
                          },
                          {
                            "active": true,
                            "age": 23,
                            "birthday": "2003-03-01",
                            "first_name": "Baek",
                            "id": 45863,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/45863/ns_mihile_2024_split_2.png",
                            "last_name": "Sang-hwi",
                            "modified_at": "2026-03-16T12:53:48Z",
                            "name": "Mihile",
                            "nationality": "KR",
                            "role": "top",
                            "slug": "mihile"
                          },
                          {
                            "active": true,
                            "age": 20,
                            "birthday": "2005-07-27",
                            "first_name": "Batu",
                            "id": 52354,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/52354/ezgif_613bdb4b2eb2253d.png",
                            "last_name": "Kaygusuz",
                            "modified_at": "2026-03-16T12:53:47Z",
                            "name": "Batuuu",
                            "nationality": "TR",
                            "role": "sup",
                            "slug": "batuuu"
                          }
                        ],
                        "team": {
                          "acronym": "HRTS",
                          "dark_mode_image_url": null,
                          "id": 132212,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/132212/team_hereticslogo_square.png",
                          "location": "ES",
                          "modified_at": "2026-03-16T12:53:48Z",
                          "name": "Team Heretics Academy",
                          "slug": "team-heretics-academy"
                        }
                      },
                      {
                        "players": [
                          {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-12-19",
                            "first_name": "Onurcan",
                            "id": 15358,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/15358/gl_ragner_2025_split_2.png",
                            "last_name": "Aslan",
                            "modified_at": "2026-03-16T12:57:12Z",
                            "name": "Ragner",
                            "nationality": "TR",
                            "role": "top",
                            "slug": "ragner"
                          },
                          {
                            "active": true,
                            "age": 22,
                            "birthday": "2003-09-09",
                            "first_name": "Jeong-hyeon",
                            "id": 32745,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/32745/kt.c_hype_2024_split_2.png",
                            "last_name": "Byeon ",
                            "modified_at": "2026-03-16T12:57:12Z",
                            "name": "Hype",
                            "nationality": "KR",
                            "role": "adc",
                            "slug": "kingkong"
                          },
                          {
                            "active": true,
                            "age": 21,
                            "birthday": "2004-08-12",
                            "first_name": "Doğukan",
                            "id": 34917,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/34917/kcb_113_summer_2024.png",
                            "last_name": "Balci",
                            "modified_at": "2026-03-16T12:57:12Z",
                            "name": "113",
                            "nationality": "TR",
                            "role": "jun",
                            "slug": "player-113"
                          },
                          {
                            "active": true,
                            "age": 21,
                            "birthday": "2004-03-20",
                            "first_name": "Seo",
                            "id": 34985,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/34985/kcb_slow_q_2025_split_2.png",
                            "last_name": "Ye-bit",
                            "modified_at": "2026-03-16T12:57:12Z",
                            "name": "SlowQ",
                            "nationality": "KR",
                            "role": "mid",
                            "slug": "slowq"
                          },
                          {
                            "active": true,
                            "age": 24,
                            "birthday": "2001-07-13",
                            "first_name": "Paul ",
                            "id": 38918,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/38918/th_stend_2025_split_3.png",
                            "last_name": "Lardin",
                            "modified_at": "2026-03-16T12:57:13Z",
                            "name": "Stend",
                            "nationality": "FR",
                            "role": "sup",
                            "slug": "stend"
                          }
                        ],
                        "team": {
                          "acronym": "ME",
                          "dark_mode_image_url": null,
                          "id": 133984,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/133984/misa_esportslogo_profile.png",
                          "location": "TR",
                          "modified_at": "2026-03-16T12:57:13Z",
                          "name": "Misa Esports",
                          "slug": "misa-esports"
                        }
                      },
                      {
                        "players": [
                          {
                            "active": true,
                            "age": 22,
                            "birthday": "2003-07-02",
                            "first_name": "Šimon",
                            "id": 28947,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/28947/bkr_omon_2025_split_2.png",
                            "last_name": "Říháček",
                            "modified_at": "2026-03-16T12:53:43Z",
                            "name": "OMON",
                            "nationality": "CZ",
                            "role": "mid",
                            "slug": "cgg-omon"
                          },
                          {
                            "active": true,
                            "age": 20,
                            "birthday": "2005-04-18",
                            "first_name": "Franciszek",
                            "id": 31740,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/31740/z10_harpoon_2024_split_1.png",
                            "last_name": "Gryszkiewicz",
                            "modified_at": "2026-03-16T12:53:43Z",
                            "name": "Harpoon",
                            "nationality": "PL",
                            "role": "adc",
                            "slug": "harpoon"
                          },
                          {
                            "active": true,
                            "age": 20,
                            "birthday": "2005-12-15",
                            "first_name": "Carl",
                            "id": 39177,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/39177/th_carlsen_2025_split_3.png",
                            "last_name": "Carlsen",
                            "modified_at": "2026-03-16T12:53:42Z",
                            "name": "Carlsen",
                            "nationality": "DK",
                            "role": "top",
                            "slug": "carlsen"
                          },
                          {
                            "active": true,
                            "age": 22,
                            "birthday": "2003-05-16",
                            "first_name": "Théo",
                            "id": 39882,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/39882/gl_zoelys_2025_split_2.png",
                            "last_name": "Le Scornec",
                            "modified_at": "2026-03-16T12:53:43Z",
                            "name": "Zoelys",
                            "nationality": "FR",
                            "role": "sup",
                            "slug": "zoelys"
                          },
                          {
                            "active": true,
                            "age": 24,
                            "birthday": "2002-01-27",
                            "first_name": "Francisco ",
                            "id": 42925,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/42925/bar_thayger_2024_split_2.png",
                            "last_name": "Mazo",
                            "modified_at": "2026-03-16T12:53:43Z",
                            "name": "Thayger",
                            "nationality": "ES",
                            "role": "jun",
                            "slug": "thayger"
                          }
                        ],
                        "team": {
                          "acronym": "GAL",
                          "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/136019/galions_darkmode.png",
                          "id": 136019,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/136019/galionslogo_square.png",
                          "location": "FR",
                          "modified_at": "2026-03-16T12:53:43Z",
                          "name": "Galions",
                          "slug": "galions"
                        }
                      },
                      {
                        "players": [
                          {
                            "active": true,
                            "age": 27,
                            "birthday": "1998-11-05",
                            "first_name": "Lucas",
                            "id": 1304,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/1304/kc_saken_2024_split_1.png",
                            "last_name": "Fayard",
                            "modified_at": "2026-03-16T12:53:40Z",
                            "name": "Saken",
                            "nationality": "FR",
                            "role": "mid",
                            "slug": "saken"
                          },
                          {
                            "active": true,
                            "age": 25,
                            "birthday": "2000-06-30",
                            "first_name": "Raphael",
                            "id": 1639,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/1639/kc_targamas_2025_split_3.png",
                            "last_name": "Crabbe",
                            "modified_at": "2026-03-16T12:53:40Z",
                            "name": "Targamas",
                            "nationality": "BE",
                            "role": "sup",
                            "slug": "targamas"
                          },
                          {
                            "active": true,
                            "age": 22,
                            "birthday": "2003-09-28",
                            "first_name": "Thomas",
                            "id": 29458,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/29458/kcb_3_xa_2025_split_2.png",
                            "last_name": "Foucou",
                            "modified_at": "2026-03-16T12:53:39Z",
                            "name": "3XA",
                            "nationality": "FR",
                            "role": "adc",
                            "slug": "ldlc-exakick"
                          },
                          {
                            "active": true,
                            "age": 24,
                            "birthday": "2001-12-30",
                            "first_name": "Adam",
                            "id": 32021,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/32021/bds_adam_2024_split_1.png",
                            "last_name": "Maanane",
                            "modified_at": "2026-03-16T12:53:40Z",
                            "name": "Adam",
                            "nationality": "FR",
                            "role": "top",
                            "slug": "kc-adam"
                          },
                          {
                            "active": true,
                            "age": null,
                            "birthday": null,
                            "first_name": "Isak",
                            "id": 52566,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/52566/rs_natty_natt_2025_split_2_2.png",
                            "last_name": "Elgh",
                            "modified_at": "2026-03-16T12:53:40Z",
                            "name": "NattyNatt",
                            "nationality": "SE",
                            "role": "jun",
                            "slug": "nattynatt"
                          }
                        ],
                        "team": {
                          "acronym": "FF",
                          "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/137661/533px_french_flair_darkmode.png",
                          "id": 137661,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/137661/533px_french_flair_lightmode.png",
                          "location": "FR",
                          "modified_at": "2026-03-16T12:53:40Z",
                          "name": "French Flair",
                          "slug": "french-flair"
                        }
                      },
                      {
                        "players": [
                          {
                            "active": true,
                            "age": null,
                            "birthday": null,
                            "first_name": "Luchao",
                            "id": 23486,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/23486/lnga_rin_2021_split_1.png",
                            "last_name": "Wang",
                            "modified_at": "2026-03-16T12:53:40Z",
                            "name": "Rin",
                            "nationality": "CN",
                            "role": "adc",
                            "slug": "rin"
                          },
                          {
                            "active": true,
                            "age": 23,
                            "birthday": "2002-06-28",
                            "first_name": "Mark",
                            "id": 24431,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/24431/sly_markoon_2025_split_2.png",
                            "last_name": "van Woensel",
                            "modified_at": "2026-03-16T12:53:40Z",
                            "name": "Markoon",
                            "nationality": "NL",
                            "role": "jun",
                            "slug": "markoon"
                          },
                          {
                            "active": true,
                            "age": 20,
                            "birthday": "2006-01-19",
                            "first_name": "Alex",
                            "id": 40760,
                            "image_url": null,
                            "last_name": "Chea",
                            "modified_at": "2026-03-16T12:53:41Z",
                            "name": "Toasty",
                            "nationality": "US",
                            "role": "mid",
                            "slug": "toasty"
                          },
                          {
                            "active": true,
                            "age": 19,
                            "birthday": "2006-10-02",
                            "first_name": "Francesco",
                            "id": 49167,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/49167/big_shelfmade_2025_split_1.png",
                            "last_name": "Cardia",
                            "modified_at": "2026-03-16T12:53:40Z",
                            "name": "Shelfmade",
                            "nationality": "DE",
                            "role": "top",
                            "slug": "shelfmade"
                          },
                          {
                            "active": true,
                            "age": 24,
                            "birthday": "2002-02-22",
                            "first_name": "Timo",
                            "id": 56582,
                            "image_url": "https://cdn-api.pandascore.co/images/player/image/56582/ezgif_367b9c54a412c7.png",
                            "last_name": "Bock",
                            "modified_at": "2026-03-16T12:53:41Z",
                            "name": "Tockimo",
                            "nationality": "DE",
                            "role": "sup",
                            "slug": "tockimo"
                          }
                        ],
                        "team": {
                          "acronym": "G2N",
                          "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/137945/603px_g2_nord_darkmode.png",
                          "id": 137945,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/137945/603px_g2_nord_lightmode.png",
                          "location": "DE",
                          "modified_at": "2026-03-16T12:53:41Z",
                          "name": "G2 NORD",
                          "slug": "g2-nord"
                        }
                      }
                    ],
                    "has_bracket": true,
                    "id": 20412,
                    "league": {
                      "id": 4996,
                      "image_url": "https://cdn-api.pandascore.co/images/league/image/4996/emea_masters_2023-png",
                      "modified_at": "2023-04-01T08:10:00Z",
                      "name": "EMEA Masters",
                      "slug": "league-of-legends-emea-masters",
                      "url": null
                    },
                    "league_id": 4996,
                    "live_supported": false,
                    "matches": [
                      {
                        "begin_at": "2026-03-23T16:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397490,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-16T12:54:33Z",
                        "name": "Upper bracket round 1 match 1: FF vs G2N",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-23T16:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-23T16:00:00Z",
                        "slug": "2026-03-23-56ec8f55-8508-45ee-b8b6-b57756cde276",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-23T16:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397493,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-16T14:01:10Z",
                        "name": "Upper bracket round 1 match 4: HRTS vs USE",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-23T19:00:00Z",
                        "rescheduled": true,
                        "scheduled_at": "2026-03-23T16:00:00Z",
                        "slug": "2026-03-23-a8397960-9e8e-4adf-8be8-956060692136",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-23T19:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397491,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-16T14:00:54Z",
                        "name": "Upper bracket round 1 match 2: ES vs GAL",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-23T16:00:00Z",
                        "rescheduled": true,
                        "scheduled_at": "2026-03-23T19:00:00Z",
                        "slug": "2026-03-23-896019cc-e4be-4511-a6ee-3d55c4c3ea82",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-23T19:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397492,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-16T12:54:59Z",
                        "name": "Upper bracket round 1 match 3: BIG vs KCB",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-23T19:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-23T19:00:00Z",
                        "slug": "2026-03-23-a7622de1-4a89-4841-b73b-b21a97af52a8",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-24T16:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397494,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-16T12:58:43Z",
                        "name": "Upper bracket quarterfinal 1: ME vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-24T16:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-24T16:00:00Z",
                        "slug": "2026-03-24-d4c55bde-424e-4a11-a97e-a2d13c7d3aa2",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-24T16:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397495,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-16T12:58:54Z",
                        "name": "Upper bracket quarterfinal 2: KOI.F vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-24T16:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-24T16:00:00Z",
                        "slug": "2026-03-24-6f56fab3-24b3-468c-b5e3-28bade4cb5d0",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-24T19:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397496,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-16T12:59:05Z",
                        "name": "Upper bracket quarterfinal 3: SLY vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-24T19:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-24T19:00:00Z",
                        "slug": "2026-03-24-bf918605-f92e-4567-9a75-29587d192579",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-24T19:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397497,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-16T12:59:13Z",
                        "name": "Upper bracket quarterfinal 4: VDN vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-24T19:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-24T19:00:00Z",
                        "slug": "2026-03-24-11c54e1a-3787-49e6-a9d9-580c5b5249f1",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-25T16:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397498,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Lower bracket round 1 match 1: TBD vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-25T16:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-25T16:00:00Z",
                        "slug": "2026-03-25-c85cc7c0-4ec4-4c19-96f9-dea8610bf17e",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-25T16:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397499,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Lower bracket round 1 match 2: TBD vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-25T16:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-25T16:00:00Z",
                        "slug": "2026-03-25-3605a63f-2ab3-4389-8566-3430b4ecfeb5",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-25T19:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397500,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Lower bracket round 1 match 3: TBD vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-25T19:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-25T19:00:00Z",
                        "slug": "2026-03-25-2d438083-3a36-420d-8f43-59c69554ebb6",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-25T19:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397501,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Lower bracket round 1 match 4: TBD vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-25T19:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-25T19:00:00Z",
                        "slug": "2026-03-25-bf6238be-1114-4b0b-af3b-bce1e08ab66a",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-25T19:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397504,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Upper bracket semifinal 1: TBD vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-25T19:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-25T19:00:00Z",
                        "slug": "2026-03-25-27f693b5-7622-4fba-b796-193192a0e1e7",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-25T19:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397505,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Upper bracket semifinal 2: TBD vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-25T19:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-25T19:00:00Z",
                        "slug": "2026-03-25-8606652d-f413-499f-817b-501e7d0b93c4",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-31T15:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397502,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Lower bracket round 2 match 1: TBD vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-31T15:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-31T15:00:00Z",
                        "slug": "2026-03-31-8c28a508-9180-412b-8332-826328268955",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-31T15:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397509,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Upper bracket final: TBD vs TBD",
                        "number_of_games": 5,
                        "original_scheduled_at": "2026-03-31T15:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-31T15:00:00Z",
                        "slug": "2026-03-31-fdc24d44-7faf-4ac2-a3fb-c3b8992d151d",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-31T18:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397503,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Lower bracket round 2 match 2: TBD vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-03-31T18:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-03-31T18:00:00Z",
                        "slug": "2026-03-31-5eca759a-c645-4dc1-affa-081e591f5bb8",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-04-07T15:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397506,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Lower bracket quarterfinal 1: TBD vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-04-07T15:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-04-07T15:00:00Z",
                        "slug": "2026-04-07",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-04-07T15:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397507,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Lower bracket quarterfinal 2: TBD vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-04-07T15:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-04-07T15:00:00Z",
                        "slug": "2026-04-07-bdd64649-b7cf-49da-8cc6-0d043409231e",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-04-07T18:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397508,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Lower bracket semifinal: TBD vs TBD",
                        "number_of_games": 3,
                        "original_scheduled_at": "2026-04-07T18:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-04-07T18:00:00Z",
                        "slug": "2026-04-07-c2c88aa5-f614-424d-afa0-7b640f533011",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-04-14T15:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397510,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Lower bracket final: TBD vs TBD",
                        "number_of_games": 5,
                        "original_scheduled_at": "2026-04-14T15:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-04-14T15:00:00Z",
                        "slug": "2026-04-14",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-04-21T15:00:00Z",
                        "detailed_stats": true,
                        "draw": false,
                        "end_at": null,
                        "forfeit": false,
                        "game_advantage": null,
                        "id": 1397511,
                        "live": {
                          "opens_at": null,
                          "supported": false,
                          "url": null
                        },
                        "match_type": "best_of",
                        "modified_at": "2026-03-14T07:42:47Z",
                        "name": "Grand final: TBD vs TBD",
                        "number_of_games": 5,
                        "original_scheduled_at": "2026-04-21T15:00:00Z",
                        "rescheduled": false,
                        "scheduled_at": "2026-04-21T15:00:00Z",
                        "slug": "2026-04-21-54487152-11cf-4404-a38c-5d6e1b4772d6",
                        "status": "not_started",
                        "streams_list": [],
                        "tournament_id": 20412,
                        "winner_id": null,
                        "winner_type": "Team"
                      }
                    ],
                    "modified_at": "2026-03-16T14:16:20Z",
                    "name": "Playoffs",
                    "prizepool": null,
                    "region": "WEU",
                    "serie": {
                      "begin_at": "2026-03-09T16:00:00Z",
                      "end_at": "2026-04-21T22:00:00Z",
                      "full_name": "Winter 2026",
                      "id": 10306,
                      "league_id": 4996,
                      "modified_at": "2026-03-13T22:38:21Z",
                      "name": "",
                      "season": "Winter",
                      "slug": "league-of-legends-emea-masters-winter-2026",
                      "winner_id": null,
                      "winner_type": "Team",
                      "year": 2026
                    },
                    "serie_id": 10306,
                    "slug": "league-of-legends-emea-masters-winter-2026-playoffs",
                    "teams": [
                      {
                        "acronym": "KOI.F",
                        "dark_mode_image_url": null,
                        "id": 363,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/363/movistar_ko_ilogo_square.png",
                        "location": "ES",
                        "modified_at": "2026-03-16T12:57:15Z",
                        "name": "⁠Movistar KOI Fénix",
                        "slug": "movistar-riders"
                      },
                      {
                        "acronym": "SLY",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/1449/solary_darkmode.png",
                        "id": 1449,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/1449/123px_solarylogo_square.png",
                        "location": "FR",
                        "modified_at": "2026-03-16T12:57:17Z",
                        "name": "Solary",
                        "slug": "solary"
                      },
                      {
                        "acronym": "BIG",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/125905/122px_big_2020_darkmode.png",
                        "id": 125905,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/125905/berlin_international_gaminglogo_square.png",
                        "location": "DE",
                        "modified_at": "2026-03-16T12:53:45Z",
                        "name": "BIG",
                        "slug": "big-league-of-legends"
                      },
                      {
                        "acronym": "USE",
                        "dark_mode_image_url": null,
                        "id": 126832,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/126832/220px_unicorns_of_lovelogo_square.png",
                        "location": "DE",
                        "modified_at": "2026-03-16T12:53:49Z",
                        "name": "Unicorns Of Love Sexy Edition",
                        "slug": "unicorns-of-love-sexy-edition"
                      },
                      {
                        "acronym": "KCB",
                        "dark_mode_image_url": null,
                        "id": 128268,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/128268/600px_karmine_corp_allmode.png",
                        "location": "FR",
                        "modified_at": "2026-03-16T12:53:47Z",
                        "name": "Karmine Corp Blue",
                        "slug": "karmine-corp"
                      },
                      {
                        "acronym": "ES",
                        "dark_mode_image_url": null,
                        "id": 130010,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/130010/eintracht_spandaulogo_square.png",
                        "location": "DE",
                        "modified_at": "2026-03-16T12:53:42Z",
                        "name": "Eintracht Spandau",
                        "slug": "eintracht-spandau"
                      },
                      {
                        "acronym": "VDN",
                        "dark_mode_image_url": null,
                        "id": 130202,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/130202/verdantlogo_square.png",
                        "location": "GB",
                        "modified_at": "2026-03-16T12:57:16Z",
                        "name": "Verdant",
                        "slug": "verdant"
                      },
                      {
                        "acronym": "HRTS",
                        "dark_mode_image_url": null,
                        "id": 132212,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/132212/team_hereticslogo_square.png",
                        "location": "ES",
                        "modified_at": "2026-03-16T12:53:48Z",
                        "name": "Team Heretics Academy",
                        "slug": "team-heretics-academy"
                      },
                      {
                        "acronym": "ME",
                        "dark_mode_image_url": null,
                        "id": 133984,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/133984/misa_esportslogo_profile.png",
                        "location": "TR",
                        "modified_at": "2026-03-16T12:57:13Z",
                        "name": "Misa Esports",
                        "slug": "misa-esports"
                      },
                      {
                        "acronym": "GAL",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/136019/galions_darkmode.png",
                        "id": 136019,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/136019/galionslogo_square.png",
                        "location": "FR",
                        "modified_at": "2026-03-16T12:53:43Z",
                        "name": "Galions",
                        "slug": "galions"
                      },
                      {
                        "acronym": "FF",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/137661/533px_french_flair_darkmode.png",
                        "id": 137661,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/137661/533px_french_flair_lightmode.png",
                        "location": "FR",
                        "modified_at": "2026-03-16T12:53:40Z",
                        "name": "French Flair",
                        "slug": "french-flair"
                      },
                      {
                        "acronym": "G2N",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/137945/603px_g2_nord_darkmode.png",
                        "id": 137945,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/137945/603px_g2_nord_lightmode.png",
                        "location": "DE",
                        "modified_at": "2026-03-16T12:53:41Z",
                        "name": "G2 NORD",
                        "slug": "g2-nord"
                      }
                    ],
                    "tier": "b",
                    "type": "online",
                    "videogame": {
                      "id": 1,
                      "name": "LoL",
                      "slug": "league-of-legends"
                    },
                    "videogame_title": null,
                    "winner_id": null,
                    "winner_type": "Team"
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLShortTournaments"
            }
          }
        },
        "description": "A list of League-of-Legends tournaments"
      }
    },
    "schemas": {
      "LoLShortTournaments": {
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
          "title": "ShortTournament",
          "type": "object"
        },
        "title": "LoLShortTournaments",
        "type": "array"
      },
      "filter_over_LoLShortTournaments": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "begin_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "TournamentBeginAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "country": {
            "items": {
              "description": "Country code matching the location of the tournament according to the ISO 3166-1 standard (Alpha-2 code). In addition to the standard, the XK code is used for Kosovo. null if unknown",
              "title": "TournamentCountry",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "detailed_stats": {
            "description": "Whether the tournament is expected to have detailed statistics available",
            "title": "TournamentDetailedStats",
            "type": "boolean"
          },
          "end_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "TournamentEndAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "has_bracket": {
            "description": "Whether the tournament has a bracket",
            "title": "TournamentHasBracket",
            "type": "boolean"
          },
          "id": {
            "items": {
              "minimum": 1,
              "title": "TournamentID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "live_supported": {
            "description": "Whether live is supported",
            "title": "TournamentLiveSupported",
            "type": "boolean"
          },
          "modified_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "TournamentModifiedAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "TournamentName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "prizepool": {
            "items": {
              "title": "TournamentPrizepool",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "region": {
            "items": {
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
              "title": "TournamentRegion",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "serie_id": {
            "items": {
              "minimum": 1,
              "title": "SerieID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "slug": {
            "items": {
              "minLength": 1,
              "pattern": "^[a-z0-9_-]+$",
              "title": "TournamentSlug",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "tier": {
            "items": {
              "description": "The tier of the tournament, ranging from 'S' to 'Unranked'. Ranking 'S' > 'A' > 'B' > 'C' > 'D' > 'Unranked'",
              "enum": [
                "a",
                "b",
                "c",
                "d",
                "s",
                "unranked"
              ],
              "title": "TournamentTier",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "videogame_title": {
            "description": "A videogame title id or slug.\nOnly for `/csgo/*`, `/codmw/*`, `/fifa/*` and `/ow/*` endpoints\n",
            "items": {
              "oneOf": [
                {
                  "minimum": 1,
                  "title": "VideogameTitleID",
                  "type": "integer"
                },
                {
                  "minLength": 1,
                  "pattern": "^[a-z0-9_-]+$",
                  "title": "VideogameTitleSlug",
                  "type": "string"
                }
              ]
            },
            "minItems": 1,
            "type": "array"
          },
          "winner_id": {
            "items": {
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
              "title": "OpponentID"
            },
            "minItems": 1,
            "type": "array"
          },
          "winner_type": {
            "items": {
              "enum": [
                "Player",
                "Team"
              ],
              "title": "OpponentType",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          }
        },
        "type": "object"
      },
      "range_over_LoLShortTournaments": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "begin_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "TournamentBeginAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "country": {
            "items": {
              "description": "Country code matching the location of the tournament according to the ISO 3166-1 standard (Alpha-2 code). In addition to the standard, the XK code is used for Kosovo. null if unknown",
              "title": "TournamentCountry",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "detailed_stats": {
            "items": {
              "description": "Whether the tournament is expected to have detailed statistics available",
              "title": "TournamentDetailedStats",
              "type": "boolean"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "end_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "TournamentEndAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "has_bracket": {
            "items": {
              "description": "Whether the tournament has a bracket",
              "title": "TournamentHasBracket",
              "type": "boolean"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "id": {
            "items": {
              "minimum": 1,
              "title": "TournamentID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "modified_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "TournamentModifiedAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "TournamentName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "prizepool": {
            "items": {
              "title": "TournamentPrizepool",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "region": {
            "items": {
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
              "title": "TournamentRegion",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "serie_id": {
            "items": {
              "minimum": 1,
              "title": "SerieID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "slug": {
            "items": {
              "minLength": 1,
              "pattern": "^[a-z0-9_-]+$",
              "title": "TournamentSlug",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "tier": {
            "items": {
              "description": "The tier of the tournament, ranging from 'S' to 'Unranked'. Ranking 'S' > 'A' > 'B' > 'C' > 'D' > 'Unranked'",
              "enum": [
                "a",
                "b",
                "c",
                "d",
                "s",
                "unranked"
              ],
              "title": "TournamentTier",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "winner_id": {
            "items": {
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
              "title": "OpponentID"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "winner_type": {
            "items": {
              "enum": [
                "Player",
                "Team"
              ],
              "title": "OpponentType",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          }
        },
        "type": "object"
      },
      "search_over_LoLShortTournaments": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "country": {
            "description": "Country code matching the location of the tournament according to the ISO 3166-1 standard (Alpha-2 code). In addition to the standard, the XK code is used for Kosovo. null if unknown",
            "title": "TournamentCountry",
            "type": "string"
          },
          "name": {
            "title": "TournamentName",
            "type": "string"
          },
          "prizepool": {
            "title": "TournamentPrizepool",
            "type": "string"
          },
          "region": {
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
            "title": "TournamentRegion",
            "type": "string"
          },
          "slug": {
            "minLength": 1,
            "pattern": "^[a-z0-9_-]+$",
            "title": "TournamentSlug",
            "type": "string"
          },
          "tier": {
            "description": "The tier of the tournament, ranging from 'S' to 'Unranked'. Ranking 'S' > 'A' > 'B' > 'C' > 'D' > 'Unranked'",
            "enum": [
              "a",
              "b",
              "c",
              "d",
              "s",
              "unranked"
            ],
            "title": "TournamentTier",
            "type": "string"
          },
          "winner_type": {
            "enum": [
              "Player",
              "Team"
            ],
            "title": "OpponentType",
            "type": "string"
          }
        },
        "type": "object"
      },
      "sort_over_LoLShortTournaments": {
        "items": {
          "enum": [
            "begin_at",
            "-begin_at",
            "country",
            "-country",
            "detailed_stats",
            "-detailed_stats",
            "end_at",
            "-end_at",
            "has_bracket",
            "-has_bracket",
            "id",
            "-id",
            "modified_at",
            "-modified_at",
            "name",
            "-name",
            "prizepool",
            "-prizepool",
            "region",
            "-region",
            "serie_id",
            "-serie_id",
            "slug",
            "-slug",
            "tier",
            "-tier",
            "winner_id",
            "-winner_id",
            "winner_type",
            "-winner_type"
          ]
        },
        "minItems": 1,
        "type": "array"
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
    "/lol/tournaments/past": {
      "get": {
        "description": "List past League of Legends tournaments\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_tournaments_past",
        "parameters": [
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLShortTournaments"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to select results within ranges\nFor more information on ranges, see [docs](/docs/filtering-and-sorting#range).",
            "explode": true,
            "in": "query",
            "name": "range",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/range_over_LoLShortTournaments"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLShortTournaments"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLShortTournaments"
            },
            "style": "deepObject"
          },
          {
            "$ref": "#/components/parameters/Page"
          },
          {
            "$ref": "#/components/parameters/PerPage"
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLShortTournaments"
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
        "summary": "Get past LoL tournaments",
        "tags": [
          "LoL tournaments"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/tournaments/past' \\\n     --header 'accept: application/json'\n",
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