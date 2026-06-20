import streamlit as st

# ===================== 全新题库：时政公文混合卷，与测试一、二、四、五无任何重复题目 =====================
# 一、单选题 50道 法治时政+公文基础全新题目 每题1分
single_questions = [
    {
        "id": 1,
        "title": "新时代公安工作根本路线是？",
        "options": ["A.群众路线", "B.精英路线", "C.封闭执法路线", "D.简化执法路线"],
        "answer": "A",
        "analysis": "群众路线是公安工作根本路线，一切为了群众、依靠群众。"
    },
    {
        "id": 2,
        "title": "法定上行文不包含以下哪种？",
        "options": ["A.请示", "B.报告", "C.通告", "D.议案"],
        "answer": "C",
        "analysis": "通告属于下行文，面向社会公众发布事项。"
    },
    {
        "id": 3,
        "title": "2026年平安中国建设核心抓手是？",
        "options": ["A.基层矛盾源头化解", "B.取消社区警务站", "C.弱化全民普法宣传", "D.放宽电信诈骗管控"],
        "answer": "A",
        "analysis": "平安中国建设持续推进基层矛盾调解，从源头减少治安案件。"
    },
    {
        "id": 4,
        "title": "公文成文日期正确书写格式是？",
        "options": ["A.二零二六年六月一日", "B.2026.6.1", "C.2026年06月20日", "D.26/6/1"],
        "answer": "C",
        "analysis": "党政公文成文日期统一使用阿拉伯数字，完整书写年月日，月、日不足两位补0。"
    },
    {
        "id": 5,
        "title": "公安“酒城义警”机制主要作用是？",
        "options": ["A.群众协同开展治安巡逻", "B.替代民警独立办案", "C.开具行政处罚文书", "D.办理户籍业务审批"],
        "answer": "A",
        "analysis": "酒城义警为群防群治志愿队伍，仅协助巡逻宣传，无独立执法权限。"
    },
    {
        "id": 6,
        "title": "适用于表彰先进、批评错误、传达重要精神的文种是？",
        "options": ["A.通报", "B.通知", "C.函", "D.批复"],
        "answer": "A",
        "analysis": "通报三大用途：表彰先进、批评错误、传达重要工作精神与情况。"
    },
    {
        "id": 7,
        "title": "全面依法治国总目标是建设？",
        "options": ["A.社会主义法治国家", "B.经济强国", "C.文化大国", "D.军事强国"],
        "answer": "A",
        "analysis": "全面依法治国总目标：建设中国特色社会主义法治体系，建设社会主义法治国家。"
    },
    {
        "id": 8,
        "title": "不相隶属单位之间商洽工作应当使用？",
        "options": ["A.请示", "B.函", "C.报告", "D.命令"],
        "answer": "B",
        "analysis": "函适用于无上下级隶属关系单位商洽、询问、答复业务事项。"
    },
    {
        "id": 9,
        "title": "常态化反诈宣传重点针对受害高发群体是？",
        "options": ["A.老年人群、在校学生", "B.公职执法人员", "C.企业法务人员", "D.网络安全工程师"],
        "answer": "A",
        "analysis": "老年人、学生辨别能力较弱，是电信网络诈骗主要受害群体。"
    },
    {
        "id": 10,
        "title": "公文主送机关指的是？",
        "options": ["A.公文主要受理执行单位", "B.抄送备查单位", "C.文件印发单位", "D.档案保管单位"],
        "answer": "A",
        "analysis": "主送机关是公文直接承办、答复、落实工作的核心单位。"
    },
    {
        "id": 11,
        "title": "公安队伍教育整顿核心主题是？",
        "options": ["A.忠诚干净担当", "B.重业务轻政治", "C.简化纪律要求", "D.弱化思想建设"],
        "answer": "A",
        "analysis": "公安队伍建设要求打造忠诚、干净、担当的过硬警务队伍。"
    },
    {
        "id": 12,
        "title": "答复下级机关请示事项专用文种是？",
        "options": ["A.批复", "B.通知", "C.通报", "D.意见"],
        "answer": "A",
        "analysis": "批复唯一法定用途：专门答复下级单位上报的请示文件。"
    },
    {
        "id": 13,
        "title": "长江流域十年禁渔治安执法责任主体是？",
        "options": ["A.公安机关", "B.教育局", "C.财政局", "D.文旅局"],
        "answer": "A",
        "analysis": "非法捕捞、破坏水生生态治安案件由公安水上、治安部门管辖处置。"
    },
    {
        "id": 14,
        "title": "下列哪类公文不能同时抄送下级机关？",
        "options": ["A.请示", "B.决定", "C.通知", "D.通告"],
        "answer": "A",
        "analysis": "请示是上行文，严禁抄送下级单位，避免工作流程混乱。"
    },
    {
        "id": 15,
        "title": "总体国家安全观首要安全是？",
        "options": ["A.政治安全", "B.经济安全", "C.网络安全", "D.生态安全"],
        "answer": "A",
        "analysis": "政治安全是国家安全根本、首要保障任务。"
    },
    {
        "id": 16,
        "title": "向国内外宣布重要事项、法定事项文种是？",
        "options": ["A.公告", "B.通告", "C.通报", "D.通知"],
        "answer": "A",
        "analysis": "公告面向国内外发布；通告仅面向国内辖区社会群众。"
    },
    {
        "id": 17,
        "title": "基层“一村一辅警”制度核心目的是？",
        "options": ["A.下沉警务力量到农村一线", "B.替代村两委管理村务", "C.独立审批农村户籍", "D.单独办理刑事案件"],
        "answer": "A",
        "analysis": "一村一辅警推动警务下沉乡村，就近化解农村矛盾、开展治安防控。"
    },
    {
        "id": 18,
        "title": "公文附件说明标注位置在？",
        "options": ["A.正文下方成文日期之前", "B.版记抄送栏", "C.公文标题下方", "D.落款盖章之后"],
        "answer": "A",
        "analysis": "附件说明统一置于正文结束段落下方、成文日期上方。"
    },
    {
        "id": 19,
        "title": "打击跨境赌博工作牵头主管部门是？",
        "options": ["A.公安机关", "B.市场监管局", "C.农业农村局", "D.卫健委"],
        "answer": "A",
        "analysis": "跨境网络赌博属于涉网刑事犯罪，由公安网安、治安部门主导专项打击。"
    },
    {
        "id": 20,
        "title": "适用于记载会议主要情况、议定事项的文种是？",
        "options": ["A.纪要", "B.报告", "C.函", "D.批复"],
        "answer": "A",
        "analysis": "会议纪要用于完整记录会议决议、工作部署、协商内容。"
    },
    {
        "id": 21,
        "title": "法治建设十六字方针完整首句是？",
        "options": ["A.科学立法", "B.严格执法", "C.公正司法", "D.全民守法"],
        "answer": "A",
        "analysis": "十六字方针完整顺序：科学立法、严格执法、公正司法、全民守法。"
    },
    {
        "id": 22,
        "title": "下列文种属于平行文的是？",
        "options": ["A.函", "B.请示", "C.报告", "D.命令"],
        "answer": "A",
        "analysis": "函是典型平行文；请示、报告为上行；命令、通告为下行。"
    },
    {
        "id": 23,
        "title": "市夏季治安打击整治行动重点不包含？",
        "options": ["A.街头寻衅滋事整治", "B.夜市噪音扰民治理", "C.放宽酒驾查处力度", "D.景区人流安保"],
        "answer": "C",
        "analysis": "夏季行动持续严查酒驾醉驾，不会放宽路面管控。"
    },
    {
        "id": 24,
        "title": "公文标题中，发文机关与事由之间连接词是？",
        "options": ["A.关于", "B.对于", "C.有关", "D.就"],
        "answer": "A",
        "analysis": "标准标题格式：XX单位+关于+XX事由+的+文种。"
    },
    {
        "id": 25,
        "title": "公安辅警招录首要审查内容是？",
        "options": ["A.政治背景、无违法犯罪记录", "B.家庭资产收入", "C.社交平台粉丝数量", "D.机动车持有情况"],
        "answer": "A",
        "analysis": "辅警属于警务辅助人员，政治政审为第一准入门槛。"
    },
    {
        "id": 26,
        "title": "能够上行、下行、平行通用的公文文种是？",
        "options": ["A.意见", "B.请示", "C.批复", "D.通告"],
        "answer": "A",
        "analysis": "意见是唯一可向三级行文的法定公文，其余文种行文方向固定。"
    },
    {
        "id": 27,
        "title": "2026年基层网格化治理核心任务是？",
        "options": ["A.矛盾排查、信息采集、安全宣传", "B.简化网格取消巡查", "C.弱化群众走访", "D.仅处理经济纠纷"],
        "answer": "A",
        "analysis": "城乡网格三大基础工作：矛盾源头排查、基础信息采集、安全法治宣传。"
    },
    {
        "id": 28,
        "title": "公文附件名称书写规范正确的是？",
        "options": ["A.不加书名号、末尾无句号", "B.必须加《》书名号", "C.结尾添加句号分隔", "D.随意简写名称"],
        "answer": "A",
        "analysis": "附件名称纯文字表述，禁止书名号、顿号、句号等标点。"
    },
    {
        "id": 29,
        "title": "公安“三打一防”专项行动中“一防”指？",
        "options": ["A.社会治安防控", "B.防火专项检查", "C.防汛隐患排查", "D.防疫常态化管控"],
        "answer": "A",
        "analysis": "三打一防：打击侵财、打击黄赌、打击电诈，全域社会治安防控。"
    },
    {
        "id": 30,
        "title": "向上级机关反映困难、请求政策支持使用？",
        "options": ["A.请示", "B.报告", "C.函", "D.通报"],
        "answer": "A",
        "analysis": "有事需要上级批复、批准必须用请示；单纯汇报工作用报告。"
    },
    {
        "id": 31,
        "title": "总体国家安全观统筹发展和安全，底线思维是？",
        "options": ["A.防范化解各类安全风险", "B.重发展忽视安全", "C.弱化风险排查", "D.事后处置优先"],
        "answer": "A",
        "analysis": "国家安全工作坚持底线思维，提前防范化解各类潜在安全隐患。"
    },
    {
        "id": 32,
        "title": "用于发布规章制度、约束辖区公众行为用？",
        "options": ["A.通告", "B.请示", "C.报告", "D.函"],
        "answer": "A",
        "analysis": "通告面向社会发布管理规定、禁令、整治要求。"
    },
    {
        "id": 33,
        "title": "四川新时代“枫桥经验”落地载体是？",
        "options": ["A.村级调解室、社区警务站", "B.单一机关独自处置", "C.取消基层调解点位", "D.仅依靠法院诉讼"],
        "answer": "A",
        "analysis": "四川推广村级调解室、社区警务站，实现小事就地化解。"
    },
    {
        "id": 34,
        "title": "公文成文日期盖章标准是？",
        "options": ["A.骑年盖月", "B.压住年份不盖月份", "C.盖住完整正文文字", "D.斜向模糊加盖"],
        "answer": "A",
        "analysis": "公章端正居中，下压成文日期，骑住年份与月份。"
    },
    {
        "id": 35,
        "title": "2026全民普法宣传重点人群不含？",
        "options": ["A.公职人员、青少年、老年人", "B.在校中小学生", "C.已完成全部普法的成年公民无需再宣传", "D.农村留守群体"],
        "answer": "C",
        "analysis": "普法是常态化长期工作，全体公民持续开展法治宣传教育。"
    },
    {
        "id": 36,
        "title": "单位内部任免岗位、调整人员分工适用？",
        "options": ["A.通知", "B.批复", "C.函", "D.纪要"],
        "answer": "A",
        "analysis": "人事任免、岗位调整、内部事项传达统一使用通知。"
    },
    {
        "id": 37,
        "title": "网络舆情维稳属地责任主体是？",
        "options": ["A.属地公安机关、基层政府", "B.仅网络平台企业", "C.普通网民自行管控", "D.教育部门单独负责"],
        "answer": "A",
        "analysis": "网络谣言、涉本地舆情由属地公安、乡镇街道联合处置。"
    },
    {
        "id": 38,
        "title": "公文抄送机关的核心作用是？",
        "options": ["A.知晓文件内容备查", "B.牵头落实文件工作", "C.修改调整公文内容", "D.对文件作出批复答复"],
        "answer": "A",
        "analysis": "抄送单位仅知情存档，不承办、不批复、不执行主责工作。"
    },
    {
        "id": 39,
        "title": "市公安护航白酒产业治安工作不包含？",
        "options": ["A.酒厂周边巡逻防控", "B.打击酒类商标侵权", "C.取消厂区治安值守", "D.酒类运输道路保畅"],
        "answer": "C",
        "analysis": "酒城白酒产业安保是常态化重点警务工作，不会取消值守。"
    },
    {
        "id": 40,
        "title": "会议纪要正文核心内容不包含？",
        "options": ["A.参会人员、会议议题", "B.讨论发言要点", "C.议定落实事项", "D.参会人员私人薪资"],
        "answer": "D",
        "analysis": "会议纪要仅记录工作相关内容，不涉及员工私人薪酬信息。"
    },
    {
        "id": 41,
        "title": "公安工作“服务人民”宗旨落实抓手是？",
        "options": ["A.便民窗口、上门服务、延时办理", "B.增加办事门槛", "C.一次性告知缺失材料不补齐", "D.限制群众咨询渠道"],
        "answer": "A",
        "analysis": "持续优化公安政务服务，推出各类便民利民举措。"
    },
    {
        "id": 42,
        "title": "平行单位请求对方协助配合工作使用文种？",
        "options": ["A.函", "B.请示", "C.通知", "D.报告"],
        "answer": "A",
        "analysis": "无隶属单位求助、商洽、协调工作一律使用函。"
    },
    {
        "id": 43,
        "title": "2026全国打击养老诈骗专项行动核心目标？",
        "options": ["A.守住老年人财产安全", "B.放宽养老理财广告监管", "C.简化涉老案件核查", "D.降低宣传覆盖范围"],
        "answer": "A",
        "analysis": "养老诈骗专项以保护老年群众财产安全为核心目标。"
    },
    {
        "id": 44,
        "title": "上行文请示结尾规范结束语是？",
        "options": ["A.以上请示妥否，请批示", "B.尽快批准，多谢", "C.望立刻办理", "D.麻烦审批一下"],
        "answer": "A",
        "analysis": "请示结束语必须正式规范，杜绝口语化、网络化表述。"
    },
    {
        "id": 45,
        "title": "基层群防群治队伍不包含？",
        "options": ["A.义警、网格员、志愿者", "B.小区物业安保", "C.专职办案民警", "D.村社巡逻队员"],
        "answer": "C",
        "analysis": "正式民警属于专职执法力量，不属于群防群治志愿队伍。"
    },
    {
        "id": 46,
        "title": "公文标题中禁止出现的内容是？",
        "options": ["A.网络流行语、口语", "B.发文机关名称", "C.事由关键词", "D.法定文种"],
        "answer": "A",
        "analysis": "公文全程严谨正式，严禁网络热词、日常口语。"
    },
    {
        "id": 47,
        "title": "网络“断卡”行动主要打击对象是？",
        "options": ["A.出租出借银行卡、电话卡人员", "B.正常办理银行卡群众", "C.正规通讯营业厅", "D.合法电商商户"],
        "answer": "A",
        "analysis": "断卡行动针对两卡出售、出租、出借，斩断电诈资金通道。"
    },
    {
        "id": 48,
        "title": "用于传达上级单位部署、落实专项工作用？",
        "options": ["A.通知", "B.批复", "C.函", "D.公告"],
        "answer": "A",
        "analysis": "部署专项工作、传达上级指示最常用文种为通知。"
    },
    {
        "id": 49,
        "title": "总体国家安全观涵盖多少类安全领域？",
        "options": ["A.11类", "B.16类", "C.5类", "D.3类"],
        "answer": "B",
        "analysis": "总体国家安全观包含政治、国土、军事、经济、文化、社会、科技、网络、生态、资源、核、海外利益、生物、太空、深海、极地共16个领域。"
    },
    {
        "id": 50,
        "title": "公文版记必备两项要素是？",
        "options": ["A.抄送机关、印发机关与日期", "B.主送机关、标题", "C.附件、正文", "D.成文日期、落款"],
        "answer": "A",
        "analysis": "版记在文件最后，固定包含抄送栏、印发单位、印发时间。"
    }
]

