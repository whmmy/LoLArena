> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List rune paths

List the latest version of League of Legends (reforged) rune paths
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
      "LoLRunePaths": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/runes-reforged-paths": {
                "description": "/lol/runes-reforged-paths",
                "value": [
                  {
                    "id": 5,
                    "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                    "name": "Sorcery",
                    "runes": {
                      "keystones": [
                        54,
                        53,
                        52
                      ],
                      "slot1": [
                        57,
                        56,
                        55
                      ],
                      "slot2": [
                        60,
                        59,
                        58
                      ],
                      "slot3": [
                        63,
                        62,
                        61
                      ]
                    },
                    "videogame_versions": [
                      "14.10.1",
                      "14.9.1",
                      "14.8.1",
                      "14.7.1",
                      "14.6.1",
                      "14.5.1",
                      "14.4.1",
                      "14.3.1",
                      "14.2.1",
                      "14.1.1",
                      "13.24.1",
                      "13.23.1",
                      "13.22.1",
                      "13.21.1",
                      "13.19.1",
                      "13.18.1",
                      "13.17.1",
                      "13.16.1",
                      "13.15.1",
                      "13.14.1",
                      "13.13.1",
                      "13.12.1",
                      "13.11.1",
                      "13.10.1",
                      "13.9.1",
                      "13.8.1",
                      "13.7.1",
                      "13.6.1",
                      "13.5.1",
                      "13.4.1",
                      "13.3.1",
                      "13.1.1",
                      "12.23.1",
                      "12.22.1",
                      "12.21.1",
                      "12.20.1",
                      "12.19.1",
                      "12.18.1",
                      "12.17.1",
                      "12.16.1",
                      "12.15.1",
                      "12.14.1",
                      "12.13.1",
                      "12.12.1",
                      "12.11.1",
                      "12.10.1",
                      "12.9.1",
                      "12.8.1",
                      "12.7.1",
                      "12.6.1",
                      "12.5.1",
                      "12.4.1",
                      "12.3.1",
                      "12.2.1",
                      "12.1.1",
                      "11.24.1",
                      "11.23.1",
                      "11.22.1",
                      "11.21.1",
                      "11.20.1",
                      "11.19.1",
                      "11.18.1",
                      "11.17.1",
                      "11.16.1",
                      "11.15.1",
                      "11.14.1",
                      "11.13.1",
                      "11.12.1",
                      "11.11.1",
                      "11.10.1",
                      "11.9.1",
                      "11.8.1",
                      "11.7.1",
                      "11.6.1",
                      "11.5.1",
                      "11.4.1",
                      "11.3.1",
                      "11.2.1",
                      "11.1.1",
                      "10.25.1",
                      "10.24.1",
                      "10.23.1",
                      "10.22.1",
                      "10.21.1",
                      "10.20.1",
                      "10.19.1",
                      "10.10.3216176",
                      "10.10.3208608",
                      "9.9.1"
                    ]
                  },
                  {
                    "id": 4,
                    "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                    "name": "Resolve",
                    "runes": {
                      "keystones": [
                        40,
                        41,
                        42
                      ],
                      "slot1": [
                        43,
                        44,
                        45
                      ],
                      "slot2": [
                        48,
                        46,
                        47
                      ],
                      "slot3": [
                        51,
                        50,
                        49
                      ]
                    },
                    "videogame_versions": [
                      "14.10.1",
                      "14.9.1",
                      "14.8.1",
                      "14.7.1",
                      "14.6.1",
                      "14.5.1",
                      "14.4.1",
                      "14.3.1",
                      "14.2.1",
                      "14.1.1",
                      "13.24.1",
                      "13.23.1",
                      "13.22.1",
                      "13.21.1",
                      "13.19.1",
                      "13.18.1",
                      "13.17.1",
                      "13.16.1",
                      "13.15.1",
                      "13.14.1",
                      "13.13.1",
                      "13.12.1",
                      "13.11.1",
                      "13.10.1",
                      "13.9.1",
                      "13.8.1",
                      "13.7.1",
                      "13.6.1",
                      "13.5.1",
                      "13.4.1",
                      "13.3.1",
                      "13.1.1",
                      "12.23.1",
                      "12.22.1",
                      "12.21.1",
                      "12.20.1",
                      "12.19.1",
                      "12.18.1",
                      "12.17.1",
                      "12.16.1",
                      "12.15.1",
                      "12.14.1",
                      "12.13.1",
                      "12.12.1",
                      "12.11.1",
                      "12.10.1",
                      "12.9.1",
                      "12.8.1",
                      "12.7.1",
                      "12.6.1",
                      "12.5.1",
                      "12.4.1",
                      "12.3.1",
                      "12.2.1",
                      "12.1.1",
                      "11.24.1",
                      "11.23.1",
                      "11.22.1",
                      "11.21.1",
                      "11.20.1",
                      "11.19.1",
                      "11.18.1",
                      "11.17.1",
                      "11.16.1",
                      "11.15.1",
                      "11.14.1",
                      "11.13.1",
                      "11.12.1",
                      "11.11.1",
                      "11.10.1",
                      "11.9.1",
                      "11.8.1",
                      "11.7.1",
                      "11.6.1",
                      "11.5.1",
                      "11.4.1",
                      "11.3.1",
                      "11.2.1",
                      "11.1.1",
                      "10.25.1",
                      "10.24.1",
                      "10.23.1",
                      "10.22.1",
                      "10.21.1",
                      "10.20.1",
                      "10.19.1",
                      "10.10.3216176",
                      "10.10.3208608",
                      "9.9.1"
                    ]
                  },
                  {
                    "id": 3,
                    "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                    "name": "Precision",
                    "runes": {
                      "keystones": [
                        30,
                        29,
                        28,
                        27
                      ],
                      "slot1": [
                        31,
                        33,
                        32
                      ],
                      "slot2": [
                        36,
                        34,
                        35
                      ],
                      "slot3": [
                        39,
                        38,
                        37
                      ]
                    },
                    "videogame_versions": [
                      "14.10.1",
                      "14.9.1",
                      "14.8.1",
                      "14.7.1",
                      "14.6.1",
                      "14.5.1",
                      "14.4.1",
                      "14.3.1",
                      "14.2.1",
                      "14.1.1",
                      "13.24.1",
                      "13.23.1",
                      "13.22.1",
                      "13.21.1",
                      "13.19.1",
                      "13.18.1",
                      "13.17.1",
                      "13.16.1",
                      "13.15.1",
                      "13.14.1",
                      "13.13.1",
                      "13.12.1",
                      "13.11.1",
                      "13.10.1",
                      "13.9.1",
                      "13.8.1",
                      "13.7.1",
                      "13.6.1",
                      "13.5.1",
                      "13.4.1",
                      "13.3.1",
                      "13.1.1",
                      "12.23.1",
                      "12.22.1",
                      "12.21.1",
                      "12.20.1",
                      "12.19.1",
                      "12.18.1",
                      "12.17.1",
                      "12.16.1",
                      "12.15.1",
                      "12.14.1",
                      "12.13.1",
                      "12.12.1",
                      "12.11.1",
                      "12.10.1",
                      "12.9.1",
                      "12.8.1",
                      "12.7.1",
                      "12.6.1",
                      "12.5.1",
                      "12.4.1",
                      "12.3.1",
                      "12.2.1",
                      "12.1.1",
                      "11.24.1",
                      "11.23.1",
                      "11.22.1",
                      "11.21.1",
                      "11.20.1",
                      "11.19.1",
                      "11.18.1",
                      "11.17.1",
                      "11.16.1",
                      "11.15.1",
                      "11.14.1",
                      "11.13.1",
                      "11.12.1",
                      "11.11.1",
                      "11.10.1",
                      "11.9.1",
                      "11.8.1",
                      "11.7.1",
                      "11.6.1",
                      "11.5.1",
                      "11.4.1",
                      "11.3.1",
                      "11.2.1",
                      "11.1.1",
                      "10.25.1",
                      "10.24.1",
                      "10.23.1",
                      "10.22.1",
                      "10.21.1",
                      "10.20.1",
                      "10.19.1",
                      "10.10.3216176",
                      "10.10.3208608",
                      "9.9.1"
                    ]
                  },
                  {
                    "id": 2,
                    "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                    "name": "Inspiration",
                    "runes": {
                      "keystones": [
                        15,
                        64,
                        65,
                        17,
                        16
                      ],
                      "slot1": [
                        20,
                        75,
                        19,
                        18
                      ],
                      "slot2": [
                        76,
                        77,
                        23,
                        22,
                        21
                      ],
                      "slot3": [
                        26,
                        25,
                        78,
                        24
                      ]
                    },
                    "videogame_versions": [
                      "14.10.1",
                      "14.9.1",
                      "14.8.1",
                      "14.7.1",
                      "14.6.1",
                      "14.5.1",
                      "14.4.1",
                      "14.3.1",
                      "14.2.1",
                      "14.1.1",
                      "13.24.1",
                      "13.23.1",
                      "13.22.1",
                      "13.21.1",
                      "13.19.1",
                      "13.18.1",
                      "13.17.1",
                      "13.16.1",
                      "13.15.1",
                      "13.14.1",
                      "13.13.1",
                      "13.12.1",
                      "13.11.1",
                      "13.10.1",
                      "13.9.1",
                      "13.8.1",
                      "13.7.1",
                      "13.6.1",
                      "13.5.1",
                      "13.4.1",
                      "13.3.1",
                      "13.1.1",
                      "12.23.1",
                      "12.22.1",
                      "12.21.1",
                      "12.20.1",
                      "12.19.1",
                      "12.18.1",
                      "12.17.1",
                      "12.16.1",
                      "12.15.1",
                      "12.14.1",
                      "12.13.1",
                      "12.12.1",
                      "12.11.1",
                      "12.10.1",
                      "12.9.1",
                      "12.8.1",
                      "12.7.1",
                      "12.6.1",
                      "12.5.1",
                      "12.4.1",
                      "12.3.1",
                      "12.2.1",
                      "12.1.1",
                      "11.24.1",
                      "11.23.1",
                      "11.22.1",
                      "11.21.1",
                      "11.20.1",
                      "11.19.1",
                      "11.18.1",
                      "11.17.1",
                      "11.16.1",
                      "11.15.1",
                      "11.14.1",
                      "11.13.1",
                      "11.12.1",
                      "11.11.1",
                      "11.10.1",
                      "11.9.1",
                      "11.8.1",
                      "11.7.1",
                      "11.6.1",
                      "11.5.1",
                      "11.4.1",
                      "11.3.1",
                      "11.2.1",
                      "11.1.1",
                      "10.25.1",
                      "10.24.1",
                      "10.23.1",
                      "10.22.1",
                      "10.21.1",
                      "10.20.1",
                      "10.19.1",
                      "10.10.3216176",
                      "10.10.3208608",
                      "9.9.1"
                    ]
                  },
                  {
                    "id": 1,
                    "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                    "name": "Domination",
                    "runes": {
                      "keystones": [
                        4,
                        3,
                        2,
                        1
                      ],
                      "slot1": [
                        7,
                        6,
                        5
                      ],
                      "slot2": [
                        8,
                        10,
                        9
                      ],
                      "slot3": [
                        14,
                        11,
                        13,
                        12
                      ]
                    },
                    "videogame_versions": [
                      "14.10.1",
                      "14.9.1",
                      "14.8.1",
                      "14.7.1",
                      "14.6.1",
                      "14.5.1",
                      "14.4.1",
                      "14.3.1",
                      "14.2.1",
                      "14.1.1",
                      "13.24.1",
                      "13.23.1",
                      "13.22.1",
                      "13.21.1",
                      "13.19.1",
                      "13.18.1",
                      "13.17.1",
                      "13.16.1",
                      "13.15.1",
                      "13.14.1",
                      "13.13.1",
                      "13.12.1",
                      "13.11.1",
                      "13.10.1",
                      "13.9.1",
                      "13.8.1",
                      "13.7.1",
                      "13.6.1",
                      "13.5.1",
                      "13.4.1",
                      "13.3.1",
                      "13.1.1",
                      "12.23.1",
                      "12.22.1",
                      "12.21.1",
                      "12.20.1",
                      "12.19.1",
                      "12.18.1",
                      "12.17.1",
                      "12.16.1",
                      "12.15.1",
                      "12.14.1",
                      "12.13.1",
                      "12.12.1",
                      "12.11.1",
                      "12.10.1",
                      "12.9.1",
                      "12.8.1",
                      "12.7.1",
                      "12.6.1",
                      "12.5.1",
                      "12.4.1",
                      "12.3.1",
                      "12.2.1",
                      "12.1.1",
                      "11.24.1",
                      "11.23.1",
                      "11.22.1",
                      "11.21.1",
                      "11.20.1",
                      "11.19.1",
                      "11.18.1",
                      "11.17.1",
                      "11.16.1",
                      "11.15.1",
                      "11.14.1",
                      "11.13.1",
                      "11.12.1",
                      "11.11.1",
                      "11.10.1",
                      "11.9.1",
                      "11.8.1",
                      "11.7.1",
                      "11.6.1",
                      "11.5.1",
                      "11.4.1",
                      "11.3.1",
                      "11.2.1",
                      "11.1.1",
                      "10.25.1",
                      "10.24.1",
                      "10.23.1",
                      "10.22.1",
                      "10.21.1",
                      "10.20.1",
                      "10.19.1",
                      "10.10.3216176",
                      "10.10.3208608",
                      "9.9.1"
                    ]
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLRunePaths"
            }
          }
        },
        "description": "A list of League-of-Legends runes paths"
      }
    },
    "schemas": {
      "LoLRunePaths": {
        "items": {
          "additionalProperties": false,
          "deprecated": false,
          "properties": {
            "id": {
              "description": "ID of the rune path",
              "minimum": 1,
              "title": "LoLRunePathID",
              "type": "integer"
            },
            "image_url": {
              "description": "URL to an image of the rune path",
              "format": "uri",
              "title": "LoLRunePathImageURL",
              "type": "string"
            },
            "name": {
              "description": "Name of the rune",
              "title": "LoLRunePathName",
              "type": "string"
            },
            "runes": {
              "additionalProperties": false,
              "deprecated": false,
              "properties": {
                "keystones": {
                  "description": "IDs of the keystone runes available for this path",
                  "items": {
                    "description": "ID of the rune",
                    "minimum": 1,
                    "title": "LoLRuneReforgedID",
                    "type": "integer"
                  },
                  "title": "LoLKeystoneRunes",
                  "type": "array"
                },
                "slot1": {
                  "description": "IDs of the slot 1 runes available for this path",
                  "items": {
                    "description": "ID of the rune",
                    "minimum": 1,
                    "title": "LoLRuneReforgedID",
                    "type": "integer"
                  },
                  "maxItems": 4,
                  "minItems": 3,
                  "title": "LoLSlot1Runes",
                  "type": "array"
                },
                "slot2": {
                  "description": "IDs of the slot 2 runes available for this path",
                  "items": {
                    "description": "ID of the rune",
                    "minimum": 1,
                    "title": "LoLRuneReforgedID",
                    "type": "integer"
                  },
                  "maxItems": 6,
                  "minItems": 3,
                  "title": "LoLSlot2Runes",
                  "type": "array"
                },
                "slot3": {
                  "description": "IDs of the slot 3 runes available for this path",
                  "items": {
                    "description": "ID of the rune",
                    "minimum": 1,
                    "title": "LoLRuneReforgedID",
                    "type": "integer"
                  },
                  "maxItems": 4,
                  "minItems": 3,
                  "title": "LoLSlot3Runes",
                  "type": "array"
                }
              },
              "required": [
                "keystones",
                "slot1",
                "slot2",
                "slot3"
              ],
              "title": "LoLRunePathRunesObject",
              "type": "object"
            },
            "videogame_versions": {
              "description": "Array of of video game versions (ie. patches) for this resource",
              "items": {
                "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                "title": "VideogameVersion",
                "type": "string"
              },
              "title": "VideogameVersions",
              "type": "array"
            }
          },
          "required": [
            "id",
            "image_url",
            "name",
            "runes",
            "videogame_versions"
          ],
          "title": "LoLRunePath",
          "type": "object"
        },
        "title": "LoLRunePaths",
        "type": "array"
      },
      "filter_over_LoLRunePaths": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "id": {
            "items": {
              "description": "ID of the rune path",
              "minimum": 1,
              "title": "LoLRunePathID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "name": {
            "items": {
              "description": "Name of the rune",
              "title": "LoLRunePathName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "videogame_version": {
            "description": "Filter by the names of videogame versions, all versions using `filter[videogame_version]=all`, or by the latest version using `filter[videogame_version]=latest`"
          }
        },
        "type": "object"
      },
      "range_over_LoLRunePaths": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "id": {
            "items": {
              "description": "ID of the rune path",
              "minimum": 1,
              "title": "LoLRunePathID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "name": {
            "items": {
              "description": "Name of the rune",
              "title": "LoLRunePathName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          }
        },
        "type": "object"
      },
      "search_over_LoLRunePaths": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "name": {
            "description": "Name of the rune",
            "title": "LoLRunePathName",
            "type": "string"
          }
        },
        "type": "object"
      },
      "sort_over_LoLRunePaths": {
        "items": {
          "enum": [
            "id",
            "-id",
            "name",
            "-name"
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
    "/lol/runes-reforged-paths": {
      "get": {
        "description": "List the latest version of League of Legends (reforged) rune paths\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_runes-reforged-paths",
        "parameters": [
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLRunePaths"
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
              "$ref": "#/components/schemas/range_over_LoLRunePaths"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLRunePaths"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLRunePaths"
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
            "$ref": "#/components/responses/LoLRunePaths"
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
        "summary": "List rune paths",
        "tags": [
          "LoL runes"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/runes-reforged-paths' \\\n     --header 'accept: application/json'\n",
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