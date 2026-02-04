## 一、基础设施服务列表

| 服务名称 | 服务访问地址 | 使用文档 |
| - | -| - |
|CLA|https://clasign.osinfra.cn/sign/690ca9ddf91c03dee6082ab1|[cla使用指南.md](./cla/cla使用指南.md)|
|机器人服务|NA|[robot使用指南.md](./robot/robot使用指南.md)|
|漏洞管理|NA|[漏洞管理使用指南.md](./cve-manager/manual.md)|
|会议中心|https://meeting.ascend.osinfra.cn/|[Ascend社区会议指南.md](./meeting/Ascend社区会议指南.md)|

## 二、组件仓库 CIE 支撑矩阵

**支撑范围说明**：您在参与开源贡献过程中，若遇到流水线、代码合入等问题，优先联系对应组件仓库的 CIE（持续集成工程师） 支撑处理：

- 编译、构建异常
- 静态代码检查结果异常
- 开发者测试（DT：包括单元测试UT和系统测试ST）任务执行异常
- 每日冒烟流水线（Nightly）执行异常
- 代码合入异常

| 组件          | 仓名                                                         | GITCODE账号                                           | 邮箱                  |
| ------------- | ------------------------------------------------------------ | ----------------------------------------------------- | --------------------- |
| MindStudio    | [MindStudio-Profiler-Tools-Interface](https://gitcode.com/Ascend/mspti) | [@overfitting_zh](https://gitcode.com/overfitting_zh) | zhanghan72@huawei.com |
|               | [MindStudio-Operator-Tools](https://gitcode.com/Ascend/msot) |                                                       |                       |
|               | [MindStudio-MemScope](https://gitcode.com/Ascend/msmemscope) |                                                       |                       |
|               | [MindStudio-Monitor](https://gitcode.com/Ascend/msmonitor)   |                                                       |                       |
|               | [MindStudio-Profiler](https://gitcode.com/Ascend/msprof)     |                                                       |                       |
|               | [MindStudio-Insight](https://gitcode.com/Ascend/msinsight)   |                                                       |                       |
|               | [MindStudio-ModelSlim](https://gitcode.com/Ascend/msmodelslim) |                                                       |                       |
|               | [MindStudio-Sanitizer](https://gitcode.com/Ascend/mssanitizer) |                                                       |                       |
|               | [MindStudio-Ops-Profiler](https://gitcode.com/Ascend/msopprof) |                                                       |                       |
|               | [MindStudio-Probe](https://gitcode.com/Ascend/msprobe)       |                                                       |                       |
|               | [MindStudio-Service-Profiler](https://gitcode.com/Ascend/msserviceprofiler) |                                                       |                       |
|               | [MindStudio-Ops-Common](https://gitcode.com/Ascend/msopcom)  |                                                       |                       |
|               | [MindStudio-Modeling](https://gitcode.com/Ascend/msmodeling) |                                                       |                       |
|               | [MindStudio-Profiler-Analyze](https://gitcode.com/Ascend/msprof-analyze) |                                                       |                       |
|               | [MindStudio-Debugger](https://gitcode.com/Ascend/msdebug)    |                                                       |                       |
|               | [MindStudio-Kernel-Performance-Prediction](https://gitcode.com/Ascend/mskpp) |                                                       |                       |
|               | [MindStudio-Tools-Extension-Library](https://gitcode.com/Ascend/mstx) |                                                       |                       |
|               | [MindStudio-Ops-Tuner](https://gitcode.com/Ascend/msoptuner) |                                                       |                       |
|               | [MindStudio-Ops-Generator](https://gitcode.com/Ascend/msopgen) |                                                       |                       |
|               | [MindStudio-Kernel-Launcher](https://gitcode.com/Ascend/mskl) |                                                       |                       |
| MindIE        | [MindIE-LLM](https://gitcode.com/Ascend/MindIE-LLM)          |                                                       |                       |
|               | [MindIE-SD](https://gitcode.com/Ascend/MindIE-SD)            |                                                       |                       |
|               | [MindIE-Turbo](https://gitcode.com/Ascend/MindIE-Turbo)      |                                                       |                       |
|               | [MindIE-Motor](https://gitcode.com/Ascend/MindIE-Motor)      |                                                       |                       |
|               | [MindIE-PyMotor](https://gitcode.com/Ascend/MindIE-PyMotor)  |                                                       |                       |
| MindSpeed     | [MindSpeed](https://gitcode.com/Ascend/MindSpeed)            |                                                       |                       |
|               | [MindSpeed-LLM](https://gitcode.com/Ascend/MindSpeed-LLM)    |                                                       |                       |
|               | [MindSpeed-MM](https://gitcode.com/Ascend/MindSpeed-MM)      |                                                       |                       |
|               | [MindSpeed-RL](https://gitcode.com/Ascend/MindSpeed-RL)      |                                                       |                       |
|               | [MindSpeed-Core-MS](https://gitcode.com/Ascend/MindSpeed-Core-MS) |                                                       |                       |
| PyTorch       | [pytorch](https://gitcode.com/Ascend/pytorch)                |                                                       |                       |
|               | [op-plugin](https://gitcode.com/Ascend/op-plugin)            |                                                       |                       |
|               | [ModelZoo-PyTorch](https://gitcode.com/Ascend/ModelZoo-PyTorch) |                                                       |                       |
|               | [torchair](https://gitcode.com/Ascend/torchair)              |                                                       |                       |
|               | [torch-mlir](https://gitcode.com/Ascend/torch-mlir)          |                                                       |                       |
|               | [Tensorpipe](https://gitcode.com/Ascend/Tensorpipe)          |                                                       |                       |
|               | [vision](https://gitcode.com/Ascend/vision)                  |                                                       |                       |
| MindCluster   | [MindCluster](https://gitcode.com/Ascend/mind-cluster)       |                                                       |                       |
|               | [MEF](https://gitcode.com/Ascend/MEF)                        |                                                       |                       |
|               | [OMSDK](https://gitcode.com/Ascend/OMSDK)                    |                                                       |                       |
|               | [memcache](https://gitcode.com/Ascend/memcache)              |                                                       |                       |
|               | [memfabric-hybrid](https://gitcode.com/Ascend/memfabric_hybrid) |                                                       |                       |
| MindSeriesSDK | [RecSDK](https://gitcode.com/Ascend/RecSDK)                  |                                                       |                       |
|               | [VisionSDK](https://gitcode.com/Ascend/VisionSDK)            |                                                       |                       |
|               | [AgentSDK](https://gitcode.com/Ascend/AgentSDK)              |                                                       |                       |
|               | [MultimodalSDK](https://gitcode.com/Ascend/MultimodalSDK)    |                                                       |                       |
|               | [DrivingSDK](https://gitcode.com/Ascend/DrivingSDK)          |                                                       |                       |
|               | [IndexSDK](https://gitcode.com/Ascend/IndexSDK)              |                                                       |                       |
|               | [RAGSDK](https://gitcode.com/Ascend/RAGSDK)                  |                                                       |                       |
|               | [MindInferenceService](https://gitcode.com/Ascend/MindInferenceService) |                                                       |                       |

