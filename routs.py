from flask import Flask
from views import AdView

app = Flask("app")#что означает app?

app.add_url_rule("/advertisements/<int:id_ad>/", view_func=AdView.as_view('advertisements_delete'),
                 methods=['DELETE', 'GET'])#когда ставим круглые скобки, а когда квадратные? в чем разница
app.add_url_rule("/advertisements", view_func=AdView.as_view('advertisements_create'), methods=['POST'])#что означает method Post?
