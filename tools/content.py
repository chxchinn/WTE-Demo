# -*- coding: utf-8 -*-
# Single source of truth for all copy: key -> (th, en, zh)
T = {}
def D(key, th, en, zh):
    assert key not in T, key
    T[key] = (th, en, zh)

# ---------- meta / nav ----------
D("meta.home", "WTE Corporation | พลังงานสะอาด วิศวกรรมที่ไว้วางใจได้",
  "WTE Corporation | Clean energy, engineered to be trusted",
  "WTE Corporation | 以值得信赖的工程成就清洁能源")
D("meta.about", "เกี่ยวกับเรา | WTE Corporation", "About Us | WTE Corporation", "关于我们 | WTE Corporation")
D("meta.business", "ธุรกิจของเรา | WTE Corporation", "Our Business | WTE Corporation", "我们的业务 | WTE Corporation")
D("meta.news", "ข่าวสารและกิจกรรม | WTE Corporation", "News & Activities | WTE Corporation", "新闻与活动 | WTE Corporation")
D("meta.contact", "ติดต่อเรา | WTE Corporation", "Contact | WTE Corporation", "联系我们 | WTE Corporation")

D("nav.home", "หน้าแรก", "Home", "首页")
D("nav.about", "รู้จัก WTE", "About WTE", "关于 WTE")
D("nav.business", "ธุรกิจของเรา", "Business", "业务")
D("nav.news", "ข่าวสาร", "News", "新闻")
D("nav.contact", "ติดต่อเรา", "Contact Us", "联系我们")
D("nav.skip", "ข้ามไปยังเนื้อหา", "Skip to content", "跳至正文")

# ---------- shared ----------
D("c.more", "ดูรายละเอียด", "Learn more", "了解详情")
D("c.contactus", "ติดต่อทีมงาน", "Talk to our team", "联系我们的团队")
D("c.slogan", "มุ่งสู่การเป็นบริษัทชั้นนำด้านวิศวกรรมในภูมิภาคอาเซียนอย่างยั่งยืน",
  "Our aim is to become a leading engineering company in ASEAN, sustainably.",
  "致力于成为东盟地区领先的工程企业，并实现可持续发展。")
D("c.company", "บริษัท ดับบลิวทีอี คอร์ปอเรชั่น จำกัด", "WTE Corporation Co., Ltd.", "WTE Corporation 有限公司")
D("c.regno", "นิติบุคคลเลขที่ 0105559156913", "Juristic person no. 0105559156913", "法人注册号 0105559156913")
D("c.hq", "สำนักงานใหญ่ (ที่อยู่สำหรับออกใบกำกับภาษีและใบเสร็จรับเงิน)", "Head office (tax invoice & receipt address)", "总部（税务发票及收据地址）")
D("c.hq.addr", "101/1 ซ.พระยาสุเรนทร์ 20 แขวงบางชัน เขตคลองสามวา กรุงเทพมหานคร 10510",
  "101/1 Soi Phraya Suren 20, Bang Chan, Khlong Sam Wa, Bangkok 10510, Thailand",
  "泰国曼谷 Khlong Sam Wa 区 Bang Chan 街道 Soi Phraya Suren 20，101/1 号，邮编 10510")
D("c.office", "สำนักงานปัจจุบัน (ที่อยู่สำหรับจัดส่งเอกสาร)", "Current office (document delivery address)", "现办公地址（文件寄送地址）")
D("c.office.addr", "77/5 หมู่บ้านดริสทริค เอกมัย-รามอินทรา ซ.รามอินทรา 40 แขวงนวลจันทร์ เขตบึงกุ่ม กรุงเทพมหานคร 10230",
  "77/5 Drist Village Ekkamai-Ramintra, Soi Ramintra 40, Nuan Chan, Bueng Kum, Bangkok 10230, Thailand",
  "泰国曼谷 Bueng Kum 区 Nuan Chan 街道 Ramintra 40 巷，Drist 村 Ekkamai-Ramintra，77/5 号，邮编 10230")
D("c.phone", "โทรศัพท์", "Phone", "电话")
D("c.email", "อีเมล", "Email", "电子邮件")
D("c.rights", "สงวนลิขสิทธิ์", "All rights reserved.", "版权所有。")
D("f.nav", "เมนู", "Menu", "菜单")
D("f.biz", "ธุรกิจ", "Business", "业务")
D("f.contact", "ติดต่อ", "Contact", "联系")
D("f.tag", "พลังงานทดแทน วิศวกรรม และเชื้อเพลิงจากขยะ เพื่ออนาคตที่ยั่งยืน",
  "Renewable energy, engineering and waste-derived fuel for a sustainable future.",
  "以可再生能源、工程和垃圾衍生燃料，共创可持续的未来。")

# ---------- home ----------
D("h.h1", "พลังงานสะอาด<br>ด้วยวิศวกรรมที่<em>ไว้วางใจได้</em>",
  "Clean energy, engineered to be <em>trusted</em>.",
  "以值得信赖的工程，<em>成就清洁能源</em>")
D("h.cta1", "ดูธุรกิจของเรา", "Explore our business", "了解我们的业务")

D("s.1", "2559", "2016", "2016")
D("s.1l", "ปีที่ก่อตั้งบริษัท (พ.ศ.)", "Year founded", "公司成立年份")
D("s.2l", "ปีประสบการณ์ในธุรกิจพลังงานทดแทน", "Years in renewable energy", "年可再生能源行业经验")
D("s.3l", "ปีประสบการณ์ของทีมผู้บริหาร", "Years of leadership experience", "年管理团队经验")
D("s.4l", "กลุ่มธุรกิจหลัก", "Core business groups", "大核心业务板块")

D("h.about.h", "จาก<em>ขยะ สู่พลังงาน</em> เพื่ออนาคตที่ยั่งยืนของอาเซียน",
  "From <em>waste to energy</em>, for a sustainable ASEAN",
  "变<em>废为能</em>，成就东盟的可持续未来")

D("h.w2e.p", "ประเทศไทยมีขยะมูลฝอยชุมชนราว 75,000 ตัน/วัน (กรมควบคุมมลพิษ, ปี 2560) และมีแนวโน้มเพิ่มขึ้นทุกปี การฝังกลบจึงไม่ใช่คำตอบอีกต่อไป WTE นำแนวคิดเศรษฐกิจหมุนเวียนมาเปลี่ยนขยะให้เป็นเชื้อเพลิงและพลังงาน",
  "Thailand generates roughly 75,000 tonnes of municipal solid waste per day (Pollution Control Department, 2017), and the volume keeps growing. Landfill is no longer the answer. WTE applies circular-economy thinking to turn waste into fuel and energy.",
  "泰国每天产生约 75,000 吨城市生活垃圾（污染控制厅，2017年数据），且逐年增长，填埋已不再是出路。WTE 以循环经济的理念，将垃圾转化为燃料与能源。")
D("h.w2e.1", "ลดขยะฝังกลบด้วยระบบเศรษฐกิจหมุนเวียน", "Cuts landfill through a circular economy", "以循环经济减少垃圾填埋")
D("h.w2e.2", "ไพโรไลซิสใช้ความร้อนย่อยสลายขยะพลาสติก ไม่ใช่การเผา", "Pyrolysis breaks plastic down with heat. It is not incineration.", "热解利用热量分解塑料垃圾，而非焚烧")
D("h.w2e.3", "น้ำมันบางส่วนหมุนเวียนกลับมาเป็นพลังงานให้เครื่องจักร", "Part of the oil is recycled back to power the machine", "部分产出的油回用为设备的能源")

