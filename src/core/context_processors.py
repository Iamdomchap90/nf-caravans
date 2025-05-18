"""
This module contains context processors for the project.

## Sentry

The sentry_* functions are used to expose configuration variables that the Sentry SDK uses
to record frontend errors, and to record user sessions. The rates are set to 0.0 by default,
disabling the functionality.
"""

import environ


def sentry_dsn(request):
    """
    This exposes the SENTRY_DSN environment variable to the template context.
    """

    env = environ.Env(
        SENTRY_URL=(str, False),
    )

    return {"sentry_dsn": env("SENTRY_URL")}


def sentry_profile_sample_rate(request):
    """
    This exposes the SENTRY_PROFILE_SAMPLE_RATE environment variable to the template context,
    defaulting to off if this is unset.
    """

    env = environ.Env(
        SENTRY_PROFILE_SAMPLE_RATE=(float, 0.0),
    )

    return {"sentry_profile_sample_rate": env("SENTRY_PROFILE_SAMPLE_RATE")}


def sentry_replay_session_sample_rate(request):
    """
    This exposes the SENTRY_REPLAY_SESSION_SAMPLE_RATE environment variable to the template
    context, defaulting to off if this is unset.
    """

    env = environ.Env(
        SENTRY_REPLAY_SESSION_SAMPLE_RATE=(float, 0.0),
    )

    return {"sentry_replay_session_sample_rate": env("SENTRY_REPLAY_SESSION_SAMPLE_RATE")}


def sentry_replay_error_sample_rate(request):
    """
    This exposes the SENTRY_REPLAY_ERROR_SAMPLE_RATE environment variable to the template context,
    defaulting to off if this is unset.
    """

    env = environ.Env(
        SENTRY_REPLAY_ERROR_SAMPLE_RATE=(float, 0.0),
    )

    return {"sentry_replay_error_sample_rate": env("SENTRY_REPLAY_ERROR_SAMPLE_RATE")}
