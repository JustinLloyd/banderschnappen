from season_types import SeasonData

SEASON_SPRING_KEY = "spring"
SEASON_SUMMER_KEY = "summer"
SEASON_AUTUMN_KEY = "autumn"
SEASON_WINTER_KEY = "winter"
SEASON_CONSTANT_KEY = "constant"

# the temperatures are considered the two extremes of possible world wide temperatures for any given climate
# for example, summer temperatures may hit 130F in a desert climate, but a polar climate, the highest temperature will be much lower
# the season temperature gives a range, and the climate clamps that range.
SEASON_SPRING = SeasonData(name=SEASON_SPRING_KEY, description="Spring", minimum_temperature=0, maximum_temperature=70)
SEASON_SUMMER = SeasonData(name=SEASON_SUMMER_KEY, description="Summer", minimum_temperature=50, maximum_temperature=130)
SEASON_AUTUMN = SeasonData(name=SEASON_AUTUMN_KEY, description="Autumn", minimum_temperature=0, maximum_temperature=70)
SEASON_WINTER = SeasonData(name=SEASON_WINTER_KEY, description="Winter", minimum_temperature=-40, maximum_temperature=30)
SEASON_CONSTANT = SeasonData(name=SEASON_CONSTANT_KEY, description="Constant", minimum_temperature=-40, maximum_temperature=130)

SEASONS_DB = [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER, SEASON_CONSTANT]