D("h.goal.h", "เป้าหมาย<em>ที่เรามุ่งไป</em>", "The goals <em>we are working toward</em>", "我们<em>努力的目标</em>")
D("h.goal.y", "ปี", "yrs", "年")
D("h.goal.1", "ก้าวขึ้นเป็นหนึ่งในผู้นำด้านวิศวกรรมในภูมิภาคอาเซียน เริ่มจากประเทศไทย ด้วยงานวิศวกรรม จัดซื้อ ติดตั้ง และบริหารโครงการแบบ EPCM (Engineering Procurement Construction Management)",
  "Become one of ASEAN's engineering leaders, starting in Thailand, through EPCM: Engineering, Procurement, Construction Management.",
  "以泰国为起点，通过 EPCM（工程、采购、施工管理）模式，成为东盟地区的工程领军企业之一。")
D("h.goal.2", "บริหารจัดการธุรกิจพลังงานทดแทนทุกประเภท ด้วยบุคลากรที่มีประสบการณ์และคุณภาพ",
  "Manage every type of renewable energy business with experienced, high-quality people.",
  "凭借经验丰富的优秀人才，管理各类可再生能源业务。")

D("h.ms.h", "เหตุการณ์<em>สำคัญ</em>", "Company <em>milestones</em>", "公司<em>大事记</em>")
D("ms.y1", "พ.ศ. 2559", "2016", "2016年")
D("ms.y2", "พ.ศ. 2562", "2019", "2019年")
D("ms.y3", "พ.ศ. 2566", "2023", "2023年")
D("ms.1h", "ก่อตั้งบริษัท", "Company founded", "公司成立")
D("ms.1p", "ก่อตั้งโดยการรวมตัวของกลุ่มผู้เชี่ยวชาญที่มีความรู้และประสบการณ์จากหลากหลายสาขา เพื่อรองรับงานรับเหมาติดตั้งแบบเบ็ดเสร็จ (EPC) ในโครงการพลังงานทดแทน",
  "Founded by specialists from many disciplines to deliver turnkey EPC contracting for renewable energy projects.",
  "由多个专业领域的专家联合创办，承接可再生能源项目的 EPC 交钥匙工程。")
D("ms.2h", "เปลี่ยนผู้ถือหุ้นและชื่อบริษัท", "New shareholders and company name", "股东变更与公司更名")
D("ms.2p", "ผู้ถือหุ้นมีมติเปลี่ยนแปลงผู้ถือหุ้น แต่งตั้งผู้บริหารชุดใหม่ และเปลี่ยนชื่อเป็น บริษัท ดับบลิวทีอี คอร์ปอเรชั่น จำกัด",
  "Shareholders resolved to change the shareholding, appoint a new management team and rename the company WTE Corporation Co., Ltd.",
  "股东决议变更股权结构、任命新一届管理层，并将公司更名为 WTE Corporation 有限公司。")
D("ms.3h", "ขยายการลงทุนพลังงานทดแทน", "Expanding renewable energy investment", "扩大可再生能源投资")
D("ms.3p", "วางแผนขยายการลงทุนด้านเชื้อเพลิงจากขยะชุมชน พลังงานแสงอาทิตย์ และอนุรักษ์พลังงาน มีมติเข้าซื้อกิจการโรงไฟฟ้าขยะชุมชน จีเด็ค จำกัด และเพิ่มทุนจดทะเบียนใหม่ 450 ล้านบาท",
  "Planned expansion into municipal-waste fuel, solar and energy conservation. Resolved to acquire G-Dec Co., Ltd. (จีเด็ค), a municipal-waste power plant and raise registered capital by THB 450 million.",
  "计划扩大城市垃圾燃料、太阳能及节能领域的投资；决议收购城市垃圾发电厂 จีเด็ค（G-Dec）有限公司，并新增注册资本 4.5 亿泰铢。")

D("h.cta.h", "มาสร้างโครงการที่ยั่งยืนครั้งต่อไปด้วยกัน", "Let's build your next sustainable project.", "携手打造您的下一个可持续项目")
D("h.cta.p", "คุยกับ WTE เกี่ยวกับความต้องการของโครงการคุณ", "Talk to WTE about your project requirements.", "与 WTE 探讨您的项目需求。")

# ---------- about ----------
D("a.h1", "เกี่ยวกับ WTE", "About WTE", "关于 WTE")
D("a.sub", "ผู้เชี่ยวชาญด้านพลังงานทางเลือกครบวงจร ที่ผสานวิศวกรรมเข้ากับความยั่งยืน",
  "Integrated alternative-energy specialists who combine engineering with sustainability.",
  "将工程能力与可持续发展相结合的一站式替代能源专家。")
D("a.story.h", "เรื่องราว<em>ของเรา</em>", "Our <em>story</em>", "我们的<em>故事</em>")
D("a.story.p1", "บริษัท ดับบลิวทีอี คอร์ปอเรชั่น จำกัด (WTE) ก่อตั้งเมื่อปี พ.ศ. 2559 โดยการรวมตัวของกลุ่มผู้เชี่ยวชาญที่มีความรู้ ความสามารถ และประสบการณ์จากหลากหลายสาขาวิชาชีพ ดำเนินธุรกิจพลังงานทางเลือกครบวงจร ครอบคลุมงานออกแบบติดตั้งทางวิศวกรรม การพัฒนาโครงการพลังงานทดแทนและการอนุรักษ์พลังงาน การจัดหาอุปกรณ์เทคโนโลยี และเครื่องจักรกลนวัตกรรมขั้นสูง (High Innovative Technology) รวมถึงงานออกแบบและติดตั้งด้านพลังงานและสาธารณูปโภค (Energy & Utility)",
  "WTE Corporation Co., Ltd. was founded in 2016 by specialists with knowledge and experience across many professions. We run a full-service alternative-energy business: engineering design and installation, renewable energy and energy-conservation project development, supply of technology and high-innovation machinery, and design and installation for energy and utilities.",
  "WTE Corporation 有限公司成立于2016年，由来自多个专业领域、经验丰富的专家共同创办。我们提供一站式替代能源服务：工程设计与安装、可再生能源与节能项目开发、技术设备及高端创新机械的供应，以及能源与公用事业的设计与安装。")
D("a.story.p2", "ผู้บริหารมีประสบการณ์ในธุรกิจการเงิน เครื่องจักรกล สิ่งแวดล้อม และพลังงานทดแทน รวมกว่า 20 ปี บริษัทพัฒนาธุรกิจเข้าสู่การบริหารจัดการขยะแบบกำจัดขยะเป็นศูนย์ (Zero Waste Management) และขยายการลงทุนในพลังงานทดแทน มุ่งเน้นเชื้อเพลิงจากขยะชุมชน พลังงานแสงอาทิตย์ และงานอนุรักษ์พลังงาน",
  "Our executives bring more than 20 years of experience in finance, machinery, environment and renewable energy. The company has moved into Zero Waste Management and expanded its renewable investments, focusing on municipal-waste fuel, solar power and energy conservation.",
  "我们的管理层在金融、机械、环保和可再生能源领域拥有20多年的经验。公司已拓展至“零废弃”垃圾管理，并扩大可再生能源投资，重点布局城市垃圾燃料、太阳能和节能业务。")

