logger_config = {
    'formatters': {
        'std_format': {
            'format': "{asctime} | {levelname} >>> {message} @ def {funcName}",
            'style': '{',
        },
        'start_format': {
            'format': "\n_________________ <<< Started test: '{message}' @ {asctime} >>> _________________",
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'tests.log',
            'level': 'DEBUG',
            'formatter': 'std_format'
        },
        'file_start': {
            'class': 'logging.FileHandler',
            'filename': 'tests.log',
            'level': 'DEBUG',
            'formatter': 'start_format'
        }
    },
    'loggers': {
        'console_logger': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
        'file_logger': {
            'level': 'DEBUG',
            'handlers': ['file']
        },
        'file_logger_start': {
            'level': 'DEBUG',
            'handlers': ['file_start']
        },

    },
    'version': 1,
    'disable_existing_loggers': False,
}
