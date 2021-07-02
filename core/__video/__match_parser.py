import re
import logging
from typing import List, Match, Sequence
from dataclasses import dataclass

from .__char import parse_to_code, get_name_by_code

player_fighter_regex = r'((?:\b\w+ ?\|? ?)?\w+ ?)(?:[(（](.+?)[)）])(?: ?vs\.? ?)((?:\b\w+ ?\|? ?)?\w+ ?)(?:[(（](.+?)[)）])'


@dataclass
class MatchInfo():
    title: str
    match_name: str = ''
    p1: str = ''
    p1_fighter: List[str] = []
    p2: str = ''
    p2_fighter: List[str] = []
    pool: bool = False
    grand_final: bool = False
    winner: bool = False
    loser: bool = False
    round: str = ''


def parse_match(title: str):
    match_info = MatchInfo(title=title)
    


def _get_codes(char_string: str):
    chars = re.split(r'[,，]', char_string)
    return list(map(lambda x: parse_to_code(x), chars))


def __replace_name(match: Match):
    p1_fighter = _get_codes(match.group(1))
    p2_fighter = _get_codes(match.group(3))
    return '{} ({}) Vs. {} ({})'.format(match.group(0), ', '.join(p1_fighter),
                                        match.group(2), ', '.join(p2_fighter))


def get_player_fighter(title: str, match_info: MatchInfo):
    result = []
    title = re.sub(player_fighter_regex,
                   lambda x: result.append(x) or __replace_name(x), title, 0,
                   re.IGNORECASE)
    if len(result):
        logging.warning('cannot find player/fighter, no result: ', title)
        return None
    result = result[0]
    if not len(result) == 4:
        logging.warning('cannot find player/fighter, groups != 5: ', title)
        return None
    match_info.p1 = result.group(0)
    match_info.p1_fighter = _get_codes(result.group(1))
    match_info.p2 = result.group(2)
    match_info.p2_fighter = _get_codes(result.group(3))
    return title, match_info


def get_round(title: str, match_info: MatchInfo):
    def replace_with_result(string: str, match: str, replace: str):
        result = []
        match = match + r'(?:\'?s?\'?)(?:\b|$)'
        return re.sub(match, lambda x: result.append(x.group(0)) or replace,
                      string, 0,
                      re.IGNORECASE), result[0] if len(result) else None

    # check grand
    title, result = replace_with_result(title, r'(grand ?fin.+?)', '总决赛')
    if result:
        match_info.grand_final = True
        return title

    # check if winner
    title, result = replace_with_result(title, r'(winner)', '胜者组')
    if result:
        match_info.winner = True
    else:
        # not winner, check if loser
        title, result = replace_with_result(title, r'(loser)', '败者组')
        if result:
            match_info.loser = True

    # check if pool
    title, result = replace_with_result(title, r'(pool|bracket)', '初赛')
    if result:
        match_info.pool = True

    # look for round
    result = re.search(r'((?:round|top) \d+\b)', title, re.IGNORECASE)
    if result:
        match_info.round = result.group(1)

    for keyword, replace in [(r'(semi)', '半决赛'), (r'(final)', '决赛'),
                             (r'(qua.+?)', '¼决赛')]:
        title, result = replace_with_result(title, keyword, replace)
        if result:
            match_info.round = result.group(0)
            break

    # look for game name
    result = re.search(r'(^.+(?: )(?:top|ssbu|-|grand|win|los|pool|vs))',
                       title, re.IGNORECASE)
    if result:
        match_info.match_name = result.group(1)

    return title, match_info