D("a.groups.h", "กลุ่มธุรกิจ<em>ของ WTE</em>", "WTE's <em>business groups</em>", "WTE 的<em>业务板块</em>")
D("a.g1", "กลุ่มธุรกิจพลังงานทดแทนและอนุรักษ์พลังงาน", "Renewable Energy & Energy Conservation", "可再生能源与节能板块")
D("a.g1.1", "ผลิตและแปรรูปเชื้อเพลิงจากขยะชุมชน", "Production and processing of fuel from municipal waste", "城市垃圾燃料的生产与加工")
D("a.g1.2", "ผลิตและจำหน่ายน้ำมันจากขยะพลาสติก", "Production and sale of oil from plastic waste", "塑料垃圾制油的生产与销售")
D("a.g1.3", "ผลิตและจำหน่ายเม็ดพลาสติกจากขยะพลาสติก", "Production and sale of plastic pellets from plastic waste", "塑料垃圾再生塑料粒的生产与销售")
D("a.g1.4", "ไฟฟ้าพลังงานแสงอาทิตย์", "Solar power", "太阳能发电")
D("a.g1.5", "บริหารจัดการพลังงานและนวัตกรรม", "Energy management and innovation", "能源管理与创新")
D("a.g2", "กลุ่มธุรกิจบริหารจัดการน้ำเสีย", "Wastewater Management", "废水管理板块")
D("a.g3", "กลุ่มธุรกิจสาธารณูปโภคและสื่อสารโทรคมนาคม", "Utilities & Telecommunications", "公用事业与通信板块")

D("a.team.h", "ทีม<em>ผู้บริหาร</em>", "Executive <em>team</em>", "<em>管理团队</em>")
D("p.n1", "นายธีรศักดิ์ สุวรรณยศ", "Mr. Teerasak Suwannayos", "นายธีรศักดิ์ สุวรรณยศ")
D("p.r1", "ประธานกรรมการบริหาร", "Executive Chairman", "执行董事长")
D("p.n2", "นายอรรถวิทย์ วรรณศรี", "Mr. Attawit Wannasri", "นายอรรถวิทย์ วรรณศรี")
D("p.r2", "กรรมการผู้จัดการและกรรมการบริหาร", "Managing Director and Executive Director", "董事总经理兼执行董事")
D("p.n3", "ดร.ประพันธ์ พิกุลทอง", "Dr. Prapan Pikulthong", "ดร.ประพันธ์ พิกุลทอง")
D("p.r3", "รองกรรมการผู้จัดการใหญ่ สายงานปฏิบัติการ", "Deputy Managing Director, Operations", "副总经理，运营")
D("p.n4", "นายพลาย ภิรมย์", "Mr. Plai Phirom", "นายพลาย ภิรมย์")
D("p.r4", "รองกรรมการผู้จัดการใหญ่ สายงานพัฒนาองค์กรอย่างยั่งยืนและเศรษฐกิจเพื่อชุมชน", "Deputy Managing Director, Sustainable Development & Community Economy", "副总经理，可持续发展与社区经济")
D("p.n5", "น.ส.ณัชชารีย์ ไชยสัตย์", "Ms. Natcharee Chaisat", "น.ส.ณัชชารีย์ ไชยสัตย์")
D("p.r5", "รองกรรมการผู้จัดการใหญ่ สายงานบริหารศักยภาพองค์กร", "Deputy Managing Director, Organizational Capability", "副总经理，组织能力管理")
D("p.n6", "นายสุไลมาน สุทธิพันธ์", "Mr. Sulaiman Suthipan", "นายสุไลมาน สุทธิพันธ์")
D("p.r6", "รองกรรมการผู้จัดการใหญ่ สายงานบัญชีและการเงิน", "Deputy Managing Director, Accounting & Finance", "副总经理，会计与财务")
D("p.n7", "ดร.ภูเทพ คอนท้วม", "Dr. Phuthep Konthuam", "ดร.ภูเทพ คอนท้วม")
D("p.r7", "รองกรรมการผู้จัดการใหญ่ สายงานพัฒนาธุรกิจ", "Deputy Managing Director, Business Development", "副总经理，业务发展")

# ---------- business ----------
D("b.h1", "ธุรกิจของเรา", "Our Business", "我们的业务")
D("b.sub", "พลังงานทดแทน เชื้อเพลิง รีไซเคิล และวิศวกรรม EPC ครบในที่เดียว",
  "Renewable energy, fuel, recycling and EPC engineering, all in one place.",
  "可再生能源、燃料、回收与 EPC 工程，一站式解决。")
D("b.nav1", "พลังงานทดแทน", "Renewable energy", "可再生能源")
D("b.nav2", "เชื้อเพลิง", "Fuel", "燃料")
D("b.nav3", "เม็ดพลาสติกรีไซเคิล", "Recycled plastic", "再生塑料")
D("b.nav4", "วิศวกรรม EPC", "EPC engineering", "EPC 工程")

D("b1.h", "พลังงานทดแทนและ<em>เทคโนโลยีอนุรักษ์พลังงาน</em>", "Renewable energy & <em>energy-saving technology</em>", "可再生能源与<em>节能技术</em>")
D("b1.msw.h", "โรงคัดแยกขยะชุมชน (MSW Plant)", "Municipal solid waste (MSW) plant", "城市生活垃圾分拣厂（MSW）")
D("b1.msw.p", "Waste to Energy คือแนวคิดผลิตพลังงานจากขยะ ที่ได้รับความสนใจมากขึ้นเมื่อปัญหาขยะล้นเมืองต้องการทางออกเร่งด่วน การฝังกลบไม่ตอบโจทย์อีกต่อไป การนำเศรษฐกิจหมุนเวียน (Circular Economy) มาใช้ ด้วยนวัตกรรมและเทคโนโลยี ทำให้ขยะกลายเป็นเชื้อเพลิงผลิตไฟฟ้าใน ‘โรงไฟฟ้าพลังงานขยะ’ ซึ่งอยู่ในแผนพัฒนาพลังงานทดแทนและพลังงานทางเลือกของประเทศ พ.ศ. 2558–2579",
  "Waste to Energy, generating power from waste, is gaining attention as overflowing waste calls for urgent solutions. Landfill no longer answers the problem. Applying the circular economy with innovation and technology turns waste into fuel for electricity at waste-to-energy power plants, a priority in Thailand's 2015–2036 alternative energy development plan.",
  "垃圾发电（Waste to Energy）正随着“垃圾围城”问题日益受到关注。填埋已无法解决问题，借助创新与技术引入循环经济，让垃圾成为“垃圾发电厂”的发电燃料——这也是泰国2015–2036年替代能源发展规划的重点方向。")
D("b1.solar.h", "พลังงานแสงอาทิตย์ (Solar Power Plant)", "Solar power", "太阳能发电")
D("b1.solar.p", "กระแสโลกร้อนทำให้หลายประเทศใช้มาตรการลดก๊าซเรือนกระจกเป็นเงื่อนไขทางการค้า ผู้ประกอบการไทยจึงสนใจพลังงานสะอาดมากขึ้น เพราะช่วยรักษาสิ่งแวดล้อม สร้างภาพลักษณ์ที่ดีต่อคู่ค้า และลดต้นทุนการดำเนินธุรกิจ ระบบเซลล์แสงอาทิตย์แบ่งเป็น 3 ระบบ",
  "As global warming drives trade measures to cut greenhouse gases, Thai businesses are turning to clean energy. It protects the environment, builds a better image with partners and lowers operating costs. Solar PV comes in three system types.",
  "随着全球变暖，一些国家将减排措施作为贸易门槛，泰国企业也越来越关注清洁能源——它既保护环境，又提升合作伙伴心中的形象，还能降低运营成本。光伏发电系统分为三类。")
