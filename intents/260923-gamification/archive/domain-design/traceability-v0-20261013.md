{
  "stage": "domain-design",
  "note": "Intent v1: upstream = US của phạm vi đợt và dòng AC dạng USn-ACk (dòng thứ k của bảng AC UI/UX trong PRD v0.14). Target là component trong components.md.",
  "upstream_ids": [
    "US14", "US14-AC1", "US14-AC2", "US14-AC3", "US14-AC4", "US14-AC5", "US14-AC6", "US14-AC7", "US14-AC8", "US14-AC9",
    "US15", "US15-AC1", "US15-AC2", "US15-AC3", "US15-AC4", "US15-AC5"
  ],
  "excluded": [
    { "id": "US15-AC4", "reason": "Quyền 'Xem danh sách học viên và hạng' chỉ xuất hiện trên màn role khi có endpoint learners (Unit Bảng xếp hạng, US12). Lát này đã đưa mã quyền vào tags của C-01 (ADR-002)" }
  ],
  "coverage": [
    { "id": "US14", "status": "OK", "target": "GamificationSettings" },
    { "id": "US14-AC1", "status": "OK", "target": "GamificationSettings, GamificationSettingsPage" },
    { "id": "US14-AC2", "status": "OK", "target": "GamificationSettingsPage" },
    { "id": "US14-AC3", "status": "OK", "target": "GamificationSettingsPage" },
    { "id": "US14-AC4", "status": "OK", "target": "GamificationSettingsPage" },
    { "id": "US14-AC5", "status": "OK", "target": "GamificationSettingsPage", "note": "Phần số campaign đang chạy ngoài lát (2.43 A4)" },
    { "id": "US14-AC6", "status": "OK", "target": "GamificationSettingsPage" },
    { "id": "US14-AC7", "status": "OK", "target": "GamificationSettingsPage, GamificationSettings", "note": "Lần đầu = visibility_first_enabled_at (ADR-005)" },
    { "id": "US14-AC8", "status": "OK", "target": "GamificationSettingsPage, GamificationSettingsOpsApi" },
    { "id": "US14-AC9", "status": "OK", "target": "GamificationSettingsPage" },
    { "id": "US15", "status": "OK", "target": "OpsAccessControl" },
    { "id": "US15-AC1", "status": "OK", "target": "OpsAccessControl, RolePermissionScreen" },
    { "id": "US15-AC2", "status": "OK", "target": "GamificationSettingsOpsApi, GamificationSettingsPage" },
    { "id": "US15-AC3", "status": "OK", "target": "GamificationSettingsOpsApi, GamificationSettingsPage" },
    { "id": "US15-AC5", "status": "OK", "target": "OpsPermissionCatalog, GamificationSettingsPage" }
  ]
}
