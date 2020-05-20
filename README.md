# Email-Sender

This project is an E-mail sender app built using Django and Bootstrap frameworks.

It demonstrates: 
			<pre>
				<li> Django E-mail [<a href="https://docs.djangoproject.com/en/3.0/topics/email/" target="_blank">view doc</a>]</li>
				<li> Django Custom Template Tags & Filters [<a href="https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/" target="_blank">view doc</a>]</li>
			</pre>
				

## Prerequisite for Sending E-mail
To send email from an unauthorized app, there are 2 options: <br>
i. Allow Less Secure App Access - Not Recommended [<a href="https://devanswers.co/allow-less-secure-apps-access-gmail-account/" target="_blank">more</a>] <br>
ii. Add App Passwords - Requires Enabling a 2-Step Verification [<a href="https://devanswers.co/create-application-specific-password-gmail/" target="_blank">more</a>]

<br>
<u>Note:</u>
<br>
- The values for <code>SECRET_KEY</code>, <code>EMAIL_HOST_USER</code> and <code>EMAIL_HOST_PASSWORD</code> are stored in environment variables, so configure them on your system accordingly. Refer to <i>settings.py</i>