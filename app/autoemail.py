import smtplib
from email.mime.text import MIMEText

sender_email = "ericgithaiga007@gmail.com"
sender_password = "gjwn hajc tols wlui "
recipient_email = "erickgithaiga28@gmail.com"
subject = "Hello from Ricky's Shop"
body = '''
<!DOCTYPE html>
<html
  style="
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    box-sizing: border-box;
    font-size: 14px;
    margin: 0;
  "
>
  <head>
    <meta name="viewport" content="width=device-width" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <style type="text/css">
      body {
        margin: 0;
        padding: 0;
      }
      img {
        border: 0 !important;
        outline: none !important;
      }
      p {
        margin: 0px !important;
        padding: 0px !important;
      }
      table {
        border-collapse: collapse;
        mso-table-lspace: 0px;
        mso-table-rspace: 0px;
      }
      td,
      a,
      span {
        border-collapse: collapse;
        mso-line-height-rule: exactly;
      }
      .hh-grayBox {
	background-color: #F8F8F8;
	margin-bottom: 20px;
	padding: 35px;
  margin-top: 20px;
}
.pt45{padding-top:45px;}
.order-tracking{
	text-align: center;
	width: 33.33%;
	position: relative;
	display: block;
}
.order-tracking .is-complete{
	display: block;
	position: relative;
	border-radius: 50%;
	height: 30px;
	width: 30px;
	border: 0px solid #AFAFAF;
	background-color: #f7be16;
	margin: 0 auto;
	transition: background 0.25s linear;
	-webkit-transition: background 0.25s linear;
	z-index: 2;
}
.order-tracking .is-complete:after {
	display: block;
	position: absolute;
	content: '';
	height: 14px;
	width: 7px;
	top: -2px;
	bottom: 0;
	left: 5px;
	margin: auto 0;
	border: 0px solid #ffffff;
	border-width: 0px 2px 2px 0;
	transform: rotate(45deg);
	opacity: 0;
}
.order-tracking.completed .is-complete{
	border-color: #27aa80;
	border-width: 0px;
	background-color: #27aa80;
}
.order-tracking.completed .is-complete:after {
	border-color: #ffffff;
	border-width: 0px 3px 3px 0;
	width: 7px;
	left: 11px;
	opacity: 1;
}
.order-tracking p {
	color: #A4A4A4;
	font-size: 16px;
	margin-top: 8px;
	margin-bottom: 0;
	line-height: 20px;
}
.order-tracking p span{font-size: 14px;}
.order-tracking.completed p{color: #000000;}
.order-tracking::before {
	content: '';
	display: block;
	height: 3px;
	width: calc(100% - 40px);
	background-color: #f7be16;
	top: 13px;
	position: absolute;
	left: calc(-50% + 20px);
	z-index: 0;
}
.order-tracking:first-child:before{display: none;}
.order-tracking.completed:before{background: #27aa80;}
.justify-content-between{
    display: flex;
    justify-content: center;
    flex-wrap: nowrap;    
}
.em_full_img2{
    height: 25rem;
    width: 25rem;
    border-radius: 0.2rem;
}

    </style>
  </head>
  <body
    itemscope
    itemtype="http://schema.org/EmailMessage"
    style="
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
      box-sizing: border-box;
      font-size: 14px;
      -webkit-font-smoothing: antialiased;
      -webkit-text-size-adjust: none;
      width: 100% !important;
      height: 100%;
      line-height: 1.6em;
      background-color: #f6f6f6;
      margin: 0;
    "
    bgcolor="#f6f6f6"
  >
    <table
      width="100%"
      border="0"
      cellspacing="0"
      cellpadding="0"
      class="em_full_wrap"
      align="center"
      bgcolor="#efefef"
    >
      <tr>
        <td align="center" valign="top">
          <table
            align="center"
            width="650"
            border="0"
            cellspacing="0"
            cellpadding="0"
            class="em_main_table"
            style="width: 650px; table-layout: fixed"
          >
            <tr>
              <td
                align="center"
                valign="top"
                style="padding: 0 25px"
                class="em_aside10"
              >
                <table
                  width="100%"
                  border="0"
                  cellspacing="0"
                  cellpadding="0"
                  align="center"
                >
                  <tr>
                    <td height="26" style="height: 26px" class="em_h20">
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td align="center" valign="top">
                      <a href="#" target="_blank" style="text-decoration: none"
                        ><p
                          
                          width="208"
                          height="41"
                          
                          border="0"
                          style="
                            display: block;
                            font-family: Arial, sans-serif;
                            font-size: 18px;
                            line-height: 25px;
                            text-align: center;
                            color: #000000;
                            font-weight: bold;
                            max-width: 208px;
                          "
                          class="em_w150"
                      > Ricky's Shop</p></a>
                    </td>
                  </tr>
                  <tr>
                    <td height="28" style="height: 28px" class="em_h20">
                      &nbsp;
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    <table
      width="100%"
      border="0"
      cellspacing="0"
      cellpadding="0"
      class="em_full_wrap"
      align="center"
      bgcolor="#efefef"
    >
      <tr>
        <td align="center" valign="top" class="em_aside5">
          <table
            align="center"
            width="650"
            border="0"
            cellspacing="0"
            cellpadding="0"
            class="em_main_table"
            style="width: 650px; table-layout: fixed"
          >
            <tr>
              <td
                align="center"
                valign="top"
                style="padding: 0 25px; background-color: #ffffff"
                class="em_aside10"
              >
                <table
                  width="100%"
                  border="0"
                  cellspacing="0"
                  cellpadding="0"
                  align="center"
                >
                  <tr>
                    <td height="25" style="height: 25px" class="em_h10">
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td valign="top" align="center">
                      <img
                        src="https://res.cloudinary.com/dufdnc0ie/image/upload/v1711814696/rxtpylvrj5xo3zzalsor.png"
                        width="380"
                        height="200"
                        class="em_full_img2"
                        alt="Alt tag goes here"
                        border="0"
                        style="
                          display: block;
                          max-width: 380px;
                          font-family: Arial, sans-serif;
                          font-size: 17px;
                          line-height: 20px;
                          color: #000000;
                          font-weight: bold;
                        "
                      />
                    </td>
                  </tr>
                  <tr>
                    <td height="22" style="height: 22px" class="em_h20">
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td
                      class="em_blue em_font_22"
                      align="center"
                      valign="top"
                      style="
                        font-family: Arial, sans-serif;
                        font-size: 26px;
                        line-height: 29px;
                        color: #000000;
                        font-weight: bold;
                      "
                    >
                      Thank You For Shopping with us
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="15"
                      style="height: 15px; font-size: 0px; line-height: 0px"
                    >
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td
                      class="em_grey"
                      align="center"
                      valign="top"
                      style="
                        font-family: Arial, sans-serif;
                        font-size: 16px;
                        line-height: 22px;
                        color: #434343;
                      "
                    >
                      {name}, thanks so much for choosing Ricky Shop for your
                      litter box needs.<br class="em_hide" />
                      We’ve received your order, and the herding of cats
                      has&nbsp;begun.
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="15"
                      style="height: 15px; font-size: 1px; line-height: 1px"
                    >
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td
                      class="em_grey"
                      align="center"
                      valign="top"
                      style="
                        font-family: Arial, sans-serif;
                        font-size: 16px;
                        line-height: 22px;
                        color: #434343;
                      "
                    >
                      <strong>Order #:</strong>
                      <span style="color: #da885b; text-decoration: underline"
                        >{order.id}</span
                      >
                      <span class="em_hide2">&nbsp;|&nbsp;</span
                      ><span class="em_mob_block"></span>
                      <strong>Order Date:</strong>{order.created_at}
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="20"
                      style="height: 20px; font-size: 1px; line-height: 1px"
                    >
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td align="center" valign="top">
                      <table
                        width="145"
                        style="
                          width: 145px;
                          background-color: #000000;
                          border-radius: 4px;
                        "
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        align="center"
                        bgcolor="#6bafb2"
                      >
                        <tr>
                          <td
                            class="em_white"
                            height="42"
                            align="center"
                            valign="middle"
                            style="
                              font-family: Arial, sans-serif;
                              font-size: 16px;
                              color: #ffffff;
                              font-weight: bold;
                              height: 42px;
                            "
                          >
                            <a
                              href=""
                              target="_blank"
                              style="
                                text-decoration: none;
                                color: #ffffff;
                                line-height: 42px;
                                display: block;
                              "
                              >Order Status</a
                            >
                          </td>
                        </tr>
                        
                      </table>
                      <div class="container">
                        <div class="row">
                                              <div class="col-12 col-md-10 hh-grayBox pt45 pb20">
                                                  <div class="row justify-content-between">
                                                      <div class="order-tracking completed">
                                                          <span class="is-complete"></span>
                                                          <p>Ordered<br><span>Mon, June 24</span></p>
                                                      </div>
                                                      <div class="order-tracking ">
                                                          <span class="is-complete"></span>
                                                          <p>Shipped<br><span>Tue, June 25</span></p>
                                                      </div>
                                                      <div class="order-tracking">
                                                          <span class="is-complete"></span>
                                                          <p>Delivered<br><span>Fri, June 28</span></p>
                                                      </div>
                                                  </div>
                                              </div>
                                          </div>
                      </div>
                    </td>
                  </tr>
                  <tr>
                    <td height="40" style="height: 40px" class="em_h10">
                      &nbsp;
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            <tr>
              <td
                height="15"
                class="em_h10"
                style="height: 15px; font-size: 1px; line-height: 1px"
              >
                &nbsp;
              </td>
            </tr>
            <tr>
              <td
                align="center"
                valign="top"
                style="padding: 0 50px; background-color: #ffffff"
                class="em_aside10"
              >
                <table
                  width="100%"
                  border="0"
                  cellspacing="0"
                  cellpadding="0"
                  align="center"
                >
                  <tr>
                    <td height="35" style="height: 35px" class="em_h10">
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td
                      class="em_grey"
                      align="center"
                      valign="top"
                      style="
                        font-family: Arial, sans-serif;
                        font-size: 18px;
                        line-height: 22px;
                        color: #434343;
                        font-weight: bold;
                      "
                    >
                      BILLED TO:
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="10"
                      style="height: 10px; font-size: 1px; line-height: 1px"
                    >
                      &nbsp;
                    </td>
                  </tr>

                  <tr>
                    <td
                      class="em_grey"
                      align="center"
                      valign="top"
                      style="
                        font-family: Arial, sans-serif;
                        font-size: 16px;
                        line-height: 24px;
                        color: #434343;
                      "
                    >
                      {name}<br />
                      XXXX XXXXXXX XX<br />
                      XXXXXX, XX XXXXX
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="20"
                      style="height: 20px; font-size: 1px; line-height: 1px"
                    >
                      &nbsp;
                    </td>
                  </tr>

                  <tr>
                    <td
                      height="1"
                      bgcolor="#efefef"
                      style="
                        height: 1px;
                        background-color: #efefef;
                        font-size: 0px;
                        line-height: 0px;
                      "
                    >
                      <img
                        src="/assets/pilot/images/templates/spacer.gif"
                        width="1"
                        height="1"
                        alt=""
                        border="0"
                        style="display: block"
                      />
                    </td>
                  </tr>

                  <tr>
                    <td
                      height="25"
                      class="em_h20"
                      style="height: 25px; font-size: 1px; line-height: 1px"
                    >
                      &nbsp;
                    </td>
                  </tr>

                  <tr>
                    <td valign="top" align="center">
                      <table
                        width="100%"
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        align="center"
                      >
                        <tr>
                          <td valign="top">
                            <table
                              width="120"
                              border="0"
                              cellspacing="0"
                              cellpadding="0"
                              align="left"
                              style="width: 120px"
                              class="em_wrapper"
                            >
                              <tr>
                                <td valign="top" align="center">
                                  <img
                                    src="/assets/pilot/images/templates/cat_2.jpg"
                                    width="120"
                                    height="120"
                                    alt="Alt tag goes here"
                                    border="0"
                                    style="
                                      display: block;
                                      max-width: 120px;
                                      font-family: Arial, sans-serif;
                                      font-size: 17px;
                                      line-height: 20px;
                                      color: #000000;
                                      font-weight: bold;
                                    "
                                  />
                                </td>
                              </tr>
                            </table>
                            <table
                              width="25"
                              border="0"
                              cellspacing="0"
                              cellpadding="0"
                              align="left"
                              style="width: 25px"
                              class="em_hide"
                            >
                              <tr>
                                <td
                                  valign="top"
                                  align="left"
                                  width="25"
                                  style="width: 25px"
                                  class="em_hide"
                                >
                                  &nbsp;
                                </td>
                              </tr>
                            </table>
                            <table
                              width="405"
                              border="0"
                              cellspacing="0"
                              cellpadding="0"
                              align="left"
                              style="width: 405px"
                              class="em_wrapper"
                            >
                              <tr>
                                <td
                                  height="16"
                                  style="
                                    height: 16px;
                                    font-size: 1px;
                                    line-height: 1px;
                                  "
                                >
                                  &nbsp;
                                </td>
                              </tr>
                              <tr>
                                <td
                                  class="em_grey"
                                  align="left"
                                  valign="top"
                                  style="
                                    font-family: Arial, sans-serif;
                                    font-size: 18px;
                                    line-height: 22px;
                                    color: #434343;
                                    font-weight: bold;
                                  "
                                >
                                  Master Kitty Enterprise Edition
                                </td>
                              </tr>
                              <tr>
                                <td
                                  height="13"
                                  style="
                                    height: 13px;
                                    font-size: 1px;
                                    line-height: 1px;
                                  "
                                >
                                  &nbsp;
                                </td>
                              </tr>
                              <tr>
                                <td
                                  class="em_grey"
                                  align="left"
                                  valign="top"
                                  style="
                                    font-family: Arial, sans-serif;
                                    font-size: 16px;
                                    line-height: 20px;
                                    color: #434343;
                                  "
                                >
                                  Quantity:
                                  <span
                                    style="color: #da885b; font-weight: bold"
                                    >1</span
                                  >
                                </td>
                              </tr>
                              <tr>
                                <td
                                  height="13"
                                  style="
                                    height: 13px;
                                    font-size: 1px;
                                    line-height: 1px;
                                  "
                                >
                                  &nbsp;
                                </td>
                              </tr>
                              <tr>
                                <td
                                  class="em_grey"
                                  align="left"
                                  valign="top"
                                  style="
                                    font-family: Arial, sans-serif;
                                    font-size: 16px;
                                    line-height: 20px;
                                    color: #434343;
                                  "
                                >
                                  Amount ($):
                                  <span
                                    style="color: #da885b; font-weight: bold"
                                    >$850</span
                                  >
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="25"
                      class="em_h20"
                      style="height: 25px; font-size: 1px; line-height: 1px"
                    >
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="1"
                      bgcolor="#efefef"
                      style="
                        height: 1px;
                        background-color: #efefef;
                        font-size: 0px;
                        line-height: 0px;
                      "
                    >
                      <img
                        src="/assets/pilot/images/templates/spacer.gif"
                        width="1"
                        height="1"
                        alt=""
                        border="0"
                        style="display: block"
                      />
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="21"
                      class="em_h20"
                      style="height: 21px; font-size: 1px; line-height: 1px"
                    >
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td valign="top" align="right" style="padding-bottom: 5px">
                      <table
                        width="100%"
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        align="right"
                      >
                        <tr>
                          <td>&nbsp;</td>
                          <td
                            class="em_grey"
                            width="100"
                            align="right"
                            valign="top"
                            style="
                              font-family: Arial, sans-serif;
                              font-size: 16px;
                              line-height: 20px;
                              color: #434343;
                              width: 100px;
                            "
                          >
                            Subtotal
                          </td>
                          <td
                            width="20"
                            style="
                              width: 20px;
                              font-size: 0px;
                              line-height: 0px;
                            "
                          ></td>
                          <td
                            width="100"
                            class="em_grey"
                            align="right"
                            valign="top"
                            style="
                              font-family: Arial, sans-serif;
                              font-size: 16px;
                              line-height: 20px;
                              color: #434343;
                              width: 100px;
                            "
                          >
                            $850
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td valign="top" align="right" style="padding-bottom: 10px">
                      <table
                        width="100%"
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        align="right"
                      >
                        <tr>
                          <td>&nbsp;</td>
                          <td
                            class="em_grey"
                            width="100"
                            align="right"
                            valign="top"
                            style="
                              font-family: Arial, sans-serif;
                              font-size: 16px;
                              line-height: 20px;
                              color: #434343;
                              width: 100px;
                            "
                          >
                            Sales Tax
                          </td>
                          <td
                            width="20"
                            style="
                              width: 20px;
                              font-size: 0px;
                              line-height: 0px;
                            "
                          ></td>
                          <td
                            width="100"
                            class="em_grey"
                            align="right"
                            valign="top"
                            style="
                              font-family: Arial, sans-serif;
                              font-size: 16px;
                              line-height: 20px;
                              color: #434343;
                              width: 100px;
                            "
                          >
                            $76.50
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td valign="top" align="right">
                      <table
                        width="100%"
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        align="right"
                      >
                        <tr>
                          <td>&nbsp;</td>
                          <td
                            class="em_grey"
                            width="100"
                            align="right"
                            valign="top"
                            style="
                              font-family: Arial, sans-serif;
                              font-size: 16px;
                              line-height: 20px;
                              color: #434343;
                              width: 100px;
                              font-weight: bold;
                            "
                          >
                            Total
                          </td>
                          <td
                            width="20"
                            style="
                              width: 20px;
                              font-size: 0px;
                              line-height: 0px;
                            "
                          ></td>
                          <td
                            width="100"
                            class="em_grey"
                            align="right"
                            valign="top"
                            style="
                              font-family: Arial, sans-serif;
                              font-size: 16px;
                              line-height: 20px;
                              color: #434343;
                              width: 100px;
                              font-weight: bold;
                            "
                          >
                            $926.50
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td height="36" style="height: 36px" class="em_h10">
                      &nbsp;
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    <table
      width="100%"
      border="0"
      cellspacing="0"
      cellpadding="0"
      class="em_full_wrap"
      align="center"
      bgcolor="#efefef"
    >
      <tr>
        <td align="center" valign="top">
          <table
            align="center"
            width="650"
            border="0"
            cellspacing="0"
            cellpadding="0"
            class="em_main_table"
            style="width: 650px; table-layout: fixed"
          >
            <tr>
              <td
                align="center"
                valign="top"
                style="padding: 0 25px"
                class="em_aside10"
              >
                <table
                  width="100%"
                  border="0"
                  cellspacing="0"
                  cellpadding="0"
                  align="center"
                >
                  <tr>
                    <td height="40" style="height: 40px" class="em_h20">
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td align="center" valign="top">
                      <table
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        align="center"
                      >
                        <tr>
                          <td
                            width="30"
                            style="width: 30px"
                            align="center"
                            valign="middle"
                          >
                            <a
                              href="#"
                              target="_blank"
                              style="text-decoration: none"
                              ><img
                                src="/assets/pilot/images/templates/fb.png"
                                width="30"
                                height="30"
                                alt="Fb"
                                border="0"
                                style="
                                  display: block;
                                  font-family: Arial, sans-serif;
                                  font-size: 18px;
                                  line-height: 25px;
                                  text-align: center;
                                  color: #000000;
                                  font-weight: bold;
                                  max-width: 30px;
                                "
                            /></a>
                          </td>
                          <td width="12" style="width: 12px">&nbsp;</td>
                          <td
                            width="30"
                            style="width: 30px"
                            align="center"
                            valign="middle"
                          >
                            <a
                              href="#"
                              target="_blank"
                              style="text-decoration: none"
                              ><img
                                src="/assets/pilot/images/templates/tw.png"
                                width="30"
                                height="30"
                                alt="Tw"
                                border="0"
                                style="
                                  display: block;
                                  font-family: Arial, sans-serif;
                                  font-size: 14px;
                                  line-height: 25px;
                                  text-align: center;
                                  color: #000000;
                                  font-weight: bold;
                                  max-width: 30px;
                                "
                            /></a>
                          </td>
                          <td width="12" style="width: 12px">&nbsp;</td>
                          <td
                            width="30"
                            style="width: 30px"
                            align="center"
                            valign="middle"
                          >
                            <a
                              href="#"
                              target="_blank"
                              style="text-decoration: none"
                              ><img
                                src="/assets/pilot/images/templates/insta.png"
                                width="30"
                                height="30"
                                alt="Insta"
                                border="0"
                                style="
                                  display: block;
                                  font-family: Arial, sans-serif;
                                  font-size: 14px;
                                  line-height: 25px;
                                  text-align: center;
                                  color: #000000;
                                  font-weight: bold;
                                  max-width: 30px;
                                "
                            /></a>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="16"
                      style="
                        height: 16px;
                        font-size: 1px;
                        line-height: 1px;
                        height: 16px;
                      "
                    >
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td
                      class="em_grey"
                      align="center"
                      valign="top"
                      style="
                        font-family: Arial, sans-serif;
                        font-size: 15px;
                        line-height: 18px;
                        color: #434343;
                        font-weight: bold;
                      "
                    >
                      Problems or questions?
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="10"
                      style="height: 10px; font-size: 1px; line-height: 1px"
                    >
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td
                      align="center"
                      valign="top"
                      style="font-size: 0px; line-height: 0px"
                    >
                      <table
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        align="center"
                      >
                        <tr>
                          <td
                            width="15"
                            align="left"
                            valign="middle"
                            style="
                              font-size: 0px;
                              line-height: 0px;
                              width: 15px;
                            "
                          >
                            <a
                              href="mailto:meow@meowgun.com"
                              style="text-decoration: none"
                              ><img
                                src="/assets/pilot/images/templates/email_img.png"
                                width="15"
                                height="12"
                                alt=""
                                border="0"
                                style="display: block; max-width: 15px"
                            /></a>
                          </td>
                          <td
                            width="9"
                            style="width: 9px; font-size: 0px; line-height: 0px"
                            class="em_w5"
                          >
                            <img
                              src="/assets/pilot/images/templates/spacer.gif"
                              width="1"
                              height="1"
                              alt=""
                              border="0"
                              style="display: block"
                            />
                          </td>
                          <td
                            class="em_grey em_font_11"
                            align="left"
                            valign="middle"
                            style="
                              font-family: Arial, sans-serif;
                              font-size: 13px;
                              line-height: 15px;
                              color: #434343;
                            "
                          >
                            <a
                              href="mailto:meow@meowgun.com"
                              style="text-decoration: none; color: #434343"
                              >meow@meowgun.com</a
                            >
                            <a
                              href="mailto:marketing@mailgun.com"
                              style="text-decoration: none; color: #434343"
                              >[mailto:marketing@mailgun.com]</a
                            >
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="9"
                      style="font-size: 0px; line-height: 0px; height: 9px"
                      class="em_h10"
                    >
                      <img
                        src="/assets/pilot/images/templates/spacer.gif"
                        width="1"
                        height="1"
                        alt=""
                        border="0"
                        style="display: block"
                      />
                    </td>
                  </tr>
                  <tr>
                    <td align="center" valign="top">
                      <table
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        align="center"
                      >
                        <tr>
                          <td
                            width="12"
                            align="left"
                            valign="middle"
                            style="
                              font-size: 0px;
                              line-height: 0px;
                              width: 12px;
                            "
                          >
                            <a
                              href="#"
                              target="_blank"
                              style="text-decoration: none"
                              ><img
                                src="/assets/pilot/images/templates/img_1.png"
                                width="12"
                                height="16"
                                alt=""
                                border="0"
                                style="display: block; max-width: 12px"
                            /></a>
                          </td>
                          <td
                            width="7"
                            style="width: 7px; font-size: 0px; line-height: 0px"
                            class="em_w5"
                          >
                            &nbsp;
                          </td>
                          <td
                            class="em_grey em_font_11"
                            align="left"
                            valign="middle"
                            style="
                              font-family: Arial, sans-serif;
                              font-size: 13px;
                              line-height: 15px;
                              color: #434343;
                            "
                          >
                            <a
                              href="#"
                              target="_blank"
                              style="text-decoration: none; color: #434343"
                              >Ricky Shop</a
                            >
                            &bull; 123 Meow Way &bull; Cattown, CA 95389
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td height="35" style="height: 35px" class="em_h20">
                      &nbsp;
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            <tr>
              <td
                height="1"
                bgcolor="#dadada"
                style="font-size: 0px; line-height: 0px; height: 1px"
              >
                <img
                  src="/assets/pilot/images/templates/spacer.gif"
                  width="1"
                  height="1"
                  alt=""
                  border="0"
                  style="display: block"
                />
              </td>
            </tr>
            <tr>
              <td
                align="center"
                valign="top"
                style="padding: 0 25px"
                class="em_aside10"
              >
                <table
                  width="100%"
                  border="0"
                  cellspacing="0"
                  cellpadding="0"
                  align="center"
                >
                  <tr>
                    <td
                      height="16"
                      style="font-size: 0px; line-height: 0px; height: 16px"
                    >
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td align="center" valign="top">
                      <table
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        align="left"
                        class="em_wrapper"
                      >
                        <tr>
                          <td
                            class="em_grey"
                            align="center"
                            valign="middle"
                            style="
                              font-family: Arial, sans-serif;
                              font-size: 11px;
                              line-height: 16px;
                              color: #434343;
                            "
                          >
                            &copy; Meowgun 2019 &nbsp;|&nbsp;
                            <a
                              href="#"
                              target="_blank"
                              style="text-decoration: underline; color: #434343"
                              >Unsubscribe</a
                            >
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td
                      height="16"
                      style="font-size: 0px; line-height: 0px; height: 16px"
                    >
                      &nbsp;
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            <tr>
              <td
                class="em_hide"
                style="
                  line-height: 1px;
                  min-width: 650px;
                  background-color: #efefef;
                "
              >
                <img
                  alt=""
                  src="/assets/pilot/images/templates/spacer.gif"
                  height="1"
                  width="650"
                  style="
                    max-height: 1px;
                    min-height: 1px;
                    display: block;
                    width: 650px;
                    min-width: 650px;
                  "
                  border="0"
                />
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>

'''


# html_message = MIMEText(body, 'html')
# html_message['Subject'] = subject
# html_message['From'] = sender_email
# html_message['To'] = recipient_email
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
#    server.login(sender_email, sender_password)
#    server.sendmail(sender_email, recipient_email, html_message.as_string())


def send_order_email( sender_email, sender_password, recipient_email, subject, body):
    html_message = MIMEText(body, 'html')
    html_message['Subject'] = subject
    html_message['From'] = sender_email
    html_message['To'] = recipient_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, html_message.as_string())

send_order_email( sender_email, sender_password, recipient_email, subject, body)