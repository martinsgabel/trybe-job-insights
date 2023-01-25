from typing import List, Dict

import jobs


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    try:
        industries_list = []
        list = jobs.read(path)
        for offer in list:
            industry = offer["industry"]
            if industry != '' and industry not in industries_list:
                industries_list.append(industry)
        return industries_list
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo {path} não encontrado")


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
