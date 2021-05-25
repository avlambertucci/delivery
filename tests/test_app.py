def test_if_app_is_created(app):
  assert app.name == 'delivery.app'

def test_if_config_is_loaded(config):
  assert config["DEBUG"] is True

def test_request_is_404(client):
  assert client.get("/url_doesnt_exist").status_code == 404