D("sol.1", "ระบบอิสระ", "Stand-alone", "离网系统")
D("sol.1h", "PV Stand-alone System", "PV Stand-alone System", "光伏离网系统")
D("sol.1p", "ออกแบบสำหรับพื้นที่ไม่มีระบบสายส่งไฟฟ้า แผงเซลล์แสงอาทิตย์จ่ายไฟให้โหลดโดยตรง ส่วนไฟที่เหลือชาร์จเข้าแบตเตอรี่ผ่านตัวควบคุมการชาร์จ",
  "Designed for areas without a power grid. Panels feed loads directly, and surplus power charges batteries through a solar charge controller.",
  "专为无电网覆盖的区域设计。光伏板直接为负载供电，多余电力通过充电控制器存入蓄电池。")
D("sol.2", "ต่อกับระบบจำหน่ายไฟฟ้า", "Grid-connected", "并网系统")
D("sol.2h", "PV Grid-connected System", "PV Grid-connected System", "光伏并网系统")
D("sol.2p", "ใช้ในพื้นที่ที่มีโครงข่ายไฟฟ้า แผงเซลล์แสงอาทิตย์ต่อกับอินเวอร์เตอร์ แปลงไฟฟ้ากระแสตรงเป็นกระแสสลับเพื่อใช้งาน และเชื่อมต่อกับระบบจำหน่ายของการไฟฟ้าได้",
  "Used where a grid is available. Panels connect to an inverter that converts DC to AC for use, and can tie into the utility's distribution network.",
  "适用于有电网覆盖的区域。光伏板连接逆变器，将直流电转换为交流电供负载使用，并可接入电网。")
D("sol.3", "แบบผสมผสาน", "Hybrid", "混合系统")
D("sol.3h", "PV Hybrid System", "PV Hybrid System", "光伏混合系统")
D("sol.3p", "ผลิตไฟฟ้าร่วมกับแหล่งอื่น เช่น เครื่องกำเนิดไฟฟ้า กังหันลม และแบตเตอรี่ ผ่านอินเวอร์เตอร์แบบผสมผสาน และยังเชื่อมต่อกับระบบของการไฟฟ้าได้",
  "Generates power together with other sources such as generators, wind turbines and batteries through a hybrid inverter, and can still connect to the utility grid.",
  "与发电机、风力发电机和蓄电池等其他电源协同发电，通过混合逆变器供电，同样可并入电网。")
D("b1.led.h", "หลอดไฟ LED", "LED lighting", "LED 照明")
D("b1.led.p", "หลอด LED ใช้พลังงานน้อยกว่าหลอดไส้ถึง 5 เท่า คุ้มค่า และช่วยลดภาวะโลกร้อน ข้อดีอื่น ๆ ได้แก่",
  "LED lamps use up to 5 times less energy than incandescent bulbs, saving money and helping slow global warming. Other benefits:",
  "LED 灯比白炽灯节能多达5倍，经济实惠，有助于缓解全球变暖。其他优点包括：")
D("led.1", "ถนอมสายตา ให้แสงสีขาว เหมาะกับงานที่ต้องการคุณภาพแสงสูง", "Easy on the eyes, white light suited to high-quality lighting needs", "护眼，白光，适合对光质要求高的场景")
D("led.2", "อายุการใช้งานยาวนาน ไม่พังง่าย ทนการกัดกร่อน", "Long life, durable, corrosion resistant", "寿命长、不易损坏、耐腐蚀")
D("led.3", "ย่อยสลายได้เร็ว ช่วยรักษาสิ่งแวดล้อม", "Breaks down faster, better for the environment", "降解更快，更利于环保")
D("led.4", "ไม่มีรังสี UV และอินฟราเรดที่เป็นอันตรายต่อผิวหนัง", "No harmful UV or infrared radiation", "无有害紫外线和红外线辐射")
D("led.5", "ไม่ดึงดูดแมลง", "Does not attract insects", "不招引昆虫")

D("b2.h", "ธุรกิจ<em>เชื้อเพลิง</em>", "The <em>fuel</em> business", "<em>燃料</em>业务")
D("b2.p", "WTE จัดหา แปรรูป และจำหน่ายเชื้อเพลิง RDF และเชื้อเพลิงรูปแบบอื่นสำหรับโรงไฟฟ้าพลังงานหมุนเวียนทั้งในและต่างประเทศ รวมถึงส่งเสริมการปลูกพืชพลังงานและคัดแยกขยะชุมชน เพื่อเสริมความมั่นคงด้านเชื้อเพลิงให้โรงไฟฟ้าของกลุ่มบริษัทและลูกค้าภายนอก",
  "WTE sources, processes and sells RDF and other fuels for renewable power plants in Thailand and abroad. We also promote energy crops and municipal waste sorting to secure fuel supply for our group's plants and external customers.",
  "WTE 为国内外可再生能源电厂提供 RDF 及其他燃料的采购、加工和销售，同时推广能源作物种植和城市垃圾分拣，保障集团电厂及外部客户的燃料供应。")
D("b2.crop.h", "พืชพลังงาน", "Energy crops", "能源作物")
D("b2.crop.p", "พืชพลังงานคือพืชที่นำส่วนต่าง ๆ มาผลิตพลังงานทดแทนน้ำมันปิโตรเลียม แบ่งเป็น 3 ชนิด การปลูกพืชพลังงานยังช่วยสร้างงานและรายได้ให้เกษตรกร",
  "Energy crops are plants whose parts can produce energy to replace petroleum oil. There are three types, and growing them also creates jobs and income for farmers.",
  "能源作物是可将其各部分用于生产、替代石油的植物，分为三类。种植能源作物还能为农民创造就业和收入。")
D("crop.1", "พืชน้ำมัน", "Oil crops", "油料作物")
D("crop.1p", "ปาล์มน้ำมัน ถั่วเหลือง มะพร้าว ทานตะวัน ละหุ่ง สบู่ดำ", "Oil palm, soybean, coconut, sunflower, castor, jatropha", "油棕、大豆、椰子、向日葵、蓖麻、麻疯树")
D("crop.2", "พืชแป้งและน้ำตาล", "Starch & sugar crops", "淀粉与糖类作物")
D("crop.2p", "ข้าวโพด ข้าว ข้าวฟ่าง มันสำปะหลัง อ้อย แก่นทานตะวัน", "Maize, rice, sorghum, cassava, sugarcane, Jerusalem artichoke", "玉米、水稻、高粱、木薯、甘蔗、菊芋")
D("crop.3", "มวลชีวภาพ", "Biomass", "生物质")
D("crop.3p", "เศษซากพืชจากการเกษตรและอุตสาหกรรมเกษตร", "Residues from farming and agro-industry", "农业及农产品加工业的残余物")
D("b2.rdf.h", "เชื้อเพลิงขยะ RDF", "RDF fuel", "RDF 垃圾衍生燃料")
D("b2.rdf.p", "WTE จัดหาและแปรรูปเชื้อเพลิง RDF ให้โรงไฟฟ้า จากเศษวัสดุเหลือใช้ทางการเกษตรของเกษตรกรในพื้นที่ในแต่ละฤดูกาล และส่งเสริมให้ชุมชนปลูกพืชพลังงาน ในแต่ละปีบริหารเชื้อเพลิงรวมหลายแสนตัน เพื่อให้โรงไฟฟ้ามีเชื้อเพลิงเพียงพอ ด้วยต้นทุนที่เหมาะสม",
  "WTE sources and processes RDF for power plants from local farmers' agricultural residues each season, and encourages communities to grow energy crops. Each year we manage several hundred thousand tonnes of fuel so plants have enough supply at a reasonable cost.",
  "WTE 为电厂采购并加工 RDF，原料来自当地农户每季的农业剩余物，并鼓励社区种植能源作物。每年管理的燃料达数十万吨，确保电厂在合理成本下获得充足燃料。")
