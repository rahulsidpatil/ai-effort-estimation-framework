from reef.web.tour import TOUR_STAGES


def test_tour_content_models_one_complete_multi_role_journey() -> None:
    assert len(TOUR_STAGES) == 10
    assert len({stage.key for stage in TOUR_STAGES}) == len(TOUR_STAGES)
    assert TOUR_STAGES[0].key == "brief"
    assert TOUR_STAGES[-1].key == "learning"
    assert any("Commercial lead" in stage.role for stage in TOUR_STAGES)
    assert any("Delivery lead" in stage.role for stage in TOUR_STAGES)
    assert all(stage.user_need and stage.guidance for stage in TOUR_STAGES)
