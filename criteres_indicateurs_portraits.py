##############################################################################################

# Définition de chacun des critères pour les projections climatiques
# Les projections sont exprimées sous forme de delta

#criteres_par_zip = {
#   "nom du fichier" : {
#       "recurence": ["période de récurence (annuel,DJF,MAM,JJA,SON)"], 
#       "scenario": [scénario d'émission (ssp245, ssp370)],
#       "percentile": ["p10", "p25, p50", "p75", p90"],
#       "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
#   }
#}

##############################################################################################

criteres_par_zip = {

    # delta
    "espog_tg_mean_annom.zip": {
        "recurence": ["annual"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p90"],
        "periode": ["2021-2050", "2041-2070", "2071-2100"]
    },
    # valeur
    "espog_dlyfrzthw.zip": {
        "recurence": ["annual"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p50"],
        "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
    },
    # valeur
    "espog_tg_mean_abs.zip": {
        "recurence": ["JJA"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p50"],
        "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
    },
    # valeur
    "espog_degree_days_above_0.zip": {
        "recurence": ["annual"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p50"],
        "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
    },
    # valeur
    "espog_tx_mean.zip": {
        "recurence": ["JJA"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p50"],
        "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
    },
    # delta
    "espog_tn_days_above_20.zip ": {
        "recurence": ["annual"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p90"],
        "periode": ["2021-2050", "2041-2070", "2071-2100"]
    },
    # valeur
    "espog_heat_spell_frequency_class1.zip": {
        "recurence": ["annual"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p50"],
        "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
    },
    # valeur
    "espog_tx_max.zip": {
        "recurence": ["annual"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p50"],
        "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
    },
    # valeur
    "espog_tn_mean.zip": {
        "recurence": ["DJF"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p50"],
        "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
    },
    
    # valeur
    "espog_tn_min.zip": {
        "recurence": ["annual"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p50"],
        "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
    },

    # valeur
    "espog_rx1day.zip": {
        "recurence": ["JJA"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p50"],
        "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
    },
    # delta
    "espog_prcptot_solides_hiver_deltas.zip": {
        "recurence": ["DJF"], 
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p90"],
        "periode": ["2021-2050", "2041-2070", "2071-2100"]
    },
    # valeur
    "verglas_prfr_events_longer_6h.zip": {
        "recurence": ["annual"], 
        "scenario": ["rcp45", "rcp85"], #pas de SSP, fait avec CMIP5
        "percentile": ["p50"],
        "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
    },
    # delta
    "espog_dry_spell_frequency.zip": {
        "recurence": ["annual"],
        "scenario": ["ssp245", "ssp370"],
        "percentile": ["p90"],
        "periode": ["1991-2020", "2021-2050", "2041-2070", "2071-2100"]
    }
}
