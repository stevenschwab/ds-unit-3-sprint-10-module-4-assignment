'''Queries for postgres'''

GET_PASSENGERS_SURVIVED_AND_DIED = """
    select
        count(*) filter (where t.survived = 1) as total_passengers_survived,
        count(*) filter (where t.survived = 0) as total_passengers_died
    from titanic t;
"""

GET_PASSENGERS_IN_EACH_CLASS = """
    select
        count(*) filter (where t.pclass = 1) as class_1,
        count(*) filter (where t.pclass = 2) as class_2,
        count(*) filter (where t.pclass = 3) as class_3
    from titanic t;
"""

GET_PASSENGERS_SURVIVED_DIED_BY_CLASS = """
    select
        count(*) filter (where t.pclass = 1 and t.survived = 1) as class_1_survived,
        count(*) filter (where t.pclass = 1 and t.survived = 0) as class_1_died,
        count(*) filter (where t.pclass = 2 and t.survived = 1) as class_2_survived,
        count(*) filter (where t.pclass = 2 and t.survived = 0) as class_2_died,
        count(*) filter (where t.pclass = 3 and t.survived = 1) as class_3_survived,
        count(*) filter (where t.pclass = 3 and t.survived = 0) as class_3_died
    from titanic t;
"""

GET_AVG_AGE_OF_SURVIVORS_NONSURVIVORS = """
    select
        round(avg(t.age) filter (where t.survived = 1), 2) as avg_age_survivor,
        round(avg(t.age) filter (where t.survived = 0), 2) as avg_age_nonsurvivor
    from titanic t;
"""

GET_AVG_AGE_OF_EACH_PASSENGER_CLASS = """
    select
        round(avg(t.age) filter (where t.pclass = 1), 2) as avg_age_pclass1,
        round(avg(t.age) filter (where t.pclass = 2), 2) as avg_age_pclass2,
        round(avg(t.age) filter (where t.pclass = 3), 2) as avg_age_pclass3
    from titanic t;
"""

GET_AVG_FARE_BY_CLASS_AND_SURVIVAL = """
    select
        round(avg(t.fare) filter (where t.pclass = 1), 2) as avg_fare_pclass1,
        round(avg(t.fare) filter (where t.pclass = 1 and t.survived = 1), 2) as avg_fare_pclass1_survivor,
        round(avg(t.fare) filter (where t.pclass = 1 and t.survived = 0), 2) as avg_fare_pclass1_nonsurvivor,
        round(avg(t.fare) filter (where t.pclass = 2), 2) as avg_fare_pclass2,
        round(avg(t.fare) filter (where t.pclass = 2 and t.survived = 1), 2) as avg_fare_pclass2_survivor,
        round(avg(t.fare) filter (where t.pclass = 2 and t.survived = 0), 2) as avg_fare_pclass2_nonsurvivor,
        round(avg(t.fare) filter (where t.pclass = 3), 2) as avg_fare_pclass3,
        round(avg(t.fare) filter (where t.pclass = 3 and t.survived = 1), 2) as avg_fare_pclass3_survivor,
        round(avg(t.fare) filter (where t.pclass = 3 and t.survived = 0), 2) as avg_fare_pclass3_nonsurvivor
    from titanic t;
"""

GET_SIBLINGS_SPOUSES_ABORD_BY_CLASS_AND_SURVIVAL = """
    select
        round(
            count(*) filter (where t.siblings_spouses_aboard > 0)::Numeric / count(*),
            2
        ) as avg_siblings_spouses_aboard,
        round(
            count(*) filter (where t.siblings_spouses_aboard > 0 and t.pclass = 1)::Numeric / count(*) filter (where t.pclass = 1),
            2
        ) as avg_siblings_spouses_aboard_pclass1,
        round(
            count(*) filter (where t.siblings_spouses_aboard > 0 and t.pclass = 1 and t.survived = 1)::Numeric / count(*) filter (where t.pclass = 1 and t.survived = 1),
            2
        ) as avg_siblings_spouses_aboard_pclass1_survivor,
        round(
            count(*) filter (where t.siblings_spouses_aboard > 0 and t.pclass = 1 and t.survived = 0)::Numeric / count(*) filter (where t.pclass = 1 and t.survived = 0),
            2
        ) as avg_siblings_spouses_aboard_pclass1_nonsurvivor,
        round(
            count(*) filter (where t.siblings_spouses_aboard > 0 and t.pclass = 2)::Numeric / count(*) filter (where t.pclass = 2),
            2
        ) as avg_siblings_spouses_aboard_pclass2,
        round(
            count(*) filter (where t.siblings_spouses_aboard > 0 and t.pclass = 2 and t.survived = 1)::Numeric / count(*) filter (where t.pclass = 2 and t.survived = 1),
            2
        ) as avg_siblings_spouses_aboard_pclass2_survivor,
        round(
            count(*) filter (where t.siblings_spouses_aboard > 0 and t.pclass = 2 and t.survived = 0)::Numeric / count(*) filter (where t.pclass = 2 and t.survived = 0),
            2
        ) as avg_siblings_spouses_aboard_pclass2_nonsurvivor,
        round(
            count(*) filter (where t.siblings_spouses_aboard > 0 and t.pclass = 3)::Numeric / count(*) filter (where t.pclass = 3),
            2
        ) as avg_siblings_spouses_aboard_pclass3,
        round(
            count(*) filter (where t.siblings_spouses_aboard > 0 and t.pclass = 3 and t.survived = 1)::Numeric / count(*) filter (where t.pclass = 3 and t.survived = 1),
            2
        ) as avg_siblings_spouses_aboard_pclass3_survivor,
        round(
            count(*) filter (where t.siblings_spouses_aboard > 0 and t.pclass = 3 and t.survived = 0)::Numeric / count(*) filter (where t.pclass = 3 and t.survived = 0),
            2
        ) as avg_siblings_spouses_aboard_pclass3_nonsurvivor
    from titanic t;
"""