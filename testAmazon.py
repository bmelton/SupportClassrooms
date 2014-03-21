#!/bin/env python

urls = (
    "http://www.amazon.com/Brother-Feature-Rich-Built-In-Auto-Size-Buttonholes/dp/B000JQM1DE/ref=zg_bs_arts-crafts_1",
    "http://www.amazon.com/Silhouette-Cameo-Replacement-Cutting-Mat/dp/B005VPVW3I/ref=zg_bs_arts-crafts_5",
    "http://www.amazon.com/Fiskars-12-27457097-Gel-48-Piece-Value/dp/B000S161FO/ref=zg_bs_arts-crafts_6",
    "http://www.amazon.com/Fiskars-12-27457097-Gel-48-Piece-Value/dp/B000S161FO/ref=zg_bs_arts-crafts_6",
    "http://www.amazon.com/Clover-Wonder-Clips-Per-Pack/dp/B004ZKPX8A/ref=zg_bs_arts-crafts_10",
    "http://www.amazon.com/Pro-18-Piece-Sketch-Draw-Pencil/dp/B000HTBBO8/ref=zg_bs_arts-crafts_14",
    "http://www.amazon.com/dp/B007HCCNJU/ref=sa_menu_kdptq",
    "http://www.amazon.com/dp/B00B1TEIRU?pf_rd_p=1631445482&pf_rd_s=merchandised-search-4&pf_rd_t=101&pf_rd_i=7682631011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=0JR80BS2Z9QEAP292R1V&ref_=acs_ux_fbw_0_47832910",
    "http://www.amazon.com/dp/B00B1TGMIS?pf_rd_p=1631228882&pf_rd_s=merchandised-search-6&pf_rd_t=101&pf_rd_i=7682631011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=0JR80BS2Z9QEAP292R1V&ref_=acs_ux_fbw_1_47832910",
    "http://www.amazon.com/dp/B00B1TFWSY?pf_rd_p=1631229382&pf_rd_s=merchandised-search-7&pf_rd_t=101&pf_rd_i=7682631011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=0JR80BS2Z9QEAP292R1V&ref_=acs_ux_fbw_1_47832910",
    "http://www.amazon.com/gp/product/B007F9XJDY/ref=trdrt_tipp_dp_titl_tipp_ce_2226766011?pf_rd_p=1444018862&pf_rd_s=center-7&pf_rd_t=101&pf_rd_i=2226766011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=0TVH3C486NEDHTHA5HA5",
    "http://www.amazon.com/Televisions-Video/b/ref=sa_menu_tv?ie=UTF8&node=1266092011",
    "http://www.amazon.com/TCL-LE50UHDE5691-50-Inch-Ultra-120Hz/dp/B00ES5Q6E2/ref=lp_8323768011_1_3?s=electronics&ie=UTF8&qid=1395351891&sr=1-3",
    "http://www.amazon.com/dp/B00BCGROG4/ref=gb1h_img_c-3_4802_73c9bfd7?smid=ATVPDKIKX0DER&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=101&pf_rd_s=center-3&pf_rd_r=1ATEMRNW5HZADSBN4D1Z&pf_rd_i=3079714011&pf_rd_p=1714304802",
    "http://www.amazon.com/dp/B00ES5YZD6/ref=gb1h_img_c-3_4802_ca93fb1e?smid=ATVPDKIKX0DER&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=101&pf_rd_s=center-3&pf_rd_r=1ATEMRNW5HZADSBN4D1Z&pf_rd_i=3079714011&pf_rd_p=1714304802",
    "http://www.amazon.com/dp/B00ECOVVWQ/ref=s9_acss_bw_hsb_TVBBEvergreen_s4?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=1NC9VHWNBR03935ZKY70&pf_rd_t=101&pf_rd_p=1749063942&pf_rd_i=8256745011",
    "http://www.amazon.com/Norton-Antivirus-2014-User-Licenses/dp/B00EZPXOTA/ref=sr_1_1?s=software&ie=UTF8&qid=1395351921&sr=1-1",
    "http://www.amazon.com/Norton-Antivirus-2014-Licenses-Download/dp/B00FGDEAC0/ref=sr_1_1_title_1?s=software&ie=UTF8&qid=1395351921&sr=1-1",
    "http://www.amazon.com/Norton-Antivirus-2013-User-Version/dp/B008TNCZLM/ref=sr_1_2_title_1?s=software&ie=UTF8&qid=1395351921&sr=1-2",
    "http://www.amazon.com/Norton-Antivirus-2014-User-License/dp/B00EZPXTOU/ref=sr_1_3?s=software&ie=UTF8&qid=1395351921&sr=1-3",
    "http://www.amazon.com/Clover-Wonder-Clips-Per-Pack/dp/B004ZKPX8A/ref=zg_bs_arts-crafts_10",
    "http://www.amazon.com/Art-Advantage-Acrylic-Brush-24-Piece/dp/B0027AANDA/ref=zg_bs_arts-crafts_8",
    "http://www.amazon.com/Fiskars-12-27457097-Gel-48-Piece-Value/dp/B000S161FO/ref=zg_bs_arts-crafts_6",
    "http://www.amazon.com/Silhouette-Cameo-Replacement-Cutting-Mat/dp/B005VPVW3I/ref=zg_bs_arts-crafts_5",
    "http://www.amazon.com/Brother-Feature-Rich-Built-In-Auto-Size-Buttonholes/dp/B000JQM1DE/ref=zg_bs_arts-crafts_1",
)

from amazon.amazon import Amazon
a = Amazon()

for url in urls:
    asin = a.get_asin_from_url(url)
    print asin