D("b2.py.h", "น้ำมันจากระบบไพโรไลซิส", "Oil from pyrolysis", "热解制油")
D("py.1", "ลำเลียงขยะพลาสติกทุกประเภท เช่น ถุง พลาสติกห่อหุ้ม และบรรจุภัณฑ์ ลงในเครื่องนวัตกรรมไพโรไลซิส (Pyrolysis Machine)",
  "Plastic waste of every kind, such as bags, wrapping and packaging, is fed into the Pyrolysis Machine.",
  "各类塑料垃圾（如塑料袋、包装膜、包装容器）被送入热解设备（Pyrolysis Machine）。")
D("py.2", "เครื่องให้ความร้อนเพื่อย่อยสลาย เกิดควันและก๊าซไวไฟ นี่ไม่ใช่การเผา ก๊าซที่ได้ถูกรวบรวมไปใช้เป็นความร้อนในกระบวนการ",
  "The machine heats the plastic to break it down into smoke and flammable gas. This is not burning. The gas is collected and reused as process heat.",
  "设备加热使塑料分解，产生烟气与可燃气体。这不是焚烧，所得气体被回收用作工艺热源。")
D("py.3", "ควันผ่านระบบกลั่นและเปลี่ยนเป็นของเหลว กลายเป็นน้ำมันชีวภาพ", "The vapour passes through a distillation system and condenses into liquid bio-oil.", "烟气经冷凝蒸馏系统转化为液体，即生物油。")
D("py.4", "น้ำมันบางส่วนหมุนเวียนกลับมาเป็นพลังงานให้เครื่อง จึงไม่ต้องใช้น้ำมันเชื้อเพลิงจากภายนอก",
  "Part of the oil is cycled back to power the machine, so no external fuel oil is needed.",
  "部分油品回用为设备能源，因此无需外购燃油。")

D("b3.h", "เม็ดพลาสติก<em>จากการรีไซเคิล</em>", "Plastic pellets <em>from recycling</em>", "<em>再生</em>塑料粒")
D("b3.p", "WTE จัดหาและแปรรูปเม็ดพลาสติกรีไซเคิล ทางเลือกวัตถุดิบที่เป็นมิตรต่อสิ่งแวดล้อมและประหยัดต้นทุนกว่าเม็ดพลาสติกบริสุทธิ์ ผลิตตามสเปกที่ลูกค้าต้องการ ได้ผลิตภัณฑ์ที่แข็งแรง ทนทาน และช่วยลดปัญหาขยะพลาสติก",
  "WTE sources and processes recycled plastic pellets, an eco-friendly raw material that costs less than virgin pellets. We produce to the customer's specification for strong, durable products that also help reduce plastic waste.",
  "WTE 采购并加工再生塑料粒，这是一种环保且成本低于原生塑料粒的原料。可按客户规格生产，产品坚固耐用，同时有助于减少塑料垃圾。")
D("b3.use", "เหมาะกับผลิตภัณฑ์อย่าง", "Suitable for products such as", "适用于以下产品")
D("use.1", "เครื่องใช้ไฟฟ้า", "Electrical appliances", "电器设备")
D("use.2", "อุปกรณ์ยานยนต์", "Automotive parts", "汽车配件")
D("use.3", "กระเป๋า", "Bags", "箱包")
D("use.4", "ถุง", "Plastic bags", "塑料袋")
D("use.5", "ขวดพลาสติก", "Plastic bottles", "塑料瓶")

D("b4.h", "ธุรกิจ<em>วิศวกรรม EPC</em>", "<em>EPC</em> engineering", "<em>EPC</em> 工程业务")
D("b4.p1", "WTE ให้บริการวิศวกรรมครบวงจร เน้นออกแบบและก่อสร้างโรงไฟฟ้าขยะ RDF โรงคัดแยกและแปรรูปขยะ RDF รวมถึงงานก่อสร้างทั่วไป ในรูปแบบ EPC: Engineering, Procurement and Construction",
  "WTE provides full-service engineering with a focus on designing and building RDF waste power plants and RDF sorting and processing plants, as well as general construction, under the EPC model: Engineering, Procurement and Construction.",
  "WTE 提供一站式工程服务，重点为 RDF 垃圾电厂、RDF 垃圾分拣与加工厂的设计与建设，以及一般建筑工程，采用 EPC（设计、采购、施工）模式。")
D("b4.p2", "งาน EPC คือหัวใจของการดำเนินโรงไฟฟ้าให้ต่อเนื่องและมีประสิทธิภาพ ประสบการณ์ด้านเทคโนโลยีก่อสร้าง การเดินเครื่อง และการบำรุงรักษา ทำให้ WTE เข้าใจการเลือกเทคโนโลยีและการจัดหาเครื่องจักรที่ทำงานร่วมกันได้ดี และได้รับความไว้วางใจให้รับเหมาแบบครบวงจร (Turnkey) อย่างต่อเนื่อง",
  "EPC is at the heart of keeping a power plant running continuously and efficiently. Our experience in construction technology, operation and maintenance lets us choose technology and source equipment that work well together, and customers keep trusting us with full turnkey contracts.",
  "EPC 是电厂持续高效运营的核心。凭借在施工技术、设备运行和维护方面的经验，我们能选择合适的技术并采购可协同工作的设备，持续获得客户信任，承接交钥匙总承包工程。")
D("b4.1", "ออกแบบ", "Engineering", "设计")
D("b4.2", "จัดหาเครื่องจักร", "Procurement", "采购")
D("b4.3", "ก่อสร้าง", "Construction", "施工")
D("b4.4", "บริหารโครงการ", "Project management", "项目管理")

# ---------- governance ----------
D("g.csr.h", "ความรับผิดชอบ<em>ต่อสังคม</em>", "Corporate <em>social responsibility</em>", "企业<em>社会责任</em>")
D("g.csr.p", "WTE มีนโยบายดำเนินธุรกิจด้วยความรับผิดชอบต่อสังคม (CSR) บนพื้นฐานของความยั่งยืนทางธุรกิจ เพื่อประโยชน์ต่อผู้มีส่วนได้ส่วนเสียทุกฝ่าย และใช้หลักการกำกับดูแลกิจการที่ดีเป็นแนวทางพัฒนาองค์กร มุ่งเป็นองค์กรที่ช่วยยกระดับชุมชน เศรษฐกิจรอบชุมชน และความยั่งยืนด้านสังคมและสิ่งแวดล้อมในระยะยาว",
  "WTE conducts business with social responsibility (CSR) grounded in business sustainability, for the benefit of all stakeholders, and uses good corporate governance as its guide. We aim to help uplift communities, local economies and long-term social and environmental sustainability.",
  "WTE 以企业可持续发展为基础，践行社会责任（CSR），造福所有利益相关方，并以良好的公司治理指引企业发展，致力于提升社区、周边经济以及长期的社会与环境可持续性。")
D("g.csr.sub", "CSR in Process: ความรับผิดชอบต่อสังคมและสิ่งแวดล้อมในกระบวนการปฏิบัติงาน", "CSR in Process: social and environmental responsibility in our operations", "CSR in Process：在运营过程中履行社会与环境责任")
D("g.p1", "การดูแลรักษาสิ่งแวดล้อม", "Caring for the environment", "保护环境")
D("g.p2", "การปฏิบัติต่อแรงงานอย่างเป็นธรรม", "Fair treatment of labour", "公平对待劳工")
D("g.p3", "นโยบายต่อต้านการคอร์รัปชั่น", "Anti-corruption policy", "反腐败政策")