# 二、全新多选题25道 15道新时政+10道新公文（和1/2/4/5无重复，每题2分）
multi_questions = [
    # ========== 时事政治15题 ==========
    {
        "id": 1,
        "title": "2026年公安基层治理重点工作包含？",
        "options": ["A.常态化矛盾纠纷排查化解", "B.全覆盖反诈宣传入户", "C.一村一辅警提质增效", "D.缩减社区巡逻频次"],
        "answer": ["A","B","C"],
        "analysis": "持续加密城乡巡逻防控，D不符合年度公安工作要求。"
    },
    {
        "id": 2,
        "title": "新时代公安队伍十六字方针完整内容有？",
        "options": ["A.对党忠诚", "B.服务人民", "C.执法公正", "D.纪律严明"],
        "answer": ["A","B","C","D"],
        "analysis": "十六字方针全部四项为公安队伍建设根本遵循。"
    },
    {
        "id": 3,
        "title": "平安四川建设核心抓手包含？",
        "options": ["A.网格化基层治理", "B.多元调解体系建设", "C.重点场所治安管控", "D.弱化群众群防力量"],
        "answer": ["A","B","C"],
        "analysis": "四川大力发展义警、网格员等群防力量，D错误。"
    },
    {
        "id": 4,
        "title": "当前全国公安重点打击涉民生犯罪类型有？",
        "options": ["A.电信网络诈骗", "B.养老、涉老诈骗", "C.食品药品安全犯罪", "D.民间小额亲友借贷"],
        "answer": ["A","B","C"],
        "analysis": "亲友正常小额借贷不属于违法犯罪打击范畴。"
    },
    {
        "id": 5,
        "title": "全面依法治国四项重点任务包含？",
        "options": ["A.科学立法", "B.严格执法", "C.公正司法", "D.全民守法"],
        "answer": ["A","B","C","D"],
        "analysis": "法治建设十六字方针四项内容全部正确。"
    },
    {
        "id": 6,
        "title": "市本地公安特色警务工作有？",
        "options": ["A.酒城义警群防机制", "B.长江禁渔水上巡查", "C.白酒产业治安护航", "D.撤销农村警务站点"],
        "answer": ["A","B","C"],
        "analysis": "持续增设农村警务室、辅警点位，D错误。"
    },
    {
        "id": 7,
        "title": "总体国家安全观统筹的重大关系包含？",
        "options": ["A.发展和安全", "B.传统与非传统安全", "C.自身与共同安全", "D.开放与安全"],
        "answer": ["A","B","C","D"],
        "analysis": "五大统筹全部涵盖题干四项内容。"
    },
    {
        "id": 8,
        "title": "辅警队伍规范化建设落地举措有？",
        "options": ["A.统一招录政审标准", "B.制式服装标识统一管理", "C.常态化业务法治培训", "D.赋予独立刑事办案审批权"],
        "answer": ["A","B","C"],
        "analysis": "辅警无独立刑事办案、案件审批权限。"
    },
    {
        "id": 9,
        "title": "乡村振兴配套治安保障工作包含？",
        "options": ["A.农村道路交通安全劝导", "B.农村禁毒反诈宣传", "C.邻里矛盾现场调解", "D.取消村级治安巡逻"],
        "answer": ["A","B","C"],
        "analysis": "农村常态化巡逻是乡村治安基础工作。"
    },
    {
        "id": 10,
        "title": "文明城市创建公安职责包含？",
        "options": ["A.规范车辆停放秩序", "B.整治噪音扰民摊点", "C.劝导不文明交通行为", "D.放任占道经营乱象"],
        "answer": ["A","B","C"],
        "analysis": "公安联合城管整治违规占道经营。"
    },
    {
        "id": 11,
        "title": "大型群众活动安保前置工作包含？",
        "options": ["A.制定专项安保预案", "B.现场人流分流规划", "C.消防隐患提前排查", "D.取消现场警力布置"],
        "answer": ["A","B","C"],
        "analysis": "大型活动必须足额布置安保警力。"
    },
    {
        "id": 12,
        "title": "打击整治养老诈骗工作举措包含？",
        "options": ["A.社区老年群体宣讲防诈", "B.查封虚假养老经营机构", "C.追缴诈骗涉案赃款", "D.默许虚假养老理财宣传"],
        "answer": ["A","B","C"],
        "analysis": "严厉查处各类虚假养老投资、理财广告宣传。"
    },
    {
        "id": 13,
        "title": "网络空间综合治理管控违法行为有？",
        "options": ["A.网络造谣、传谣", "B.人肉搜索曝光隐私", "C.出售公民手机号、身份证信息", "D.政府依法政务公开"],
        "answer": ["A","B","C"],
        "analysis": "法定政务信息公开属于合法合规行为。"
    },
    {
        "id": 14,
        "title": "全民普法宣传重点覆盖群体有？",
        "options": ["A.青少年学生", "B.城乡老年居民", "C.企业经营从业者", "D.公职执法人员"],
        "answer": ["A","B","C","D"],
        "analysis": "四类人群均为普法重点宣传对象。"
    },
    {
        "id": 15,
        "title": "常态化扫黑除恶持续整治领域包含？",
        "options": ["A.工程建材行业", "B.乡村基层宗族势力", "C.网络裸聊、催收黑灰产", "D.合法小微企业经营"],
        "answer": ["A","B","C"],
        "analysis": "合规小微企业正常经营不属于扫黑整治范围。"
    },
    # ========== 基础公文常识10道全新题目 ==========
    {
        "id": 16,
        "title": "下列属于党政机关法定公文文种的有？",
        "options": ["A.通知", "B.纪要", "C.报告", "D.小说"],
        "answer": ["A","B","C"],
        "analysis": "小说属于文学文体，不在15种法定公文清单内。"
    },
    {
        "id": 17,
        "title": "请示公文写作硬性规范要求有？",
        "options": ["A.严格一文一事", "B.只能单一主送机关", "C.结尾使用规范请示用语", "D.抄送下级单位同步知晓"],
        "answer": ["A","B","C"],
        "analysis": "上行请示禁止抄送下级机关。"
    },
    {
        "id": 18,
        "title": "通知文种适用工作场景包含？",
        "options": ["A.传达上级工作部署", "B.内部人事岗位任免", "C.告知全体参会事项", "D.向上级申请经费拨款"],
        "answer": ["A","B","C"],
        "analysis": "向上级申请经费必须使用请示，不可用通知。"
    },
    {
        "id": 19,
        "title": "公文版记板块标准组成要素有？",
        "options": ["A.抄送机关名称", "B.文件印发单位", "C.文件印发日期", "D.公文主送机关"],
        "answer": ["A","B","C"],
        "analysis": "主送机关放置在公文正文前，不属于版记内容。"
    },
    {
        "id": 20,
        "title": "典型下行法定公文包含？",
        "options": ["A.命令（令）", "B.决定", "C.批复", "D.报告"],
        "answer": ["A","B","C"],
        "analysis": "报告是下级向上级报送的上行文。"
    },
    {
        "id": 21,
        "title": "标准完整公文标题三大必备要素是？",
        "options": ["A.发文机关全称", "B.公文核心事由", "C.法定文种名称", "D.经办工作人员姓名"],
        "answer": ["A","B","C"],
        "analysis": "公文标题不标注经办人员、联系人信息。"
    },
    {
        "id": 22,
        "title": "通报公文三大分类为？",
        "options": ["A.表彰先进通报", "B.批评错误通报", "C.工作情况通报", "D.经费申请通报"],
        "answer": ["A","B","C"],
        "analysis": "无经费申请类通报，经费申请使用请示。"
    },
    {
        "id": 23,
        "title": "公文附件格式书写正确规则有？",
        "options": ["A.附件名称不加书名号", "B.附件单独另起一页编排", "C.附件与正文具备同等效力", "D.附件名称末尾添加句号"],
        "answer": ["A","B","C"],
        "analysis": "附件名称末尾不能加任何标点符号。"
    },
    {
        "id": 24,
        "title": "函的合法适用范围包含？",
        "options": ["A.不相隶属单位商洽业务", "B.互相咨询答复工作问题", "C.平级单位请求批准事项", "D.向下级单位下达强制命令"],
        "answer": ["A","B","C"],
        "analysis": "下达强制命令使用命令、决定文种，不用函。"
    },
    {
        "id": 25,
        "title": "党政公文行文规则明确禁止行为有？",
        "options": ["A.越级行文不抄送直接上级", "B.请示文件一文多事", "C.报告夹带请示请求事项", "D.同级职能部门联合行文"],
        "answer": ["A","B","C"],
        "analysis": "同级单位联合行文符合公文规范，不属于禁止行为。"
    }
]

