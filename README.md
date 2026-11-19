# SHM Research Map

## Điểm đọc cho AI và cộng tác viên

Trong workspace nghiên cứu, bắt đầu với [Hồ sơ chương trình nghiên cứu](HO_SO_NGHIEN_CUU.md). Đây là hồ sơ hệ thống hóa duy nhất. File này ghi câu hỏi, phương pháp, bằng chứng và giới hạn của từng dự án, kèm đường dẫn tới tài liệu kỹ thuật và hướng phát triển tiếp. Hồ sơ này được lưu nội bộ cùng dữ liệu nghiên cứu.

Research programme map and journal publication progress for a set of structural health monitoring (SHM) papers, grouped by research line:

- **VS**: Virtual sensing
- **FT**: Integration and extreme fault tolerance
- **TL**: Topology, sensor localisation and restoration
- **OC**: Robust one-class detection against EOV
- **HP**: Input formulation, hyperparameter optimisation and transferability for supervised damage classification
- **WT**: Offshore wind turbine foundation OMA (setup consistency)
- **CW**: Temperature-conditioned deep learning for damage detection
- **CV**: Vision foundation models for structural surface damage
- **EL**: Equivalent linearization of nonlinear random vibration checked on measured data
- **ST**: Structural stability and out-of-plane buckling of through-arch bridges
- **PS**: Population-based SHM and cross-structure knowledge transfer
- **GN**: Graph neural networks for structural monitoring
- **WL**: Wind loading inferred from measured structural response
- **MO**: Multi-cage fish-farm mooring optimization
- **MS**: Maritime ship roll dynamics and early warning
- **PV**: Pavement engineering and green transportation infrastructure
- **CS**: Composite plate damage diagnosis

Optional semantic secondary labels (`up to 2 per paper, maximum 3 total labels including the primary code`, Title Case with true acronyms uppercase, stacked vertically without serial numbers; not needed for every paper) group cross-track domain and methodology clusters cleanly without renaming folders or consuming sequence numbers:
- **HDPE**: Aquaculture structures and HDPE marine fish cages (`VS13`, `VS14`, `VS17`, `MO1`)
- **Rail**: Railway bridge SHM and high-speed track inspection (`VS1`, `VS2`, `VS12`, `ST1`, `ST2`, `CV4`)
- **Wind**: Offshore and onshore wind turbine structures and monitoring (`VS15`, `WT1`, `OC4`, `GN1`)
- **Virtual Sensing**: Response recovery, state estimation, and digital twins (`VS1`–`VS4`, `VS8`–`VS13`, `VS15`, `VS17`, `GN2`)
- **Physics-ML**: Physics-guided/informed neural networks, residuals, Neural ODEs, and surrogates (`VS14`, `MS1`, `TL5`, `FT1`, `OC1`–`OC3`)
- **One-Class**: Unsupervised or label-free anomaly and damage detection (`OC1`–`OC4`, `FT1`, `FT3`, `TL1`, `CS1`)
- **Sensor Loss**: Tolerating, isolating, or recovering failed/offline sensors (`VS3`, `VS4`, `VS9`, `VS11`, `GN2`, `TL2`, `FT3`)

View the page: https://chungntu.github.io/shm-research-map/

`index.html` is the current public map. `build_public.py` copies the legacy HTML source only if it is present.
