from unittest.mock import patch

from telemetry.routes import inspect_route


@patch("telemetry.routes.subprocess.run")
def test_route_inspection(mock_run):
    mock_run.return_value.stdout = (
        "Routing entry for 10.20.20.0/24\n"
        "  Known via "ospf", distance 110\n"
        "  * 10.0.12.2, via eth1, cost 20\n"
    )
    mock_run.return_value.stderr = ""
    mock_run.return_value.returncode = 0

    result = inspect_route("r1", "10.20.20.0/24")
    assert result.next_hops == ("10.0.12.2",)
    assert result.interfaces == ("eth1",)