# ===================== 页面初始化配置 =====================
st.set_page_config(page_title="测试三：时政公文专项冲刺卷", layout="wide")

# 独立会话存储，不和其他试卷数据冲突
def init_session():
    if "single_answer_record3" not in st.session_state:
        st.session_state.single_answer_record3 = {}
    if "multi_answer_record3" not in st.session_state:
        st.session_state.multi_answer_record3 = {}
    if "single_score3" not in st.session_state:
        st.session_state.single_score3 = 0
    if "multi_score3" not in st.session_state:
        st.session_state.multi_score3 = 0
    if "show_result3" not in st.session_state:
        st.session_state.show_result3 = False
    if "wrong_list3" not in st.session_state:
        st.session_state.wrong_list3 = {"single":[], "multi":[]}

init_session()

# 重置本套试卷函数
def reset_exam3():
    st.session_state.single_answer_record3 = {}
    st.session_state.multi_answer_record3 = {}
    st.session_state.single_score3 = 0
    st.session_state.multi_score3 = 0
    st.session_state.show_result3 = False
    st.session_state.wrong_list3 = {"single":[], "multi":[]}
    st.rerun()

# 页面头部标题与说明
st.title("测试三：时政公文专项冲刺卷")
st.markdown("""
### 试卷说明
1. 试卷总分100分：单选50道每题1分，多选25道每题2分
2. 题库构成：单选混合法治时政+公文基础；多选15道公安时政、10道公文格式文种
3. 全部题目与测试一、测试二、测试四、测试五无重复，专攻公文、时政易丢分模块
4. 判分规则：多选错选、漏选、多选均不得分；点击展开面板才可查看标准答案+解析
""")
st.button("一键重置本套试卷所有作答记录", on_click=reset_exam3, type="secondary")

