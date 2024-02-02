
import random


APIKEY = 'lstzFDEOhfFNMLikKa0am9mgEKLBl49T'

ASSET_TYPE = ['etf', 'fund', 'stock']

EXCHANGE = {
            "NYSE": {
                    "name": "exchanges_equity_nyse",
                    "id": "E0EXG$XNYS"
                    },

            "NASDAQ" : {
                    "name": "exchanges_equity_nasdaq",
                    "id": "E0EXG$XNAS"
                        },

            "LSE" : {
                    "name": "exchanges_london_stock_exchange",
                    "id": "E0EXG$XLON"
                    },

            "AMSTERDAM" : {
                    "name": "exchanges_equity_nyse_euronext_amsterdam",
                    "id": "E0EXG$XAMS"
                        },
 
            "ATHENS" : {
                    "name": "exchanges_equity_athens_stock_exchange",
                    "id": "E0EXG$XATH"
                        },

            "BOLSA_DE_VALORES" : {
                    "name": "exchanges_equity_bolsa_de_valores",
                    "id": "E0EXG$XMEX"
                        },

            "BOMBAY" : {
                    "name": "exchanges_equity_bombay_stock_exchange",
                    "id": "E0EXG$XBOM"
                        },

            "BORSA_ITALIANA" : {
                    "name": "exchanges_equity_borsa_italiana",
                    "id": "E0EXG$XMIL"
                        },

            "BRUSSELS" : {
                    "name": "exchanges_equity_nyse_brussels",
                    "id": "E0EXG$XBRU"
                        },

            "COPENHAGEN" : {
                    "name": "exchanges_equity_omx_exchange_copenhagen",
                    "id": "E0EXG$XCSE"
                            },

            "HELSINKI" : {
                    "name": "exchanges_equity_omx_exchange_helsinki",
                    "id": "E0EXG$XHEL"
                        },

                "HONG-KONG" : {
                    "name": "exchanges_HONG_KONG",
                    "id": "E0EXG$XHKG"
                        },
            "ICELAND" : {
                    "name": "exchanges_equity_omx_exchange_iceland",
                    "id": "E0EXG$XICE"
                        },

            "INDIA" : {
                    "name": "exchanges_equity_india_stock_exchange",
                    "id": "E0EXG$XNSE"
                        },

            "IPSX" : {
                    "name": "exchanges_equity_exchange_IPSX",
                    "id": "E0EXG$IPSX"
                        },

            "IRELAND" : {
                    "name": "exchanges_equity_irish_stock_exchange",
                    "id": "E0EXG$XDUB"
                        },

            "ISTANBUL" : {
                    "name": "exchanges_equity_istanbul_stock_exchange",
                    "id": "E0EXG$XIST"
                        },

            "LISBON" : {
                    "name": "exchanges_equity_nyse_euronext_lisbon",
                    "id": "E0EXG$XLIS"
                        },

            "LUXEMBOURG" : {
                    "name": "exchanges_equity_luxembourg_stock_exchange",
                    "id": "E0EXG$XLUX"
                        },

            "OSLO_BORS" : {
                    "name": "exchanges_equity_oslo_bors",
                    "id": "E0EXG$XOSL"
                        },

            "PARIS" : {
                    "name": "exchanges_equity_nyse_paris",
                    "id": "E0EXG$XPAR"
                        },

            "RIGA" : {
                    "name": "exchanges_equity_omx_exchange_riga",
                    "id": "E0EXG$XRIS"
                        },

            "SHANGAI" : {
                    "name": "exchanges_equity_shanghai_stock_exchange",
                    "id": "E0EXG$XSHG"
                        },

            "SHENZHEN" : {
                    "name": "exchanges_equity_shenzhen_stock_exchange",
                    "id": "E0EXG$XSHE"
                        },

            "SINGAPORE" : {
                    "name": "exchanges_equity_singapore",
                    "id": "E0EXG$XSES"
                        },
        
            "STOCKHOLM" : {
                    "name": "exchanges_equity_nasdaq_omx_stockholm",
                    "id": "E0EXG$XSTO"
                        },

            "SWISS" : {
                    "name": "exchanges_equity_six__swiss_exchange",
                    "id": "E0EXG$XSWX"
                    },

            "TAIWAN" : {
                    "name": "exchanges_equity_taiwan_stock_exchange",
                    "id": "E0EXG$XTAI"
                        },

            "TALLIN" : {
                    "name": "exchanges_equity_tallin_stock_exchange",
                    "id": "E0EXG$XTAL"
                        },

            "THAILAND" : {
                    "name": "exchanges_equity_thailand_stock_exchange",
                    "id": "E0EXG$XBKK"
                        },

            "TOKYO" : {
                    "name": "exchanges_equity_tokyo_stock_exchange",
                    "id": "E0EXG$XTKS"
                        },

            "VILNIUS" : {
                    "name": "exchanges_equity_omx_exchange_vilnius",
                    "id": "E0EXG$XLIT"
                        },
                                                                                
            "WARSAW" :{
                    "name": "exchanges_equity_warsaw_stock_exchange",
                    "id": "E0EXG$XWAR"
                        },

            "WIENER_BOERSE" : {
                    "name": "exchanges_equity_wiener_boerse",
                    "id": "E0EXG$XWBO"
                        },

        "WORLDWIDE_EQUITY" : {
                    "name": "exchanges_worldwide_equity",
                    "id": "E0WWE$$ALL"
                        },
            }


