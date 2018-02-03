class Table:
    def __init__(self):
        self.id = None
        self.schema_id = None
        self.name = None
        self.description = None
        self.can_add = None
        self.can_edit = None
        self.can_delete = None
        self.temporal_mode = None
        self.means = None
        self.uuid = None
        self.fields = []
        self.constraints = []
        self.indices = []