# 渲染单选题区域
st.divider()
st.header("第一部分 单项选择题（共50题，每题1分，总分50分）")
single_correct = 0
for q in single_questions:
    qid = q["id"]
    st.subheader(f"第{qid}题：{q['title']}")
    # 修复：使用index=None 兼容低版本Streamlit，取消默认选中A
    select_opt = st.radio(f"第{qid}题选择答案", q["options"], key=f"s3_{qid}", horizontal=True, index=None)
    user_ans = select_opt.split(".")[0] if select_opt else ""
    st.session_state.single_answer_record3[qid] = user_ans

    # 默认折叠解析面板
    with st.expander("查看参考答案与解析", expanded=False):
        st.write(f"✅ 标准答案：{q['answer']}")
        st.write(f"📖 解析：{q['analysis']}")
        if user_ans == q["answer"]:
            st.success("作答正确，本题 +1分")
            single_correct += 1
        elif user_ans != "":
            st.error(f"你的答案：{user_ans}，回答错误，不得分")
            st.session_state.wrong_list3["single"].append(qid)
st.session_state.single_score3 = single_correct

# 渲染多选题区域
st.divider()
st.header("第二部分 多项选择题（共25题，每题2分，总分50分）")
multi_correct = 0
for q in multi_questions:
    qid = q["id"]
    st.subheader(f"第{qid}题：{q['title']}")
    # default=[] 多选默认空白，无需改动
    select_opts = st.multiselect(f"第{qid}题多选答案", q["options"], key=f"m3_{qid}", default=[])
    user_ans_list = [opt.split(".")[0] for opt in select_opts]
    st.session_state.multi_answer_record3[qid] = user_ans_list

    with st.expander("查看参考答案与解析", expanded=False):
        std_ans = q["answer"]
        st.write(f"✅ 标准答案：{','.join(std_ans)}")
        st.write(f"📖 解析：{q['analysis']}")
        if sorted(user_ans_list) == sorted(std_ans):
            st.success("作答完全正确，本题 +2分")
            multi_correct += 1
        elif len(user_ans_list) > 0:
            st.error(f"你的选择：{','.join(user_ans_list)}，漏选/错选/多选均不得分")
            st.session_state.wrong_list3["multi"].append(qid)
st.session_state.multi_score3 = multi_correct * 2

# 提交核算总分按钮
st.divider()
if st.button("提交本套试卷，核算总成绩", type="primary"):
    st.session_state.show_result3 = True

# 成绩单展示
if st.session_state.show_result3:
    total_score = st.session_state.single_score3 + st.session_state.multi_score3
    st.header("📊 测试三专项试卷成绩单")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("单选得分", value=f"{st.session_state.single_score3}/50")
    with col2:
        st.metric("多选得分", value=f"{st.session_state.multi_score3}/50")
    with col3:
        st.metric("试卷总分", value=f"{total_score}/100")

    st.subheader("错题汇总清单")
    wrong_single_ids = list(set(st.session_state.wrong_list3["single"]))
    wrong_multi_ids = list(set(st.session_state.wrong_list3["multi"]))
    st.write(f"单选错题题号：{wrong_single_ids if wrong_single_ids else '无错题'}")
    st.write(f"多选错题题号：{wrong_multi_ids if wrong_multi_ids else '无错题'}")
    st.info("可向上滑动页面，点击展开对应题号解析，巩固时政、公文考点")