FIELDS = [
    'AdministratorCompanyId',
    'AlphaM36',
    'AnalystRatingScale',
    'AverageCreditQualityCode',
    'AverageMarketCapital',
    'BetaM36',
    'BondStyleBox',
    'brandingCompanyId',
    'categoryId',
    'CategoryName',
    'ClosePrice',
    'currency',
    'DebtEquityRatio',
    'distribution',
    'DividendYield',
    'EBTMarginYear1',
    'EffectiveDuration',
    'EPSGrowth3YYear1',
    'equityStyle',
    'EquityStyleBox',
    'exchangeCode',
    'ExchangeId',
    'ExpertiseAdvanced',
    'ExpertiseBasic',
    'ExpertiseInformed',
    'FeeLevel',
    'fundShareClassId',
    'fundSize',
    'fundStyle',
    'FundTNAV',
    'GBRReturnD1',
    'GBRReturnM0',
    'GBRReturnM1',
    'GBRReturnM12',
    'GBRReturnM120',
    'GBRReturnM3',
    'GBRReturnM36',
    'GBRReturnM6',
    'GBRReturnM60',
    'GBRReturnW1',
    'geoRegion',
    'globalAssetClassId',
    'globalCategoryId',
    'iMASectorId',
    'IndustryName',
    'InitialPurchase',
    'instrumentName',
    'investment',
    'investmentExpertise',
    'investmentObjective',
    'investmentType',
    'investorType',
    'InvestorTypeEligibleCounterparty',
    'InvestorTypeProfessional',
    'InvestorTypeRetail',
    'LargestSector',
    'LegalName',
    'managementStyle',
    'ManagerTenure',
    'MarketCap',
    'MarketCountryName',
    'MaxDeferredLoad',
    'MaxFrontEndLoad',
    'MaximumExitCostAcquired',
    'MorningstarRiskM255',
    'Name',
    'NetMargin',
    'ongoingCharge',
    'OngoingCostActual',
    'PEGRatio',
    'PERatio',
    'PerformanceFeeActual',
    'PriceCurrency',
    'QuantitativeRating',
    'R2M36',
    'ReturnD1',
    'ReturnM0',
    'ReturnM1',
    'ReturnM12',
    'ReturnM120',
    'ReturnM3',
    'ReturnM36',
    'ReturnM6',
    'ReturnM60',
    'ReturnProfileGrowth',
    'ReturnProfileHedging',
    'ReturnProfileIncome',
    'ReturnProfileOther',
    'ReturnProfilePreservation',
    'ReturnW1',
    'RevenueGrowth3Y',
    'riskSrri',
    'ROATTM',
    'ROETTM',
    'ROEYear1',
    'ROICYear1',
    'SecId',
    'SectorName',
    'shareClassType',
    'SharpeM36',
    'StandardDeviationM36',
    'starRating',
    'StarRatingM255',
    'SustainabilityRank',
    'sustainabilityRating',
    'TenforeId',
    'Ticker',
    'totalReturn',
    'totalReturnTimeFrame',
    'TrackRecordExtension',
    'TransactionFeeActual',
    'umbrellaCompanyId',
    'Universe',
    'Yield_M12',
    'yieldPercent',

]


