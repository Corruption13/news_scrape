input_parameters = {
        'source_news':"The Hindu",                              # Allowed: The Hindu, TOI
        'must_contain_in_title': [],                            # eg: ["| National",]
        'remove_keywords': ['Narendra Modi'],                   # Remove keywords from generated keywords list.
        'add_keywords': [],                                     # TODO
        'target_domain': "caravanmagazine.in",                  # eg: thehindu.com : Just the domain name without https:// or other path.
        'time_period':'',                                       # Allowed: [None, '1h', '1d', '7d', '1y', ]  (None is for all time)
}

webdriver_parameters = {
        'dont_show_browser': False,
        'disable_images': True,
}

email_credentials = {
        #TODO
}