D("g.sus.h", "นโยบาย<em>ความยั่งยืน</em>", "Our <em>sustainability</em> policy", "<em>可持续发展</em>政策")
D("g.sus.p", "วิสัยทัศน์ของ WTE คือการเป็นโรงไฟฟ้าพลังงานสะอาดต้นแบบของโลก ที่รับผิดชอบต่อสิ่งแวดล้อม สังคม และผู้ถือหุ้น โดยพัฒนาและขยายกิจการบนหลักความยั่งยืน ภายใต้จรรยาบรรณทางธุรกิจและการกำกับดูแลกิจการที่ดี เพื่อสร้างคุณค่าให้ผู้มีส่วนได้เสียตลอดห่วงโซ่ธุรกิจ รวมถึงชุมชนและกลุ่มผู้เปราะบางรอบโรงไฟฟ้า",
  "WTE's vision is to be a model clean-power producer for the world, responsible to the environment, society and shareholders. We grow on the principles of sustainability, under a business code of conduct and good governance, creating value for stakeholders across the value chain, including communities and vulnerable groups around our plants.",
  "WTE 的愿景是成为世界清洁电力的典范，对环境、社会和股东负责。我们以可持续发展原则开展并扩大业务，遵循商业行为准则和良好治理，为整条价值链上的利益相关方——包括电厂周边的社区与弱势群体——创造价值。")
D("g.pol1", "เศรษฐกิจและธรรมาภิบาล", "Economy & governance", "经济与治理")
D("g.pol2", "สิ่งแวดล้อม", "Environment", "环境")
D("g.pol3", "สังคม", "Society", "社会")
D("g.pol.p", "นโยบายการบริหารจัดการความยั่งยืนใช้บังคับกับกลุ่มบริษัท ตามประเด็นสำคัญ 3 ด้าน", "Our sustainability management policy applies across the group, covering three key areas.", "可持续发展管理政策适用于整个集团，涵盖三大重点领域。")

D("g.org.h", "โครงสร้าง<em>การบริหารองค์กร</em>", "Corporate <em>management structure</em>", "<em>公司管理架构</em>")
D("g.org.p", "โครงสร้างการบริหารของ WTE ตั้งแต่คณะกรรมการ ผู้บริหารสูงสุด ไปจนถึงสายงานหลักทั้ง 5", "How WTE is organised: from the board and committees to the CEO and five main divisions.", "WTE 的组织架构：从董事会与各委员会、首席执行官到五大业务条线。")

D("g.ir.h", "ข้อมูล<em>นักลงทุน</em>", "Investor <em>information</em>", "<em>投资者</em>信息")
D("g.ir.p", "WTE ประกอบธุรกิจโดยการถือหุ้น (Holding Company) มุ่งลงทุนในธุรกิจหลัก คือการผลิตและจำหน่ายไฟฟ้าจากขยะชุมชนทั้งในและต่างประเทศ ด้วยเทคโนโลยีที่ทันสมัย มีประสิทธิภาพ และเป็นมิตรต่อสิ่งแวดล้อม",
  "WTE operates as a holding company. Its core business is the production and sale of electricity from municipal waste in Thailand and abroad, using modern, efficient and environmentally friendly technology.",
  "WTE 以控股公司形式运营，核心业务是利用现代、高效且环保的技术，在国内外生产和销售城市垃圾发电。")
D("g.ir.1", "ธุรกิจหลัก", "Core business", "核心业务")
D("g.ir.1p", "ไฟฟ้าจากขยะชุมชน", "Power from municipal waste", "城市垃圾发电")
D("g.ir.2", "เพิ่มทุนจดทะเบียนใหม่ (แผน พ.ศ. 2566)", "New registered capital (2023 plan)", "新增注册资本（2023年计划）")
D("g.ir.2p", "450 ล้านบาท", "THB 450 million", "4.5 亿泰铢")
D("g.ir.3", "ก่อตั้งเมื่อ", "Established", "成立时间")
D("g.ir.3p", "พ.ศ. 2559", "2016", "2016年")
D("g.ir.note", "สอบถามข้อมูลนักลงทุนได้ที่", "For investor enquiries, contact", "投资者咨询请联系")

# ---------- news ----------
D("n.h1", "ข่าวสารและกิจกรรม", "News & Activities", "新闻与活动")
D("n.sub", "ความเคลื่อนไหวล่าสุดและกิจกรรมของ WTE", "Latest updates and activities from WTE.", "WTE 的最新动态与活动。")
D("n.tag", "กิจกรรม", "Activity", "活动")
D("n.date", "6 กุมภาพันธ์ 2566", "6 February 2023", "2023年2月6日")
D("n.title", "ดูงานโรงคัดแยกฯ ห้วยกระเจา อบต.เวียง อ.ฝาง จ.เชียงใหม่", "Study visit: Huai Krachao sorting plant, Wiang Subdistrict Administrative Organization, Fang, Chiang Mai", "考察参观：清迈府 Fang 县 Wiang 镇 Huai Krachao 垃圾分拣厂")

# ---------- contact ----------
D("ct.h1", "ติดต่อเรา", "Contact us", "联系我们")
D("ct.sub", "ปรึกษาโครงการ สอบถามบริการ หรือร่วมงานกับ WTE", "Discuss a project, ask about our services, or join WTE.", "项目咨询、服务查询，或加入 WTE。")
D("ct.info", "ข้อมูลการติดต่อ", "Get in touch", "联系方式")
D("ct.form.h", "ส่งข้อความถึงเรา", "Send us a message", "给我们留言")
D("ct.name", "ชื่อ-นามสกุล", "Full name", "姓名")
D("ct.email", "อีเมล", "Email address", "电子邮箱")
D("ct.phone", "โทรศัพท์", "Phone", "电话")
D("ct.subject", "หัวข้อ", "Subject", "主题")
D("ct.msg", "ข้อความ", "Message", "留言内容")
D("ct.send", "ส่งข้อความ", "Send message", "发送留言")
D("ct.note", "เมื่อกดส่ง ระบบจะเปิดโปรแกรมอีเมลของคุณพร้อมข้อความที่กรอกไว้ เพื่อส่งถึง info@wtecorporation.com",
  "Sending opens your email app with the message filled in, addressed to info@wtecorporation.com.",
  "点击发送后，将打开您的邮件程序并带有已填写的内容，收件人为 info@wtecorporation.com。")
D("ct.map", "เปิดแผนที่", "Open map", "打开地图")
D("ct.join", "ร่วมงานกับเรา", "Careers", "加入我们")
D("ct.join.p", "สนใจร่วมงานกับ WTE ส่งประวัติและความสนใจมาที่อีเมลด้านบน", "Interested in joining WTE? Send your CV and interests to the email above.", "有意加入 WTE？请将简历和意向发送至上述邮箱。")