FILTER_FUND = [  
    'AdministratorCompanyId',
    'AnalystRatingScale',
    'BondStyleBox',
    'BrandingCompanyId',
    'CategoryId',
    'CollectedSRRI',
    'distribution',
    'EquityStyleBox',
    'ExpertiseInformed',
    'FeeLevel',
    'FundTNAV',
    'GBRReturnM0',
    'GBRReturnM12',
    'GBRReturnM120',
    'GBRReturnM36',
    'GBRReturnM60',
    'GlobalAssetClassId',
    'GlobalCategoryId',
    'IMASectorID',
    'IndexFund',
    'InvestorTypeProfessional',
    'LargestRegion',
    'LargestSector',
    'OngoingCharge',
    'QuantitativeRating',
    'ReturnProfilePreservation',
    'ShareClassTypeId',
    'starRating',
    'SustainabilityRank',
    'UmbrellaCompanyId',
    'Yield_M12',

        ]

FILTER_STOCK = [  
    'debtEquityRatio',
    'DividendYield',
    'epsGrowth3YYear1',
    'EquityStyleBox',
    'GBRReturnM0',
    'GBRReturnM12',
    'GBRReturnM36',
    'GBRReturnM60',
    'GBRReturnM120',
    'IndustryId',
    'MarketCap',
    'netMargin',
    'PBRatio',
    'PEGRatio',
    'PERatio',
    'PSRatio',
    'revenueGrowth3Y',
    'roattm',
    'roettm',
    'SectorId',
        ]



