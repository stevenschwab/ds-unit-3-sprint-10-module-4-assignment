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