# org chart
D("g.o.board", "ประธานกรรมการบริหาร", "Executive Chairman", "执行董事长")
D("g.o.c1", "คณะกรรมการกำกับกิจการที่ดี", "Corporate Governance Committee", "公司治理委员会")
D("g.o.c2", "คณะกรรมการบริหารความเสี่ยง", "Risk Management Committee", "风险管理委员会")
D("g.o.c3", "คณะกรรมการสรรหาและกำหนดค่าตอบแทน", "Nomination & Remuneration Committee", "提名与薪酬委员会")
D("g.o.c4", "คณะกรรมการตรวจสอบ", "Audit Committee", "审计委员会")
D("g.o.ceo", "ประธานเจ้าหน้าที่บริหาร", "Chief Executive Officer", "首席执行官")
D("g.o.s1", "ฝ่ายกฎหมายและบริหารสัญญา", "Legal & Contract Management", "法务与合同管理部")
D("g.o.s2", "ที่ปรึกษาชำนาญการพิเศษ", "Special Advisor", "特别顾问")
D("g.o.s3", "ฝ่ายตรวจสอบภายในองค์กร", "Internal Audit", "内部审计部")
D("g.o.s4", "ฝ่ายเลขานุการ", "Secretariat", "秘书处")
D("g.d1", "สายงานพัฒนาธุรกิจ", "Business Development", "业务发展")
D("g.d1.1", "ฝ่ายพลังงานทดแทนและอนุรักษ์พลังงาน", "Renewable Energy & Conservation", "可再生能源与节能部")
D("g.d1.2", "ฝ่ายวิจัยพัฒนานวัตกรรมและเทคโนโลยี", "Innovation & Technology R&D", "创新与技术研发部")
D("g.d1.3", "ฝ่ายโครงการพิเศษ", "Special Projects", "特别项目部")
D("g.d2", "สายงานปฏิบัติการ", "Operations", "运营")
D("g.d2.1", "ฝ่ายวิศวกรรม", "Engineering", "工程部")
D("g.d2.2", "ฝ่ายปฏิบัติการผลิตและซ่อมบำรุง", "Production & Maintenance", "生产与维护部")
D("g.d2.3", "ฝ่ายบริการและควบคุมโครงการ", "Project Service & Control", "项目服务与控制部")
D("g.d3", "สายงานบัญชีและการเงิน", "Accounting & Finance", "会计与财务")
D("g.d3.1", "ฝ่ายการเงินและวิเคราะห์การลงทุน", "Finance & Investment Analysis", "财务与投资分析部")
D("g.d3.2", "ฝ่ายงานบัญชี", "Accounting", "会计部")
D("g.d3.3", "ฝ่ายงานจัดซื้อ", "Procurement", "采购部")
D("g.d4", "สายงานพัฒนาองค์กรอย่างยั่งยืน", "Sustainable Development", "可持续发展")
D("g.d4.1", "ฝ่ายการตลาดและบริการหลังการขาย", "Marketing & After-sales", "市场与售后服务部")
D("g.d4.2", "ฝ่ายกลยุทธ์องค์กร", "Corporate Strategy", "企业战略部")
D("g.d4.3", "ฝ่ายพัฒนาชุมชนอย่างยั่งยืน", "Sustainable Community Development", "可持续社区发展部")
D("g.d5", "สายงานบริหารศักยภาพองค์กร", "Organizational Capability", "组织能力管理")
D("g.d5.1", "ฝ่ายทรัพยากรบุคคล", "Human Resources", "人力资源部")
D("g.d5.2", "ฝ่ายธุรการ", "Administration", "行政部")

# ---------- restructure (SCG-style storytelling) ----------
D("nav.sus", "ความยั่งยืน", "Sustainability", "可持续发展")
D("nav.inv", "นักลงทุน", "Investors", "投资者")
D("meta.sus", "ความยั่งยืน | WTE Corporation", "Sustainability | WTE Corporation", "可持续发展 | WTE Corporation")
D("meta.inv", "นักลงทุนสัมพันธ์ | WTE Corporation", "Investor Relations | WTE Corporation", "投资者关系 | WTE Corporation")
D("c.read", "อ่านต่อ", "Read more", "阅读更多")
D("c.all", "ดูทั้งหมด", "View all", "查看全部")
D("h.st.h", "เรื่องราว<em>จากงานของเรา</em>", "Stories <em>from our work</em>", "<em>我们的</em>业务故事")
D("h.st.p", "สามเส้นทางที่เปลี่ยนสิ่งเหลือใช้ให้เป็นพลังงาน", "Three paths that turn what is left over into energy.", "三条将废弃物转化为能源的路径。")
D("st.1h", "จากขยะพลาสติก สู่น้ำมัน", "From plastic waste to oil", "从塑料垃圾到油品")
D("st.1p", "เครื่องไพโรไลซิสใช้ความร้อนย่อยสลายพลาสติกทุกประเภท ไม่ใช่การเผา แล้วนำน้ำมันบางส่วนกลับมาเป็นพลังงานให้เครื่อง", "A pyrolysis machine breaks down every type of plastic with heat, not fire, and feeds part of the oil back to power itself.", "热解设备用热量而非明火分解各类塑料，并将部分油品回用为设备自身的能源。")
D("st.2h", "จากเศษวัสดุเกษตร สู่เชื้อเพลิง RDF", "From farm residue to RDF fuel", "从农业残余物到 RDF 燃料")
D("st.2p", "จัดหาเศษวัสดุเหลือใช้จากเกษตรกรในพื้นที่ และส่งเสริมการปลูกพืชพลังงาน สร้างรายได้ให้ชุมชนและความมั่นคงด้านเชื้อเพลิงให้โรงไฟฟ้า", "We source leftover agricultural material from local farmers and promote energy crops, creating income for communities and fuel security for power plants.", "我们从当地农户处采购农业剩余物并推广能源作物，为社区创造收入，也为电厂保障燃料供应。")
D("st.3h", "จากแสงแดด สู่ไฟฟ้า", "From sunlight to electricity", "从阳光到电力")
D("st.3p", "ออกแบบและติดตั้งระบบโซลาร์ทั้งแบบอิสระ ต่อกับระบบจำหน่ายไฟฟ้า และแบบผสมผสาน ช่วยลดต้นทุนและสร้างภาพลักษณ์ที่ดีต่อคู่ค้า", "We design and install stand-alone, grid-connected and hybrid solar systems that cut costs and build a better image with partners.", "设计并安装离网、并网及混合光伏系统，降低成本，并提升在合作伙伴心中的形象。")
D("h.news.h", "ข่าว<em>ล่าสุด</em>", "<em>Latest</em> news", "<em>最新</em>动态")
D("h.doc.h", "เอกสาร<em>เผยแพร่</em>", "Key <em>documents</em>", "<em>重要</em>文件")
D("d.1", "โปรไฟล์บริษัท (Company Profile)", "Company Profile", "公司简介")
D("d.2", "รายงานประจำปี", "Annual report", "年度报告")
D("d.3", "รายงานความยั่งยืน", "Sustainability report", "可持续发展报告")
D("d.soon", "เร็ว ๆ นี้", "Coming soon", "即将发布")
D("s.h1", "ความยั่งยืน", "Sustainability", "可持续发展")
D("s.sub", "ดำเนินธุรกิจอย่างรับผิดชอบต่อสังคมและสิ่งแวดล้อม", "Doing business responsibly toward society and the environment.", "以负责任的方式经营，兼顾社会与环境。")
D("i.h1", "นักลงทุนสัมพันธ์", "Investor Relations", "投资者关系")
D("i.sub", "ข้อมูลองค์กร การกำกับดูแล และเอกสารเผยแพร่สำหรับผู้ถือหุ้นและนักลงทุน", "Corporate information, governance and key documents for shareholders and investors.", "面向股东与投资者的公司信息、治理与重要文件。")
D("i.gov.h", "การกำกับ<em>ดูแลกิจการ</em>", "Corporate <em>governance</em>", "<em>公司治理</em>")
D("i.gov.p", "คณะกรรมการ 4 ชุดภายใต้ประธานกรรมการบริหาร ตามโครงสร้างองค์กรของ WTE", "Four committees sit under the Executive Chairman in WTE's organisational structure.", "WTE 的组织架构中，执行董事长之下设有四个委员会。")
D("i.doc.p", "เอกสารสำหรับนักลงทุนจะเผยแพร่ในส่วนนี้ ระหว่างนี้สอบถามได้ที่ info@wtecorporation.com", "Investor documents will be published here. In the meantime, write to info@wtecorporation.com.", "投资者文件将在此发布。在此期间，欢迎发送邮件至 info@wtecorporation.com 咨询。")