SITE = {
        
        'af' : {'iso3' : 'AFG', 'site' : ''},
        'ax' : {'iso3' : 'ALA', 'site' : ''},
        'al' : {'iso3' : 'ALB', 'site' : ''},
        'dz' : {'iso3' : 'DZA', 'site' : ''},
        'as' : {'iso3' : 'ASM', 'site' : ''},
        'ad' : {'iso3' : 'AND', 'site' : ''},
        'ao' : {'iso3' : 'AGO', 'site' : ''},
        'ai' : {'iso3' : 'AIA', 'site' : ''},
        'aq' : {'iso3' : 'ATA', 'site' : ''},
        'ag' : {'iso3' : 'ATG', 'site' : ''},
        'ar' : {'iso3' : 'ARG', 'site' : ''},
        'am' : {'iso3' : 'ARM', 'site' : ''},
        'aw' : {'iso3' : 'ABW', 'site' : ''},
        'au' : {'iso3' : 'AUS', 'site' : ''},
        'at' : {'iso3' : 'AUT', 'site' : ''},
        'az' : {'iso3' : 'AZE', 'site' : ''},
        'bs' : {'iso3' : 'BHS', 'site' : ''},
        'bh' : {'iso3' : 'BHR', 'site' : ''},
        'bd' : {'iso3' : 'BGD', 'site' : ''},
        'bb' : {'iso3' : 'BRB', 'site' : ''},
        'by' : {'iso3' : 'BLR', 'site' : ''},
        'be' : {'iso3' : 'BEL', 'site' : 'https://www.morningstar.be/be/'},
        'bz' : {'iso3' : 'BLZ', 'site' : ''},
        'bj' : {'iso3' : 'BEN', 'site' : ''},
        'bm' : {'iso3' : 'BMU', 'site' : ''},
        'bt' : {'iso3' : 'BTN', 'site' : ''},
        'bo' : {'iso3' : 'BOL', 'site' : ''},
        'bq' : {'iso3' : 'BES', 'site' : ''},
        'ba' : {'iso3' : 'BIH', 'site' : ''},
        'bw' : {'iso3' : 'BWA', 'site' : ''},
        'bv' : {'iso3' : 'BVT', 'site' : ''},
        'br' : {'iso3' : 'BRA', 'site' : 'https://www.morningstarbr.com/br/'},
        'io' : {'iso3' : 'IOT', 'site' : ''},
        'bn' : {'iso3' : 'BRN', 'site' : ''},
        'bg' : {'iso3' : 'BGR', 'site' : ''},
        'bf' : {'iso3' : 'BFA', 'site' : ''},
        'bi' : {'iso3' : 'BDI', 'site' : ''},
        'cv' : {'iso3' : 'CPV', 'site' : ''},
        'kh' : {'iso3' : 'KHM', 'site' : ''},
        'cm' : {'iso3' : 'CMR', 'site' : ''},
        'ca' : {'iso3' : 'CAN', 'site' : 'https://www.morningstar.ca/ca/'},
        'ky' : {'iso3' : 'CYM', 'site' : ''},
        'cf' : {'iso3' : 'CAF', 'site' : ''},
        'td' : {'iso3' : 'TCD', 'site' : ''},
        'cl' : {'iso3' : 'CHL', 'site' : 'https://www.morningstar.cl/cl/'},
        'cn' : {'iso3' : 'CHN', 'site' : ''},
        'cx' : {'iso3' : 'CXR', 'site' : ''},
        'cc' : {'iso3' : 'CCK', 'site' : ''},
        'co' : {'iso3' : 'COL', 'site' : ''},
        'km' : {'iso3' : 'COM', 'site' : ''},
        'cd' : {'iso3' : 'COD', 'site' : ''},
        'cg' : {'iso3' : 'COG', 'site' : ''},
        'ck' : {'iso3' : 'COK', 'site' : ''},
        'cr' : {'iso3' : 'CRI', 'site' : ''},
        'ci' : {'iso3' : 'CIV', 'site' : ''},
        'hr' : {'iso3' : 'HRV', 'site' : ''},
        'cu' : {'iso3' : 'CUB', 'site' : ''},
        'cw' : {'iso3' : 'CUW', 'site' : ''},
        'cy' : {'iso3' : 'CYP', 'site' : ''},
        'cz' : {'iso3' : 'CZE', 'site' : ''},
        'dk' : {'iso3' : 'DNK', 'site' : 'https://www.morningstar.dk/dk/'},
        'dj' : {'iso3' : 'DJI', 'site' : ''},
        'dm' : {'iso3' : 'DMA', 'site' : ''},
        'do' : {'iso3' : 'DOM', 'site' : ''},
        'ec' : {'iso3' : 'ECU', 'site' : ''},
        'eg' : {'iso3' : 'EGY', 'site' : ''},
        'sv' : {'iso3' : 'SLV', 'site' : ''},
        'gq' : {'iso3' : 'GNQ', 'site' : ''},
        'er' : {'iso3' : 'ERI', 'site' : ''},
        'ee' : {'iso3' : 'EST', 'site' : ''},
        'sz' : {'iso3' : 'SWZ', 'site' : ''},
        'et' : {'iso3' : 'ETH', 'site' : ''},
        'fk' : {'iso3' : 'FLK', 'site' : ''},
        'fo' : {'iso3' : 'FRO', 'site' : ''},
        'fj' : {'iso3' : 'FJI', 'site' : ''},
        'fi' : {'iso3' : 'FIN', 'site' : 'https://www.morningstar.fi/fi/'},
        'fr' : {'iso3' : 'FRA', 'site' : 'https://www.morningstar.fr/fr/'},
        'gf' : {'iso3' : 'GUF', 'site' : ''},
        'pf' : {'iso3' : 'PYF', 'site' : ''},
        'tf' : {'iso3' : 'ATF', 'site' : ''},
        'ga' : {'iso3' : 'GAB', 'site' : ''},
        'gm' : {'iso3' : 'GMB', 'site' : ''},
        'ge' : {'iso3' : 'GEO', 'site' : ''},
        'de' : {'iso3' : 'DEU', 'site' : 'https://www.morningstar.de/de/'},
        'gh' : {'iso3' : 'GHA', 'site' : ''},
        'gi' : {'iso3' : 'GIB', 'site' : ''},
        'gr' : {'iso3' : 'GRC', 'site' : ''},
        'gl' : {'iso3' : 'GRL', 'site' : ''},
        'gd' : {'iso3' : 'GRD', 'site' : ''},
        'gp' : {'iso3' : 'GLP', 'site' : ''},
        'gu' : {'iso3' : 'GUM', 'site' : ''},
        'gt' : {'iso3' : 'GTM', 'site' : ''},
        'gg' : {'iso3' : 'GGY', 'site' : ''},
        'gn' : {'iso3' : 'GIN', 'site' : ''},
        'gw' : {'iso3' : 'GNB', 'site' : ''},
        'gy' : {'iso3' : 'GUY', 'site' : ''},
        'ht' : {'iso3' : 'HTI', 'site' : ''},
        'hm' : {'iso3' : 'HMD', 'site' : ''},
        'va' : {'iso3' : 'VAT', 'site' : ''},
        'hn' : {'iso3' : 'HND', 'site' : ''},
        'hk' : {'iso3' : 'HKG', 'site' : 'https://www.morningstar.hk/hk/'},
        'hu' : {'iso3' : 'HUN', 'site' : ''},
        'is' : {'iso3' : 'ISL', 'site' : ''},
        'in' : {'iso3' : 'IND', 'site' : ''},
        'id' : {'iso3' : 'IDN', 'site' : ''},
        'ir' : {'iso3' : 'IRN', 'site' : ''},
        'iq' : {'iso3' : 'IRQ', 'site' : ''},
        'ie' : {'iso3' : 'IRL', 'site' : 'https://www.morningstarfunds.ie/ie/'},
        'im' : {'iso3' : 'IMN', 'site' : ''},
        'il' : {'iso3' : 'ISR', 'site' : ''},
        'it' : {'iso3' : 'ITA', 'site' : 'https://www.morningstar.it/it/'},
        'jm' : {'iso3' : 'JAM', 'site' : ''},
        'jp' : {'iso3' : 'JPN', 'site' : ''},
        'je' : {'iso3' : 'JEY', 'site' : ''},
        'jo' : {'iso3' : 'JOR', 'site' : ''},
        'kz' : {'iso3' : 'KAZ', 'site' : ''},
        'ke' : {'iso3' : 'KEN', 'site' : ''},
        'ki' : {'iso3' : 'KIR', 'site' : ''},
        'kp' : {'iso3' : 'PRK', 'site' : ''},
        'kr' : {'iso3' : 'KOR', 'site' : ''},
        'kw' : {'iso3' : 'KWT', 'site' : ''},
        'kg' : {'iso3' : 'KGZ', 'site' : ''},
        'la' : {'iso3' : 'LAO', 'site' : ''},
        'lv' : {'iso3' : 'LVA', 'site' : ''},
        'lb' : {'iso3' : 'LBN', 'site' : ''},
        'ls' : {'iso3' : 'LSO', 'site' : ''},
        'lr' : {'iso3' : 'LBR', 'site' : ''},
        'ly' : {'iso3' : 'LBY', 'site' : ''},
        'li' : {'iso3' : 'LIE', 'site' : ''},
        'lt' : {'iso3' : 'LTU', 'site' : ''},
        'lu' : {'iso3' : 'LUX', 'site' : ''},
        'mo' : {'iso3' : 'MAC', 'site' : ''},
        'mk' : {'iso3' : 'MKD', 'site' : ''},
        'mg' : {'iso3' : 'MDG', 'site' : ''},
        'mw' : {'iso3' : 'MWI', 'site' : ''},
        'my' : {'iso3' : 'MYS', 'site' : ''},
        'mv' : {'iso3' : 'MDV', 'site' : ''},
        'ml' : {'iso3' : 'MLI', 'site' : ''},
        'mt' : {'iso3' : 'MLT', 'site' : ''},
        'mh' : {'iso3' : 'MHL', 'site' : ''},
        'mq' : {'iso3' : 'MTQ', 'site' : ''},
        'mr' : {'iso3' : 'MRT', 'site' : ''},
        'mu' : {'iso3' : 'MUS', 'site' : ''},
        'yt' : {'iso3' : 'MYT', 'site' : ''},
        'mx' : {'iso3' : 'MEX', 'site' : 'https://www.morningstar.com.mx/mx/'},
        'fm' : {'iso3' : 'FSM', 'site' : ''},
        'md' : {'iso3' : 'MDA', 'site' : ''},
        'mc' : {'iso3' : 'MCO', 'site' : ''},
        'mn' : {'iso3' : 'MNG', 'site' : ''},
        'me' : {'iso3' : 'MNE', 'site' : ''},
        'ms' : {'iso3' : 'MSR', 'site' : ''},
        'ma' : {'iso3' : 'MAR', 'site' : ''},
        'mz' : {'iso3' : 'MOZ', 'site' : ''},
        'mm' : {'iso3' : 'MMR', 'site' : ''},
        'na' : {'iso3' : 'NAM', 'site' : ''},
        'nr' : {'iso3' : 'NRU', 'site' : ''},
        'np' : {'iso3' : 'NPL', 'site' : ''},
        'nl' : {'iso3' : 'NLD', 'site' : 'https://www.morningstar.nl/nl/'},
        'nc' : {'iso3' : 'NCL', 'site' : ''},
        'nz' : {'iso3' : 'NZL', 'site' : ''},
        'ni' : {'iso3' : 'NIC', 'site' : ''},
        'ne' : {'iso3' : 'NER', 'site' : ''},
        'ng' : {'iso3' : 'NGA', 'site' : ''},
        'nu' : {'iso3' : 'NIU', 'site' : ''},
        'nf' : {'iso3' : 'NFK', 'site' : ''},
        'mp' : {'iso3' : 'MNP', 'site' : ''},
        'no' : {'iso3' : 'NOR', 'site' : 'https://www.morningstar.no/no/'},
        'om' : {'iso3' : 'OMN', 'site' : ''},
        'pk' : {'iso3' : 'PAK', 'site' : ''},
        'pw' : {'iso3' : 'PLW', 'site' : ''},
        'ps' : {'iso3' : 'PSE', 'site' : ''},
        'pa' : {'iso3' : 'PAN', 'site' : ''},
        'pg' : {'iso3' : 'PNG', 'site' : ''},
        'py' : {'iso3' : 'PRY', 'site' : ''},
        'pe' : {'iso3' : 'PER', 'site' : ''},
        'ph' : {'iso3' : 'PHL', 'site' : ''},
        'pn' : {'iso3' : 'PCN', 'site' : ''},
        'pl' : {'iso3' : 'POL', 'site' : ''},
        'pt' : {'iso3' : 'PRT', 'site' : 'https://www.morningstar.pt/pt/'},
        'pr' : {'iso3' : 'PRI', 'site' : ''},
        'qa' : {'iso3' : 'QAT', 'site' : ''},
        're' : {'iso3' : 'REU', 'site' : ''},
        'ro' : {'iso3' : 'ROU', 'site' : ''},
        'ru' : {'iso3' : 'RUS', 'site' : ''},
        'rw' : {'iso3' : 'RWA', 'site' : ''},
        'bl' : {'iso3' : 'BLM', 'site' : ''},
        'sh' : {'iso3' : 'SHN', 'site' : ''},
        'kn' : {'iso3' : 'KNA', 'site' : ''},
        'lc' : {'iso3' : 'LCA', 'site' : ''},
        'mf' : {'iso3' : 'MAF', 'site' : ''},
        'pm' : {'iso3' : 'SPM', 'site' : ''},
        'vc' : {'iso3' : 'VCT', 'site' : ''},
        'ws' : {'iso3' : 'WSM', 'site' : ''},
        'sm' : {'iso3' : 'SMR', 'site' : ''},
        'st' : {'iso3' : 'STP', 'site' : ''},
        'sa' : {'iso3' : 'SAU', 'site' : ''},
        'sn' : {'iso3' : 'SEN', 'site' : ''},
        'rs' : {'iso3' : 'SRB', 'site' : ''},
        'sc' : {'iso3' : 'SYC', 'site' : ''},
        'sl' : {'iso3' : 'SLE', 'site' : ''},
        'sg' : {'iso3' : 'SGP', 'site' : 'https://sg.morningstar.com/sg/'},
        'sx' : {'iso3' : 'SXM', 'site' : ''},
        'sk' : {'iso3' : 'SVK', 'site' : ''},
        'si' : {'iso3' : 'SVN', 'site' : ''},
        'sb' : {'iso3' : 'SLB', 'site' : ''},
        'so' : {'iso3' : 'SOM', 'site' : ''},
        'za' : {'iso3' : 'ZAF', 'site' : ''},
        'gs' : {'iso3' : 'SGS', 'site' : ''},
        'ss' : {'iso3' : 'SSD', 'site' : ''},
        'es' : {'iso3' : 'ESP', 'site' : 'https://www.morningstar.es/es/'},
        'lk' : {'iso3' : 'LKA', 'site' : ''},
        'sd' : {'iso3' : 'SDN', 'site' : ''},
        'sr' : {'iso3' : 'SUR', 'site' : ''},
        'sj' : {'iso3' : 'SJM', 'site' : ''},
        'se' : {'iso3' : 'SWE', 'site' : 'https://www.morningstar.se/se/'},
        'ch' : {'iso3' : 'CHE', 'site' : 'https://www.morningstar.ch/ch/'},
        'sy' : {'iso3' : 'SYR', 'site' : ''},
        'tw' : {'iso3' : 'TWN', 'site' : ''},
        'tj' : {'iso3' : 'TJK', 'site' : ''},
        'tz' : {'iso3' : 'TZA', 'site' : ''},
        'th' : {'iso3' : 'THA', 'site' : ''},
        'tl' : {'iso3' : 'TLS', 'site' : ''},
        'tg' : {'iso3' : 'TGO', 'site' : ''},
        'tk' : {'iso3' : 'TKL', 'site' : ''},
        'to' : {'iso3' : 'TON', 'site' : ''},
        'tt' : {'iso3' : 'TTO', 'site' : ''},
        'tn' : {'iso3' : 'TUN', 'site' : ''},
        'tr' : {'iso3' : 'TUR', 'site' : ''},
        'tm' : {'iso3' : 'TKM', 'site' : ''},
        'tc' : {'iso3' : 'TCA', 'site' : ''},
        'tv' : {'iso3' : 'TUV', 'site' : ''},
        'ug' : {'iso3' : 'UGA', 'site' : ''},
        'ua' : {'iso3' : 'UKR', 'site' : ''},
        'ae' : {'iso3' : 'ARE', 'site' : ''},
        'gb' : {'iso3' : 'GBR', 'site' : 'https://www.morningstar.co.uk/uk/'},
        'um' : {'iso3' : 'UMI', 'site' : ''},
        'us' : {'iso3' : 'USA', 'site' : 'https://www.morningstar.com/'},
        'uy' : {'iso3' : 'URY', 'site' : ''},
        'uz' : {'iso3' : 'UZB', 'site' : ''},
        'vu' : {'iso3' : 'VUT', 'site' : ''},
        've' : {'iso3' : 'VEN', 'site' : ''},
        'vn' : {'iso3' : 'VNM', 'site' : ''},
        'vg' : {'iso3' : 'VGB', 'site' : ''},
        'vi' : {'iso3' : 'VIR', 'site' : ''},
        'wf' : {'iso3' : 'WLF', 'site' : ''},
        'eh' : {'iso3' : 'ESH', 'site' : ''},
        'ye' : {'iso3' : 'YEM', 'site' : ''},
        'zm' : {'iso3' : 'ZMB', 'site' : ''},
        'zw' : {'iso3' : 'ZWE', 'site' : ''},

 }


USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ko; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2",
    "Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) Gecko/20080214 Firefox/2.0.0.12",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8",
    "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.5) Gecko/20060819 Firefox/1.5.0.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3",
    "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.6",
    "Mozilla/5.0 (Windows; Windows NT 6.1; rv:2.0b2) Gecko/20100720 Firefox/4.0b2",
    "Mozilla/5.0 (X11; Linux x86_64; rv:2.0b4) Gecko/20100818 Firefox/4.0b4",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2) Gecko/20100308 Ubuntu/10.04 (lucid) Firefox/3.6 GTB7.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b7) Gecko/20101111 Firefox/4.0b7",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b8pre) Gecko/20101114 Firefox/4.0b8pre",
    "Mozilla/5.0 (X11; Linux x86_64; rv:2.0b9pre) Gecko/20110111 Firefox/4.0b9pre",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b9pre) Gecko/20101228 Firefox/4.0b9pre",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.2a1pre) Gecko/20110324 Firefox/4.2a1pre",
    "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110613 Firefox/6.0a2",
    "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2",
    "Mozilla/5.0 (X11; Ubuntu; Linux armv7l; rv:17.0) Gecko/20100101 Firefox/17.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
    "Mozilla/5.0 (X11; Linux i686; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.4 (KHTML, like Gecko) Chrome/6.0.481.0 Safari/534.4",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.3 Safari/532.2",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.558.0 Safari/534.10",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14",
    "Mozilla/5.0 (X11; U; Windows NT 6; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.587.0 Safari/534.12",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.38 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
]




def random_user_agent():
    """
    This function selects a random User-Agent from the User-Agent list, . User-Agents are used in
    order to avoid the limitations of the requests to morningstar.com. The User-Agent is
    specified on the headers of the requests and is different for every request.

   

    Returns:
        :obj:`str` - user_agent:
            The returned :obj:`str` is the name of a random User-Agent, which will be passed on the 
            headers of a request so to avoid restrictions due to the use of multiple requests from the 
            same User-Agent.
    
    """

    return random.choice(USER_AGENTS)





