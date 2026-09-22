"""Presentation-only content model for the REEF product experience."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TourStage:
    """One user-centered stop in the simulated estimation journey."""

    key: str
    short_name: str
    kicker: str
    title: str
    role: str
    user_need: str
    guidance: str


TOUR_STAGES = (
    TourStage(
        key="brief",
        short_name="Engagement brief",
        kicker="Begin with the decision",
        title="Clarify what this estimate must support.",
        role="Estimation lead",
        user_need=(
            "I need to understand the decision, included work, and deadline before choosing an "
            "estimation approach."
        ),
        guidance="REEF starts with the decision and available evidence—not a wall of coefficients.",
    ),
    TourStage(
        key="unknowns",
        short_name="Material unknowns",
        kicker="Triage incomplete information",
        title="Find the unknowns that could move the estimate.",
        role="Estimation lead",
        user_need="I need to know which gaps matter now and which can remain explicit assumptions.",
        guidance=(
            "Unknowns are ranked by consequence. They are not silently replaced with "
            "confident defaults."
        ),
    ),
    TourStage(
        key="work",
        short_name="Work decomposition",
        kicker="Make scope inspectable",
        title="Review the work before estimating it.",
        role="Estimation lead + domain specialist",
        user_need="I need to correct omissions, boundaries, dependencies, and acceptance evidence.",
        guidance=(
            "A proposed decomposition is editable evidence, not an authoritative plan "
            "produced by AI."
        ),
    ),
    TourStage(
        key="delivery",
        short_name="Delivery context",
        kicker="Describe how work will happen",
        title="Expose AI effects and organizational friction.",
        role="Engineering and delivery contributors",
        user_need="We need our delivery reality represented without hiding it in one multiplier.",
        guidance=(
            "Gross AI benefit, AI overhead, added PH, capacity loss, and wait time remain distinct."
        ),
    ),
    TourStage(
        key="evidence",
        short_name="Evidence & uncertainty",
        kicker="Show what supports the estimate",
        title="Make confidence earned and inspectable.",
        role="Estimation lead + reviewers",
        user_need=(
            "I need to see which claims are evidenced, assumed, correlated, or still unknown."
        ),
        guidance=(
            "REEF highlights decision-relevant uncertainty instead of decorating a point estimate."
        ),
    ),
    TourStage(
        key="scenarios",
        short_name="Scenario comparison",
        kicker="Compare causal choices",
        title="See what changes—and why.",
        role="Estimation team",
        user_need=(
            "We need to compare delivery approaches without losing the assumptions behind them."
        ),
        guidance=(
            "The values shown here are illustrative simulation data, not computed or validated "
            "estimates."
        ),
    ),
    TourStage(
        key="review",
        short_name="Challenge & review",
        kicker="Make challenge productive",
        title="Turn review comments into explicit decisions.",
        role="Engineering or delivery reviewer",
        user_need=(
            "I need to challenge weak assumptions and see whether material warnings were resolved."
        ),
        guidance=(
            "Approval means accepting a specific version with known warnings—not endorsing "
            "hidden logic."
        ),
    ),
    TourStage(
        key="commercial",
        short_name="Commercial view",
        kicker="Keep engineering truth stable",
        title="Change the engagement lens, not the effort.",
        role="Commercial lead",
        user_need=(
            "I need a commercial view with clear risk ownership and an unchanged "
            "engineering baseline."
        ),
        guidance=(
            "T&M, Fixed Bid, and Managed Service views transform the shared estimate; "
            "they do not redefine it."
        ),
    ),
    TourStage(
        key="actuals",
        short_name="Delivery actuals",
        kicker="Learn during delivery",
        title="Record what happened and what changed.",
        role="Delivery lead",
        user_need=(
            "I need variance explained by realized context, not reduced to a team "
            "performance score."
        ),
        guidance=(
            "Actual PH, elapsed time, scope change, friction, and AI correction effort are "
            "observed separately."
        ),
    ),
    TourStage(
        key="learning",
        short_name="Learning & feedback",
        kicker="Improve without rewriting history",
        title="Carry evidence into the next model version.",
        role="Model owner + estimation community",
        user_need=(
            "We need to learn from outcomes while preserving the original estimate and its context."
        ),
        guidance=(
            "A future model is evaluated as a new version; the accepted estimate remains immutable."
        ),
    ),
)