# ---------- projects page + UI refresh ----------
D("nav.projects", "ผลงาน", "Projects", "项目")
D("meta.proj", "ผลงานและไฮไลต์ | WTE Corporation", "Projects & Highlights | WTE Corporation", "项目与亮点 | WTE Corporation")
D("pj.h1", "ผลงานและไฮไลต์", "Projects & Highlights", "项目与亮点")
D("pj.sub", "งานวิศวกรรมเพื่ออนาคตที่ยั่งยืน", "Engineering solutions for a sustainable future", "助力可持续未来的工程方案")
D("pj.feat.h", "โรงงาน RDF <em>แบบครบวงจร</em>", "Integrated <em>RDF facility</em>", "一体化 <em>RDF 工厂</em>")
D("pj.feat.t", "จากขยะ สู่ทรัพยากรที่มีค่า", "From waste to valuable resources", "变废为宝")
D("pj.feat.s", "ภาพรวมกระบวนการ (ภาพประกอบ)", "Process overview (illustrative)", "流程概览（示意）")
D("pj.f1", "คัดแยกและจัดการขยะ", "Waste processing", "垃圾分拣与处理")
D("pj.f2", "เตรียมเชื้อเพลิง", "Fuel preparation", "燃料制备")
D("pj.f3", "นำทรัพยากรกลับมาใช้", "Resource recovery", "资源回收")
D("pj.ph", "ภาพประกอบ — รอรูปจริงของ WTE", "Image placeholder — WTE photo to come", "图片占位 — 待补充 WTE 实景照片")
D("pj.exp.h", "สำรวจ<em>ประเภทงานของเรา</em>", "Explore <em>our work</em>", "了解<em>我们的业务类别</em>")
D("pj.exp.p", "หมวดงานที่ WTE ให้บริการ", "The categories of work WTE delivers", "WTE 提供的业务类别")
D("pj.note", "ตัวอย่างหมวดงานเพื่อการออกแบบ ยังไม่ใช่รายการโครงการจริง ผลงานที่ตรวจสอบแล้วจะเพิ่มเข้ามาภายหลัง", "Sample work categories for design review, not verified project records. Confirmed projects will be added later.", "此处为设计示例类别，并非已核实的项目记录；经确认的项目将陆续添加。")
D("pj.fall", "ทั้งหมด", "All", "全部")
D("pj.frdf", "RDF", "RDF", "RDF")
D("pj.fepcm", "EPCM", "EPCM", "EPCM")
D("pj.frec", "รีไซเคิลและเชื้อเพลิง", "Recycling & Fuels", "回收与燃料")
D("pj.c1", "โรงแปรรูปเชื้อเพลิง RDF", "RDF processing facility", "RDF 加工厂")
D("pj.c2", "งานวิศวกรรมโรงงานอุตสาหกรรม", "Industrial plant engineering", "工业厂房工程")
D("pj.c3", "โรงคัดแยกและนำวัสดุกลับมาใช้", "Material recovery facility", "物料回收分拣厂")
D("pj.c4", "ระบบเตรียมเชื้อเพลิง", "Fuel preparation system", "燃料制备系统")
D("pj.c5", "งานก่อสร้างและติดตั้ง", "Construction & installation", "施工与安装")
D("pj.c6", "เชื้อเพลิงทางเลือก", "Alternative fuel solutions", "替代燃料解决方案")
D("bc.home", "หน้าแรก", "Home", "首页")
D("h.cta.btn2", "ดูผลงาน", "See our work", "查看项目")

# ---------- per-service project pages ----------
D("c.viewwork", "ดูผลงาน", "View projects", "查看项目")
D("pj.back", "ผลงานทั้งหมด", "All projects", "全部项目")
D("pj.svc", "รายละเอียดบริการ", "Service details", "服务详情")
D("pj.other", "ผลงานหมวดอื่น", "Other project categories", "其他项目类别")
D("pj.list", "รายการผลงาน", "Project list", "项目列表")
D("pj.empty.h", "กำลังรวบรวมผลงานในหมวดนี้", "We are compiling projects for this category", "本类别的项目正在整理中")
D("pj.empty.p", "ผลงานที่ตรวจสอบแล้วจะเผยแพร่ที่นี่ หากต้องการดูตัวอย่างงานหรือข้อมูลโครงการ ติดต่อทีมงานได้โดยตรง", "Verified projects will be published here. For project examples or details, please contact our team directly.", "经核实的项目将在此发布。如需了解项目案例或详情，欢迎直接联系我们的团队。")
D("pj.s.energy.h", "ผลงานด้าน<em>พลังงานทดแทน</em>", "<em>Renewable energy</em> projects", "<em>可再生能源</em>项目")
D("pj.s.energy.p", "โรงคัดแยกขยะชุมชน ระบบโซลาร์ และเทคโนโลยีเพื่อการอนุรักษ์พลังงาน", "Municipal waste sorting plants, solar systems and energy-saving technology.", "城市垃圾分拣厂、光伏系统与节能技术。")
D("pj.s.fuel.h", "ผลงานด้าน<em>เชื้อเพลิง</em>", "<em>Fuel</em> projects", "<em>燃料</em>项目")
D("pj.s.fuel.p", "เชื้อเพลิง RDF พืชพลังงาน และน้ำมันจากระบบไพโรไลซิส", "RDF fuel, energy crops and oil from pyrolysis.", "RDF 燃料、能源作物与热解制油。")
D("pj.s.recycling.h", "ผลงานด้าน<em>รีไซเคิล</em>", "<em>Recycling</em> projects", "<em>回收</em>项目")
D("pj.s.recycling.p", "เม็ดพลาสติกรีไซเคิลที่ผลิตตามสเปกของลูกค้า", "Recycled plastic pellets produced to customer specifications.", "按客户规格生产的再生塑料粒。")
D("pj.s.engineering.h", "ผลงานด้าน<em>วิศวกรรม EPC</em>", "<em>EPC engineering</em> projects", "<em>EPC 工程</em>项目")
D("pj.s.engineering.p", "ออกแบบ จัดหา และก่อสร้างโรงไฟฟ้าขยะ RDF และโรงคัดแยกแปรรูป", "Design, procurement and construction of RDF waste power plants and sorting and processing plants.", "RDF 垃圾电厂及分拣加工厂的设计、采购与施工。")

# ---------- design pass ----------

# ---------- services focus (official 3 business groups) ----------
D("h.svc.h", "ธุรกิจที่ <em>WTE ให้บริการ</em>", "Services <em>WTE provides</em>", "<em>WTE 提供的</em>业务")
D("h.svc.p", "3 กลุ่มธุรกิจหลัก ครอบคลุมพลังงาน น้ำ และสาธารณูปโภค", "Three core business groups across energy, water and utilities.", "三大核心业务板块，涵盖能源、水务与公用事业。")
D("svc.ask", "สอบถามรายละเอียดบริการ", "Ask about this service", "咨询服务详情")
