#
# Conditional build:
# _with_rewrite_ldap	- enable ldap map support for mod_rewrite (alpha)
# _without_ipv6		- disable IPv6 support
#
%include	/usr/lib/rpm/macros.perl
Summary:	The most widely used Web server on the Internet
Summary(cs):	Nejroz¹íøenìj¹í WWW server v Internetu
Summary(da):	Den mest brugte web-tjener på Internet
Summary(de):	Der am häufigsten verwendete Web-Server im Internet
Summary(es):	El servidor web más conocido y usado en Internet
Summary(fr):	Le serveur Web le plus utilisé sur Internet
Summary(id):	Web server yang paling banyak digunakan di Internet
Summary(is):	Vinsælasti vefþjónninn á Netinu
Summary(it):	Il web server più diffuso su Internet
Summary(ja):	¥¤¥ó¥¿¡¼¥Í¥Ã¥È¾å¤ÇºÇ¤â°ìÈÌÅª¤Ë»ÈÍÑ¤µ¤ì¤Æ¤¤¤ë Web ¥µ¡¼¥Ð¡¼
Summary(no):	Den mest utbredte web-tjeneren på Internett
Summary(pl):	Serwer WWW (World Wide Web)
Summary(pt):	O servidor Web mais largamente utilizado em toda a Internet
Summary(pt_BR):	Servidor HTTPD para prover serviços WWW
Summary(ru):	óÁÍÙÊ ÐÏÐÕÌÑÒÎÙÊ Web-Server
Summary(sk):	Najviac pou¾ívaný Web server na Internete
Summary(sl):	Najbolj uporabljani spletni stre¾nik interneta
Summary(sv):	Den mest använda webbservern på Internet
Summary(tr):	Lider WWW tarayýcý
Summary(uk):	îÁÊÐÏÐÕÌÑÒÎ¦ÛÉÊ Web-Server
Summary(zh_CN):	Internet ÉÏÓ¦ÓÃ×î¹ã·ºµÄ Web ·þÎñ³ÌÐò¡£
Name:		apache
Version:	1.3.28
Release:	0.1
License:	Apache Group 
Group:		Networking/Daemons
Source0:	http://www.apache.org/dist/httpd/%{name}_%{version}.tar.gz
# Source0-md5:	2cdece7b4881d541e072de6a2b65db77
Source1:	%{name}1.init
Source2:	%{name}.logrotate
Source3:	%{name}-icons.tar.gz
Source4:	%{name}.sysconfig
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source5-md5:	74ff6e8d8a7b365b48ed10a52fbeb84e
Source6:	%{name}-httpd.conf
Source8:	%{name}-mod_vhost_alias.conf
Source9:	%{name}-mod_status.conf
Source10:	%{name}-mod_proxy.conf
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-suexec.patch
Patch2:		%{name}-htdocs.patch
Patch3:		%{name}-errordocs.patch
Patch4:		%{name}-apxs.patch
Patch5:		%{name}-mod_ssl-addon.patch
Patch6:		%{name}-mod_ssl-eapi.patch
Patch7:		%{name}-EAPI_MM_CORE_PATH-correction.patch
Patch8:		%{name}-EAPI_MM=SYSTEM.patch
Patch9:		%{name}-ipv6-PLD.patch
Patch10:	%{name}-modules_symbols.patch
Patch11:	%{name}-apxs_force_rm_cp.patch
Patch12:	%{name}-db3.patch
Patch13:	%{name}-lookup_map_ldap.patch
Patch14:	%{name}-man.patch
Patch15:	%{name}-fpic.patch
Patch16:	%{name}-buff.patch
Patch17:	%{name}-mkstemp.patch
Patch18:	%{name}-EAPI-missing_files.patch
Patch19:	%{name}-PLD-nov6.patch
Patch20:	%{name}-configdir_skip_backups.patch
Patch21:	%{name}-apxs-quiet.patch
URL:		http://www.apache.org/
BuildRequires:	db3-devel
BuildRequires:	mm-devel >= 1.1.3
%{?_with_rewrite_ldap:BuildRequires: openldap-devel}
PreReq:		mm
PreReq:		perl
PreReq:		rc-scripts
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/useradd
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Provides:	%{name}(EAPI) = %{version}
Requires:	/etc/mime.types
Provides:	httpd
Requires:	mailcap
Requires:	psmisc >= 20.1
Provides:	webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	httpd
Obsoletes:	webserver
Obsoletes:	apache-extra
Obsoletes:	apache6
Obsoletes:	apache-doc
Obsoletes:	indexhtml

%define		_sysconfdir	/etc/httpd
%define		_includedir	%{_prefix}/include/apache
%define		_datadir	/home/httpd
%define		_libexecdir	%{_prefix}/lib/apache
%define		apxs		/usr/sbin/apxs

%description
Apache is a powerful, full-featured, efficient and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

%description -l cs
Apache je výkonný plnì funkèní efektivní a volnì dostupný WWW server.
Je to nejpopulárnìj¹í WWW server v Internetu.

%description -l da
Apache er en stærk, funktionsrig, effektiv og frit tilgængelig
web-tjener. Apache er også den mest populære web-tjener på Internet.

%description -l de
Apache ist ein leistungsfähiger, frei verfügbarer und effizienter
Web-Server mit umfassenden Funktionen. Apache ist zudem der populärste
Web-Server im Internet.

%description -l es
El servidor web Apache es el mejor servidor gratuito disponible en el
mundo UNIX hoy. Usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vean documentos y sometan datos remotamente. Puede
ejecutar varias funciones diferentes, incluyendo funciones de proxy y
caché, y nos ofrece características como monitor de estado, conversión
dinámica de tipo, y otras más.

%description -l fr
Apache est un serveur Web puissant, efficace, gratuit et complet.
Apache est aussi le serveur Web le plus populaire sur Internet.

%description -l id
Apache adalah Web server yang powerful, efisien, kaya akan feature,
dan tersedia dengan free. Apache juga merupakan Web server yang paling
populer di Internet.

%description -l is
Apache er mjög öflugur og háþróaður vefþjónn sem er ókeypis. Apache er
einnig mest notaði vefþjónninn á Internetinu.

%description -l it
Apache è un Web server potente, dotato di tutte le caratteristiche,
efficiente e gratuito. Ed è anche il web server più diffuso su
Internet.

%description -l ja
Apache ¤Ï¶¯ÎÏ¤Ç½¼¼Â¤·¤¿µ¡Ç½¤ò»ý¤ÄÌµ½þ¤Î Web ¥µ¡¼¥Ð¡¼
¤Ç¤¹¡£¤Þ¤¿¡¢apache ¤Ï¥¤¥ó¥¿¡¼¥Í¥Ã¥È¾å¤ÇºÇ¤â°ìÈÌÅª¤Ë»ÈÍÑ ¤µ¤ì¤Æ¤¤¤ë Web
¥µ¡¼¥Ð¡¼¤Ç¤¹¡£

%description -l no
Apache er en kraftig, funksjonsrik, effektiv og fritt tilgjengelig
web-tjener. Apache er også den mest populære web-tjeneren på Internet.

%description -l pl
Apache jest serwerem WWW (World Wide Web). Instaluj±c ten pakiet
bêdziesz móg³ prezentowaæ w³asne strony WWW w sieci internet.

%description -l pt
O Apache é um servidor de Web poderoso, cheio de potencialidades,
eficiente e gratuito. O Apache é também o servidor Web mais conhecido
na Internet.

%description -l pt_BR
O servidor web Apache é o melhor servidor gratuito disponível no mundo
UNIX hoje. Ele usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vejam documentos e submetam dados remotamente. Ele
pode executar várias funções diferentes, incluindo funções de proxy e
cache, e oferece características como monitor de status, conversão
dinâmica de tipo, e mais.

%description -l ru
Apache - ÜÔÏ ÍÏÝÎÙÊ, ÐÏÌÎÏÆÕÎËÃÉÏÎÁÌØÎÙÊ, ÜÆÆÅËÔÉ×ÎÙÊ, Ó×ÏÂÏÄÎÏ
ÒÁÓÐÒÏÓÔÒÁÎÑÅÍÙÊ É ÓÁÍÙÊ ÐÏÐÕÌÑÒÎÙÊ × Internet WWW-ÓÅÒ×ÅÒ.

%description -l sk
Apache je výkonný, efektívny a voµne dostupný Web server, bohatý na
funkcie. Apache je tie¾ najpopulárnej¹ím Web serverom na Internete.

%description -l sv
Apache är en kraftfull, finessrik, effektiv och fritt tillgänglig
webbserver. Apache är också den populäraste webbservern på Internet.

%description -l tr
Apache serbest daðýtýlan ve çok kullanýlan yetenekli bir web
sunucusudur.

%description -l zh_CN
Apache ÊÇ¹¦ÄÜÇ¿¾¢ÆëÈ«¡¢¸ßÐ§ÇÒÃâ·ÑÌá¹©µÄ Web ·þÎñ³ÌÐò£¬ Í¬Ê±Ò²ÊÇ
Internet ÉÏ×îÁ÷ÐÐµÄ Web ·þÎñ³ÌÐò¡£

Èç¹ûÄúÐèÒª Web ·þÎñ³ÌÐò£¬Çë°²×° apache Èí¼þ°ü¡£

%package suexec
Summary:	Apache suexec wrapper
Summary(pl):	Suexec wrapper do serwera www Apache
Summary(ru):	Apache suEXEC CGI wrapper
Summary(uk):	Apache suEXEC CGI wrapper
Group:		Development/Tools
Requires:	%{name}(EAPI) = %{version}

%description suexec
The suEXEC feature provides Apache users the ability to run CGI and
SSI programs under user IDs different from the user ID of the calling
web-server. Normally, when a CGI or SSI program executes, it runs as
the same user who is running the web server.

%description suexec -l pl
SuEXEC umo¿liwia serwerowi Apache uruchamianie programów CGI i SSI z
innym UID ni¿ wywo³uj±cy je serwer. Normalnie programy CGI i SSI s±
wykonywane jako taki sam u¿ytkownik jak serwer WWW.

%description suexec -l ru
ðÁËÅÔ suEXEC ÐÏÚ×ÏÌÑÅÔ ÚÁÐÕÓËÁÔØ CGI-ÐÒÏÇÒÁÍÍÙ ÐÏÄ user-id, ÏÔÌÉÞÎÙÍÉ
ÏÔ ÔÏÇÏ, ÐÏÄ ËÏÔÏÒÙÍ ÒÁÂÏÔÁÅÔ ×ÙÚÙ×ÁÀÝÉÊ ÉÈ web-ÓÅÒ×ÅÒ. âÕÄÕÞÉ
ÐÒÁ×ÉÌØÎÏ ÉÓÐÏÌØÚÏ×ÁÎÎÙÍ, ÜÔÏÔ ÐÁËÅÔ ÐÏÚ×ÏÌÑÅÔ ÚÁÍÅÔÎÏ ÓÎÉÚÉÔØ ÒÉÓË
ÎÁÒÕÛÅÎÉÑ ÓÉÓÔÅÍÎÏÊ ÂÅÚÏÐÁÓÎÏÓÔÉ, ×ÙÚ×ÁÎÎÙÊ ÒÁÚÒÅÛÅÎÉÅÍ ÚÁÐÕÓËÁ
ÐÏÌØÚÏ×ÁÔÅÌÑÍ CGI-ÐÒÏÇÒÁÍÍ. ÷ÍÅÓÔÅ Ó ÔÅÍ, ÂÕÄÕÞÉ ÎÅÐÒÁ×ÉÌØÎÏ
ÓËÏÎÆÉÇÕÒÉÒÏ×ÁÎÎÙÍ, ÜÔÏÔ ÐÁËÅÔ ÍÏÖÅÔ ÒÁÚÒÕÛÉÔØ ×ÁÛÕ ÓÉÓÔÅÍÕ, ÓÖÅÞØ ×ÁÛ
ÄÏÍ É ÕËÒÁÓÔØ ÄÅÎØÇÉ ÉÚ ×ÁÛÅÇÏ ÐÅÎÓÉÏÎÎÏÇÏ ÆÏÎÄÁ :)). åÓÌÉ ×Ù ÎÅ
ÉÍÅÅÔÅ ÏÐÙÔÁ ÒÁÂÏÔÙ Ó setuid root ÐÒÏÇÒÁÍÍÁÍÉ É ÐÒÏÂÌÅÍÁÍÉ ÓÉÓÔÅÍÎÏÊ
ÂÅÚÏÐÁÓÎÏÓÔÉ, ÐÏÒÏÖÄÅÎÎÙÍÉ ÉÈ ÐÒÉÍÅÎÅÎÉÅÍ, ÎÁÓÔÏÑÔÅÌØÎÏ ÒÅËÏÍÅÎÄÕÅÍ ÎÅ
ÉÓÐÏÌØÚÏ×ÁÔØ ÜÔÏÇÏ ÐÁËÅÔÁ...

%description suexec -l uk
ðÁËÅÔ suEXEC ÄÏÚ×ÏÌÑ¤ ÚÁÐÕÓËÁÔÉ CGI-ÐÒÏÇÒÁÍÉ Ð¦Ä user-id, ×¦ÄÍ¦ÎÎÉÍ
×¦Ä ÔÏÇÏ, Ð¦Ä ÑËÉÍ ÐÒÁÃÀ¤ ÓÅÒ×ÅÒ. ðÒÉ ÐÒÁ×ÉÌØÎÏÍÕ ×ÉËÏÒÉÓÔÁÎÎ¦, ÃÅÊ
ÐÁËÅÔ ÄÏÚ×ÏÌÑ¤ ÐÏÍ¦ÔÎÏ ÚÎÉÚÉÔÉ ÒÉÚÉË ÐÏÒÕÛÅÎÎÑ ÓÉÓÔÅÍÎÏ§ ÂÅÚÐÅËÉ,
×ÉËÌÉËÁÎÉÊ ÄÏÚ×ÏÌÏÍ ÚÁÐÕÓËÕ ËÏÒÉÓÔÕ×ÁÞÁÍÉ CGI-ÐÒÏÇÒÁÍ. òÁÚÏÍ Ú ÔÉÍ,
ÐÒÉ ÎÅ×¦ÒÎÏÍÕ ËÏÎÆ¦ÇÕÒÕ×ÁÎÎ¦, ÃÅÊ ÐÁËÅÔ ÍÏÖÅ ÚÒÕÊÎÕ×ÁÔÉ ×ÁÛÉ ÓÉÓÔÅÍÕ,
ÓÐÁÌÉÔÉ ×ÁÛ Ä¦Í ¦ ×ËÒÁÓÔÉ ÇÒÏÛ¦ Ú ×ÁÛÏÇÏ ÐÅÎÓ¦ÊÎÏÇÏ ÆÏÎÄÕ :)). ñËÝÏ ×É
ÎÅ ÍÁ¤ÔÅ ÄÏÓ×¦ÄÕ ÒÏÂÏÔÉ Ú setuid root ÐÒÏÇÒÁÍÁÍÉ ÔÁ ÐÒÏÂÌÅÍÁÍÉ
ÓÉÓÔÅÍÎÏ§ ÂÅÚÐÅËÉ, ËÏÔÒ¦ ÐÏÒÏÄÖÅÎ¦ ×ÉËÏÒÉÓÔÁÎÎÑÍ ÔÁËÉÈ ÐÒÏÇÒÁÍ,
ÎÁÓÔ¦ÊÌÉ×Ï ÒÁÄÉÍÏ ÎÅ ×ÉËÏÒÉÓÔÏ×Õ×ÁÔÉ ÃØÏÇÏ ÐÁËÅÔÕ...

%package devel
Summary:	Module development tools for the Apache web server
Summary(cs):	Hlavièkové soubory pro Apache Web server
Summary(da):	Header-filer for Apache webserveren
Summary(de):	Include-Dateien für den Apache Web-Server
Summary(es):	Archivos de inclusión del Apache para desarrollo de módulos
Summary(fr):	Fichiers à inclure pour le serveur Web Apache
Summary(id):	File header untuk Apache Web server
Summary(is):	Hausaskrár með Apache vefþjóninum
Summary(it):	File include per il web server Apache
Summary(ja):	Apache Web ¥µ¡¼¥Ð¡¼ÍÑ¤Î³«È¯¥Ä¡¼¥ë
Summary(no):	Headerfiler for webtjeneren Apache
Summary(pl):	Pliki nag³ówkowe do tworzenai modu³ów rozszerzeñ do serwera www Apache
Summary(pt):	Ficheiros de inclusão para o servidor Web Apache
Summary(pt_BR):	Arquivos de inclusão do Apache para desenvolvimento de módulos
Summary(ru):	æÁÊÌÙ ÚÁÇÏÌÏ×ËÏ× ÄÌÑ web server'Á Apache
Summary(sk):	Hlavièkové súbory pre Apache Web server
Summary(sl):	Glave za spletni stre¾nik Apache
Summary(sv):	Huvudfiler för webbservern Apache
Summary(uk):	úÁÓÏÂÉ ÓÔ×ÏÒÅÎÎÑ ÍÏÄÕÌ¦× ÄÌÑ web server'Õ Apache
Summary(zh_CN):	ÓÃÓÚ Apache Web ·þÎñ³ÌÐòµÄ¿ª·¢¹¤¾ß¡£
Group:		Networking/Utilities
Requires:	%{name}(EAPI) = %{version}
Provides:	%{name}(EAPI)-devel = %{version}

%description devel
The apache-devel package contains header files for Apache.

%description devel -l cs
Balíèek apache-devel obsahuje hlavièkové soubory pro Apache.

%description devel -l da
Apache-devel pakken indeholder headerfiler for Apache.

%description devel -l de
Das Paket apache-devel enthält Header-Dateien für Apache.

%description devel -l es
Este paquete contiene los archivos de inclusión para el Apache.

%description devel -l fr
Le package apache-devel contient le code source pour le serveur Web
Apache.

%description devel -l id
Package apache-devel berisi source code dari Apache Web server.

%description devel -l is
Apache-devel pakkinn inniheldur frumkóða Apache vefþjónsins.

%description devel -l it
Il pacchetto apache-devel contiene i file header per Apache.

%description devel -l no
Apache-devel pakken inneholder headerfiler for Apache.

%description devel -l pl
Pliki nag³ówkowe dla serwera WWW Apache.

%description devel -l pt
O pacote apache-devel contém outros ficheiros para o Apache.

%description devel -l pt_BR
Este pacote contem os arquivos de inclusão para o Apache.

%description devel -l ru
ðÁËÅÔ apache-devel ÓÏÄÅÒÖÉÔ ÈÅÄÅÒÙ ÄÌÑ Web Server'Á.

%description devel -l sk
Balík apache-devel obsahuje zdrojový kód Apache Web servera.

%description devel -l sv
Paketet apache-devel innehåller huvudfilerna för Apache.

%description devel -l uk
ðÁËÅÔ apache-devel Í¦ÓÔÉÔØ ÈÅÄÅÒÉ ÄÌÑ Web Server'Á.

%package mod_actions
Summary:	Apache module for run CGI whenever a file of a certain type is requested
Summary(pl):	Modu³ dla apache do uruchamiania skryptów cgi
Group:		Networking/Daemons
Requires(post,preun):	%{_sbindir}/apxs
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_actions
This package contains mod_actions module. This module lets you run CGI
scripts whenever a file of a certain type is requested. This makes it
much easier to execute scripts that process files.

%description mod_actions -l pl
Ten modu³ pozwala na uruchamianie skryptów w momencie gdy nadchodzi
¿±danie pobrania pliku okre¶lonego typu.

%package mod_auth
Summary:	Apache module with user authentication using textual files
Summary(pl):	Modu³ autentykacji u¿ytkownika przy u¿yciu plików tekstowych dla Apache
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_auth
This package contains mod_auth module. It provides for user
authentication using textual files.

%description mod_auth -l pl
Ten pakiet zawiera modu³ mod_auth. S³u¿y on do autentykacji przy
u¿yciu plików tekstowych.

%package mod_auth_anon
Summary:	Apache module with "anonymous" user access authentication
Summary(pl):	Modu³ apache oferuj±cy anonimow± autoryzacjê u¿ytkownia
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_auth_anon
This package contains mod_auth_anon module. It allows "anonymous" user
access to authenticated areas. It does access control in a manner
similar to anonymous-ftp sites; i.e. have a 'magic' user id
'anonymous' and the email address as a password. These email addresses
can be logged. Combined with other (database) access control methods,
this allows for effective user tracking and customization according to
a user profile while still keeping the site open for 'unregistered'
users. One advantage of using Auth-based user tracking is that, unlike
magic-cookies and funny URL pre/postfixes, it is completely browser
independent and it allows users to share URLs.

%description mod_auth_anon -l pl
Ten modu³ oferuje anonimow± autoryzacjê u¿ytkownia podobnie do
anonimowych serwerów ftp (u¿ytkownik ,,anonymous'' oraz has³o w
postaci adresu pocztowego u¿ytkownika).

%package mod_auth_db
Summary:	Apache module with user authentication which uses Berkeley DB files
Summary(pl):	Modu³ apache z mechanizmem autentykacji u¿ywaj±cym plików Berkeley DB
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_auth_db
This package contains mod_auth_db module. It provides for user
authentication using Berkeley DB files. It is an alternative to DBM
files for those systems which support DB and not DBM. It is only
available in Apache 1.1 and later.

%description mod_auth_db -l pl
Ten pakiet zawiera modu³ mod_auth_db. Modu³ ten s³u¿y do autentykacji
ale jako plików danych u¿ywa Berkeley DB.

%package mod_auth_digest
Summary:	Apache user authentication module using MD5 Digest Authentication
Summary(pl):	Modu³ apache do autoryzacji MD5
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}
Obsoletes:	%{name}-mod_digest

%description mod_auth_digest
This package contains mod_digest module. It provides user
authentication using MD5 Digest Authentication.

%description mod_auth_digest -l pl
Modu³ ten dostarcza metodê autoryzacji bazuj±c± na MD5 Digest
Authentication.

%package mod_define
Summary:	Apache module - authentication variables for arbitrary directives
Summary(pl):	Modu³ apache do definiowania zmiennych
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_define
It provides the definition variables for arbitrary directives, i.e.
variables which can be expanded on any(!) directive line.

%description mod_define -l pl
Modu³ ten umo¿liwia definicjê zmiennych i dyrektyw.

%package mod_digest
Summary:	Older version of apache user authentication module using MD5 Digest Authentication
Summary(pl):	Starsza wersja modu³u apache do autoryzacji MD5
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_digest
This package contains mod_digest module. It provides user
authentication using MD5 Digest Authentication. It implements an older
version of the MD5 Digest Authentication specification which will
probably not work with modern browsers. Please take a look at
mod_auth_digest which implements the most recent version of the
standard.

%description mod_digest -l pl
Modu³ ten dostarcza metodê autoryzacji bazuj±c± na MD5 Digest
Authentication. Implementuje on jedynie starsz± wersjê specyfikacji
autentykacji MD5, i mo¿e nie dzia³aæ z nowoczesnymi przegl±darkami.
Sprawd¼ mod_auth_digest je¶li potrzebujesz implementacji najnowszej
wersji standardu.

%package mod_dir
Summary:	Apache module for "trailing slash" redirects and serving directory index files
Summary(pl):	Modu³ oferuj±cy przekierowania i serwowanie indeksu katalogu.
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_dir
This package contains mod_dir which provides "trailing slash"
redirects and serving directory index files.

%description mod_dir -l pl
Modu³ oferuj±cy przekierowania i serwowanie indeksu katalogu.

%package mod_headers
Summary:	Apache module allows for the customization of HTTP response headers
Summary(pl):	Modu³ pozwalaj±cy na modyfikacjê nag³ówków HTTP
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_headers
This package contains mod_headers module. The module allows for the
customization of HTTP response headers. Headers can be merged,
replaced or removed.

%description mod_headers -l pl
Modu³ pozwalaj±cy na ³±czenie, usuwania, zamianê nag³ówków HTTP
wysy³anych do przegl±darki.

%package mod_mmap_static
Summary:	Apache module for mmap()ing statically configured list files
Summary(pl):	Modu³ s³u¿±cy do mmap()owania plików.
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_mmap_static
This package contains mod_mmap_static module. It provides mmap()ing of
a statically configured list of frequently requested but not changed
files.

%description mod_mmap_static -l pl
Modu³ umo¿liwia mmap()owanie statycznie skonfigurowanych plików
(czêsto u¿ywanych ale nie ulegaj±cych zmianom).

%package mod_imap
Summary:	Apache module with imap-file handler
Summary(pl):	Modu³ z obs³ug± imap-file
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_imap
This package contains mod_imap module. It provides for .map files,
replacing the functionality of the imagemap CGI program. Any directory
or document type configured to use the handler imap-file.

%description mod_imap -l pl
Modu³ umozliwiaj±cy obs³ugê plików .map (imap-file handler)

%package mod_info
Summary:	Apache module with comprehensive overview of the server configuration
Summary(pl):	Modu³ dostarczaj±cy informacji na temat serwera.
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_info
This package contains mod_info module. It provides a comprehensive
overview of the server configuration including all installed modules
and directives in the configuration files.

%description mod_info -l pl
Modu³ dostarczaj±cy informacji o konfiguracji serwera, zainstalowanych
modu³ach itp.

%package mod_proxy
Summary:	Apache module with Web proxy
Summary(pl):	Modu³ dodaj±cy obs³ugê serwera proxy
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_proxy
This package contains module with implementation a proxy/cache for
Apache. It implements proxying capability for FTP, CONNECT (for SSL),
HTTP/0.9, and HTTP/1.0. The module can be configured to connect to
other proxy modules for these and other protocols.

%description mod_proxy -l pl
Modu³ zawiera implementacjê serwera proxy/cache dla Apache.
Iplementacja zawiera obs³ugê FTP, CONNECT (dla SSL), HTTP/0.9 i
HTTP/1.0.

%package mod_rewrite
Summary:	Apache module with rule-based engine for rewrite requested URLs on the fly
Summary(pl):	Modu³ do ,,przepisywania'' adresów URL w locie
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_rewrite
This package contains It provides a rule-based rewriting engine to
rewrite requested URLs on the fly.

%description mod_rewrite -l pl
Modu³ oferuj±cy mo¿liwo¶æ ,,przepisywania'' adresów URL w locie.

%package mod_status
Summary:	Server status report module for apache
Summary(pl):	Modu³ dostarczaj±cy informacje statystyczne o serwerze.
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_status
The Status module allows a server administrator to find out how well
their server is performing. A HTML page is presented that gives the
current server statistics in an easily readable form. If required this
page can be made to automatically refresh (given a compatible
browser).

%description mod_status -l pl
Modu³ pozwala administratorowi na przegl±danie statystyk dotycz±cych
pracy serwera apache (w postaci strony HTML).

%package mod_usertrack
Summary:	Apache module for user tracking using cookies
Summary(pl):	Modu³ s³u¿±cy do ¶ledzenia ,,ciasteczek''.
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_usertrack
This package contains the user tracking module which did its own
logging using CookieLog directory. This module allow multiple log
files.

%description mod_usertrack -l pl
Modu³ pozwalaj±cy na ¶ledzenie ,,ciasteczek''.

%package mod_vhost_alias
Summary:	Apache module for dynamically configured mass virtual hosting
Summary(pl):	Modu³ dodaj±cy obs³ugê hostów wirtualnych.
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_vhost_alias
This package contains the mod_vhost_alias. It provides support for
dynamically configured mass virtual hosting.

%description mod_vhost_alias -l pl
Modu³ umo¿liwia na dynamiczne konfigurowanie masowej ilo¶ci serwerów
wirtualnych.

%package mod_unique_id
Summary:	Apache module which provides a magic token for each request
Summary(pl):	Modu³ nadaj±cy ka¿demu ¿±daniu unikalny token
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_unique_id
This package contains the mod_unique_id. This module provides a magic
token for each request which is guaranteed to be unique across "all"
requests under very specific conditions. The unique identifier is even
unique across multiple machines in a properly configured cluster of
machines. The environment variable UNIQUE_ID is set to the identifier
for each request. Unique identifiers are useful for various reasons
which are beyond the scope of this document.

%description mod_unique_id -l pl
Modu³ nadaje przy ka¿dym ¿±daniu token unikalny w ramach wszystkich
¿±dañ, nawet w ramach poprawnie skonfigurowanego klastra z wielu
maszyn. Modu³ ustawia przy ka¿dym ¿±daniu zmienn± ¶rodowiskow±
UNIQUE_ID.

%package mod_expires
Summary:	Apache module which generates Expires HTTP headers
Summary(pl):	Modu³ generuj±cy nag³ówki HTTP Expires
Group:		Networking/Daemons
Prereq:		%{_sbindir}/apxs
Prereq:		perl
Requires:	%{name}(EAPI) = %{version}

%description mod_expires
This module controls the setting of the Expires HTTP header in server
responses. The expiration date can set to be relative to either the
time the source file was last modified, or to the time of the client
access.

%description mod_expires -l pl
Modu³ kontroluje ustawianie nag³ówka HTTP Expires. Data wyga¶niêcia
wa¿no¶ci mo¿e byæ ustalana w zale¿no¶ci od czasu modyfikacji plików
¼ród³owych lub odwo³ania klienta.

%prep
%setup -q -n apache_%{version} -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p1
%patch8 -p1
%{!?_without_ipv6:%patch9 -p1}
%patch10 -p1
%patch11 -p1
%patch12 -p1
%{?_with_rewrite_ldap:%patch13 -p1}
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%{?_without_ipv6:%patch19 -p1}
%patch20 -p1
%patch21 -p1

%build
OPTIM="%{rpmcflags} -DHARD_SERVER_LIMIT=2048" \
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--includedir=%{_includedir} \
	--sbindir=%{_sbindir} \
	--libexecdir=%{_libexecdir} \
	--datadir=%{_datadir} \
	--manualdir=%{_datadir}/html/manual \
	--localstatedir=/var \
	--runtimedir=/var/run \
	--logfiledir=/var/log/httpd \
	--with-layout=PLD \
	--without-confadjust \
	--enable-module=all \
	--enable-module=auth_digest \
	--enable-shared=max \
	--proxycachedir=/var/cache/apache \
	--with-perl=%{_bindir}/perl \
	--enable-suexec \
	--suexec-caller=http \
	--suexec-uidmin=500 \
	--suexec-gidmin=500 \
	--suexec-docroot=%{_datadir} \
	--disable-rule=WANTHSREGEX \
	--enable-rule=EAPI \
	%{!?_without_ipv6:--enable-rule=INET6}

%{__make} LIBS1="-lm -lcrypt -lmm -ldl"

rm -f src/modules/standard/mod_auth_db.so
%{__make} -C src/modules/standard mod_auth_db.so \
	LIBS_SHLIB="-ldb"

rm -f src/modules/standard/mod_rewrite.so
%{__make} -C src/modules/standard mod_rewrite.so \
	LIBS_SHLIB="-ldb %{?_with_rewrite_ldap:-lldap -llber}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT%{_datadir}/errordocs \
	$RPM_BUILD_ROOT/var/{log/{httpd,archiv/httpd},run/apache}

%{__make} install-quiet \
	root="$RPM_BUILD_ROOT"

mv -f $RPM_BUILD_ROOT%{_datadir}/html/manual $RPM_BUILD_ROOT%{_datadir}

install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/apache
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/apache
bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

touch $RPM_BUILD_ROOT/var/log/httpd/{access,error,agent,referer}_log

install errordocs/* $RPM_BUILD_ROOT%{_datadir}/errordocs

install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf

install %{SOURCE8}  $RPM_BUILD_ROOT%{_sysconfdir}/mod_vhost_alias.conf
install %{SOURCE9}  $RPM_BUILD_ROOT%{_sysconfdir}/mod_status.conf
install %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/mod_proxy.conf

ln -sf index.html.en $RPM_BUILD_ROOT%{_datadir}/html/index.html

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid http`" ]; then
	if [ "`getgid http`" != "51" ]; then
		echo "Error: group http doesn't have gid=51. Correct this before installing apache." 1>&2
		exit 1
	fi
else
	echo "Adding group http GID=51."
	/usr/sbin/groupadd -g 51 -r -f http
fi
if [ -n "`id -u http 2>/dev/null`" ]; then
	if [ "`id -u http`" != "51" ]; then
		echo "Error: user http doesn't have uid=51. Correct this before installing apache." 1>&2
		exit 1
	fi
else
	echo "Adding user http UID=51."
	/usr/sbin/useradd -u 51 -r -d /home/httpd -s /bin/false -c "HTTP User" -g http http 1>&2
fi

%post
/sbin/chkconfig --add httpd
%{apxs} -e -a -n access %{_libexecdir}/mod_access.so 1>&2
%{apxs} -e -a -n alias %{_libexecdir}/mod_alias.so 1>&2
%{apxs} -e -a -n asis %{_libexecdir}/mod_asis.so 1>&2
%{apxs} -e -a -n autoindex %{_libexecdir}/mod_autoindex.so 1>&2
%{apxs} -e -a -n cern_meta %{_libexecdir}/mod_cern_meta.so 1>&2
%{apxs} -e -a -n cgi %{_libexecdir}/mod_cgi.so 1>&2
%{apxs} -e -a -n env %{_libexecdir}/mod_env.so 1>&2
%{apxs} -e -a -n include %{_libexecdir}/mod_include.so 1>&2
%{apxs} -e -a -n log_agent %{_libexecdir}/mod_log_agent.so 1>&2
%{apxs} -e -a -n log_config %{_libexecdir}/mod_log_config.so 1>&2
%{apxs} -e -a -n log_referer %{_libexecdir}/mod_log_referer.so 1>&2
%{apxs} -e -a -n mime_magic %{_libexecdir}/mod_mime_magic.so 1>&2
%{apxs} -e -a -n mime %{_libexecdir}/mod_mime.so 1>&2
%{apxs} -e -a -n negotiation %{_libexecdir}/mod_negotiation.so 1>&2
%{apxs} -e -a -n setenvif %{_libexecdir}/mod_setenvif.so 1>&2
%{apxs} -e -a -n speling %{_libexecdir}/mod_speling.so 1>&2
%{apxs} -e -a -n userdir %{_libexecdir}/mod_userdir.so 1>&2
umask 137
touch /var/log/httpd/{access,error,agent,referer}_log
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n access %{_libexecdir}/mod_access.so 1>&2
	%{apxs} -e -A -n alias %{_libexecdir}/mod_alias.so 1>&2
	%{apxs} -e -A -n asis %{_libexecdir}/mod_asis.so 1>&2
	%{apxs} -e -A -n autoindex %{_libexecdir}/mod_autoindex.so 1>&2
	%{apxs} -e -A -n cern_meta %{_libexecdir}/mod_cern_meta.so 1>&2
	%{apxs} -e -A -n cgi %{_libexecdir}/mod_cgi.so 1>&2
	%{apxs} -e -A -n env %{_libexecdir}/mod_env.so 1>&2
	%{apxs} -e -A -n include %{_libexecdir}/mod_include.so 1>&2
	%{apxs} -e -A -n log_agent %{_libexecdir}/mod_log_agent.so 1>&2
	%{apxs} -e -A -n log_config %{_libexecdir}/mod_log_config.so 1>&2
	%{apxs} -e -A -n log_referer %{_libexecdir}/mod_log_referer.so 1>&2
	%{apxs} -e -A -n mime %{_libexecdir}/mod_mime.so 1>&2
	%{apxs} -e -A -n mime_magic %{_libexecdir}/mod_mime_magic.so 1>&2
	%{apxs} -e -A -n negotiation %{_libexecdir}/mod_negotiation.so 1>&2
	%{apxs} -e -A -n setenvif %{_libexecdir}/mod_setenvif.so 1>&2
	%{apxs} -e -A -n speling %{_libexecdir}/mod_speling.so 1>&2
	%{apxs} -e -A -n userdir %{_libexecdir}/mod_userdir.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd stop 1>&2
	fi
	/sbin/chkconfig --del httpd
fi

%postun
if [ "$1" = "0" ]; then
	echo "Removing user http."
	/usr/sbin/userdel http
	echo "Removing group http."
	/usr/sbin/groupdel http
fi

%post mod_actions
%{apxs} -e -a -n actions %{_libexecdir}/mod_actions.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_actions
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n actions %{_libexecdir}/mod_actions.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_auth
%{apxs} -e -a -n auth %{_libexecdir}/mod_auth.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_auth
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n auth %{_libexecdir}/mod_auth.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_auth_anon
%{apxs} -e -a -n auth_anon %{_libexecdir}/mod_auth_anon.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_auth_anon
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n auth_anon %{_libexecdir}/mod_auth_anon.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_auth_db
%{apxs} -e -a -n auth_db %{_libexecdir}/mod_auth_db.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_auth_db
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n auth_db %{_libexecdir}/mod_auth_db.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_auth_digest
%{apxs} -e -a -n auth_digest %{_libexecdir}/mod_auth_digest.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_auth_digest
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n auth_digest %{_libexecdir}/mod_auth_digest.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%triggerpostun mod_auth_db -- apache-mod_auth_db <= 1.3.20-2
%{apxs} -e -A -n auth_dbm %{_libexecdir}/mod_auth_dbm.so 1>&2

%post mod_define
%{apxs} -e -a -n define %{_libexecdir}/mod_define.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_define
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n define %{_libexecdir}/mod_define.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_digest
%{apxs} -e -a -n digest %{_libexecdir}/mod_digest.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_digest
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n digest %{_libexecdir}/mod_digest.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_dir
%{apxs} -e -a -n dir %{_libexecdir}/mod_dir.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_dir
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n dir %{_libexecdir}/mod_dir.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_expires
%{apxs} -e -a -n expires %{_libexecdir}/mod_expires.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_expires
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n expires %{_libexecdir}/mod_expires.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_headers
%{apxs} -e -a -n headers %{_libexecdir}/mod_headers.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_headers
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n headers %{_libexecdir}/mod_headers.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_mmap_static
%{apxs} -e -a -n mmap_static %{_libexecdir}/mod_mmap_static.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_mmap_static
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n mmap_static %{_libexecdir}/mod_mmap_static.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_imap
%{apxs} -e -a -n imap %{_libexecdir}/mod_imap.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_imap
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n imap %{_libexecdir}/mod_imap.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_info
%{apxs} -e -a -n info %{_libexecdir}/mod_info.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_info
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n info %{_libexecdir}/mod_info.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_proxy
%{apxs} -e -a -n proxy %{_libexecdir}/libproxy.so 1>&2
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*mod_proxy.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/mod_proxy.conf" >> /etc/httpd/httpd.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_proxy
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n proxy %{_libexecdir}/libproxy.so 1>&2
	grep -v "^Include.*mod_proxy.conf" /etc/httpd/httpd.conf > \
		/etc/httpd/httpd.conf.tmp
	mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_rewrite
%{apxs} -e -a -n rewrite %{_libexecdir}/mod_rewrite.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_rewrite
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n rewrite %{_libexecdir}/mod_rewrite.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_status
%{apxs} -e -a -n status %{_libexecdir}/mod_status.so 1>&2
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*mod_status.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/mod_status.conf" >> /etc/httpd/httpd.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_status
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n status %{_libexecdir}/mod_status.so 1>&2
	grep -v "^Include.*mod_status.conf" /etc/httpd/httpd.conf > \
		/etc/httpd/httpd.conf.tmp
	mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_usertrack
%{apxs} -e -a -n usertrack %{_libexecdir}/mod_usertrack.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_usertrack
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n usertrack %{_libexecdir}/mod_usertrack.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_unique_id
%{apxs} -e -a -n unique_id %{_libexecdir}/mod_unique_id.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_unique_id
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n unique_id %{_libexecdir}/mod_unique_id.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%post mod_vhost_alias
%{apxs} -e -a -n vhost_alias %{_libexecdir}/mod_vhost_alias.so 1>&2
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*mod_vhost_alias.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/mod_vhost_alias.conf" >> /etc/httpd/httpd.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun mod_vhost_alias
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n vhost_alias %{_libexecdir}/mod_vhost_alias.so 1>&2
	grep -v "^Include.*mod_vhost_alias.conf" /etc/httpd/httpd.conf > \
		/etc/httpd/httpd.conf.tmp
	mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc ABOUT_APACHE src/CHANGES README
%doc conf/mime.types

%attr(754,root,root) /etc/rc.d/init.d/httpd

%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %{_sysconfdir}/magic

%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/*
%attr(640,root,root) %config(noreplace) /etc/logrotate.d/*

%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/mod_access.so
%attr(755,root,root) %{_libexecdir}/mod_alias.so
%attr(755,root,root) %{_libexecdir}/mod_asis.so
%attr(755,root,root) %{_libexecdir}/mod_autoindex.so
%attr(755,root,root) %{_libexecdir}/mod_cern_meta.so
%attr(755,root,root) %{_libexecdir}/mod_cgi.so
%attr(755,root,root) %{_libexecdir}/mod_env.so
%attr(755,root,root) %{_libexecdir}/mod_include.so
%attr(755,root,root) %{_libexecdir}/mod_log_agent.so
%attr(755,root,root) %{_libexecdir}/mod_log_config.so
%attr(755,root,root) %{_libexecdir}/mod_log_referer.so
%attr(755,root,root) %{_libexecdir}/mod_mime.so
%attr(755,root,root) %{_libexecdir}/mod_mime_magic.so
%attr(755,root,root) %{_libexecdir}/mod_negotiation.so
%attr(755,root,root) %{_libexecdir}/mod_setenvif.so
%attr(755,root,root) %{_libexecdir}/mod_speling.so
%attr(755,root,root) %{_libexecdir}/mod_userdir.so

%attr(755,root,root) %{_bindir}/checkgid
%attr(755,root,root) %{_bindir}/htdigest

%attr(755,root,root) %{_sbindir}/ab
%attr(755,root,root) %{_sbindir}/apachectl
%attr(755,root,root) %{_sbindir}/apxs
%attr(755,root,root) %{_sbindir}/httpd
%attr(755,root,root) %{_sbindir}/logresolve
%attr(755,root,root) %{_sbindir}/rotatelogs

%dir %attr(1773,root,http) /var/run/apache

%{_mandir}/man1/htdigest.1*
%{_mandir}/man8/*
%lang(hu) %{_mandir}/hu/man8/*
%lang(ko) %{_mandir}/ko/man8/*
%lang(pl) %{_mandir}/pl/man8/*

%attr(750,root,root) %dir /var/log/httpd
%attr(750,root,root) %dir /var/log/archiv/httpd
%attr(640,root,root) %ghost /var/log/httpd/*

%dir %{_datadir}
%dir %{_datadir}/manual
%dir %{_datadir}/manual/images/
%{_datadir}/manual/images/apache_header.gif
%{_datadir}/manual/images/custom_errordocs.gif
%{_datadir}/manual/images/home.gif
%{_datadir}/manual/images/index.gif
%{_datadir}/manual/images/pixel.gif
%{_datadir}/manual/images/sub.gif
%{_datadir}/manual/misc
%dir %{_datadir}/manual/search
%attr(755,root,root) %{_datadir}/manual/search/manual-index.cgi
%{_datadir}/manual/LICENSE
%{_datadir}/manual/bind.html.html
%{_datadir}/manual/bind.html.en
%lang(fr) %{_datadir}/manual/bind.html.fr
%lang(ja) %{_datadir}/manual/bind.html.ja.jis
%{_datadir}/manual/cgi_path.html.html
%{_datadir}/manual/cgi_path.html.en
%lang(fr) %{_datadir}/manual/cgi_path.html.fr
%lang(ja) %{_datadir}/manual/cgi_path.html.ja.jis
%{_datadir}/manual/configuring.html.html
%{_datadir}/manual/configuring.html.en
%lang(fr) %{_datadir}/manual/configuring.html.fr
%lang(ja) %{_datadir}/manual/configuring.html.ja.jis
%{_datadir}/manual/content-negotiation.html.html
%{_datadir}/manual/content-negotiation.html.en
%lang(ja) %{_datadir}/manual/content-negotiation.html.ja.jis
%{_datadir}/manual/custom-error.html.html
%{_datadir}/manual/custom-error.html.en
%lang(fr) %{_datadir}/manual/custom-error.html.fr
%lang(ja) %{_datadir}/manual/custom-error.html.ja.jis
%{_datadir}/manual/dns-caveats.html.html
%{_datadir}/manual/dns-caveats.html.en
%lang(fr) %{_datadir}/manual/dns-caveats.html.fr
%{_datadir}/manual/dso.html
%{_datadir}/manual/env.html.html
%{_datadir}/manual/env.html.en
%lang(ja) %{_datadir}/manual/env.html.ja.jis
%{_datadir}/manual/footer.html
%{_datadir}/manual/handler.html.html
%{_datadir}/manual/handler.html.en
%lang(ja) %{_datadir}/manual/handler.html.ja.jis
%{_datadir}/manual/header.html
%{_datadir}/manual/index.html.html
%{_datadir}/manual/index.html.en
%lang(fr) %{_datadir}/manual/index.html.fr
%lang(ja) %{_datadir}/manual/index.html.ja.jis
%{_datadir}/manual/install.html.html
%{_datadir}/manual/install.html.en
%lang(es) %{_datadir}/manual/install.html.es
%lang(fr) %{_datadir}/manual/install.html.fr
%lang(ja) %{_datadir}/manual/install.html.ja.jis
%{_datadir}/manual/invoking.html.html
%{_datadir}/manual/invoking.html.en
%lang(fr) %{_datadir}/manual/invoking.html.fr
%{_datadir}/manual/keepalive.html.html
%{_datadir}/manual/keepalive.html.en
%lang(ja) %{_datadir}/manual/keepalive.html.ja.jis
%{_datadir}/manual/location.html
%{_datadir}/manual/logs.html
%{_datadir}/manual/multilogs.html
%{_datadir}/manual/new_features_1_3.html.html
%{_datadir}/manual/new_features_1_3.html.en
%lang(ja) %{_datadir}/manual/new_features_1_3.html.ja.jis
%{_datadir}/manual/process-model.html.html
%{_datadir}/manual/process-model.html.en
%lang(ja) %{_datadir}/manual/process-model.html.ja.jis
%{_datadir}/manual/sections.html.html
%{_datadir}/manual/sections.html.en
%lang(ja) %{_datadir}/manual/sections.html.ja.jis
%{_datadir}/manual/server-wide.html.html
%{_datadir}/manual/server-wide.html.en
%lang(fr) %{_datadir}/manual/server-wide.html.fr
%lang(ja) %{_datadir}/manual/server-wide.html.ja.jis
%{_datadir}/manual/sitemap.html
%{_datadir}/manual/sourcereorg.html
%{_datadir}/manual/stopping.html.html
%{_datadir}/manual/stopping.html.en
%lang(fr) %{_datadir}/manual/stopping.html.fr
%{_datadir}/manual/upgrading_to_1_3.html
%{_datadir}/manual/urlmapping.html
%dir %{_datadir}/manual/howto
%{_datadir}/manual/howto/cgi.html.html
%{_datadir}/manual/howto/cgi.html.en
%lang(ja) %{_datadir}/manual/howto/cgi.html.ja.jis
%{_datadir}/manual/howto/footer.html
%{_datadir}/manual/howto/header.html
%{_datadir}/manual/howto/htaccess.html
%{_datadir}/manual/howto/ssi.html.html
%{_datadir}/manual/howto/ssi.html.en
%lang(ja) %{_datadir}/manual/howto/ssi.html.ja.jis
%dir %{_datadir}/manual/mod
%{_datadir}/manual/mod/core.html.html
%{_datadir}/manual/mod/core.html.en
%lang(fr) %{_datadir}/manual/mod/core.html.fr
%lang(ja) %{_datadir}/manual/mod/core.html.ja.jis
%{_datadir}/manual/mod/directive-dict.html.html
%{_datadir}/manual/mod/directive-dict.html.en
%lang(fr) %{_datadir}/manual/mod/directive-dict.html.fr
%lang(ja) %{_datadir}/manual/mod/directive-dict.html.ja.jis
%{_datadir}/manual/mod/directives.html.html
%lang(de) %{_datadir}/manual/mod/directives.html.de
%{_datadir}/manual/mod/directives.html.en
%lang(fr) %{_datadir}/manual/mod/directives.html.fr
%lang(ja) %{_datadir}/manual/mod/directives.html.ja.jis
%{_datadir}/manual/mod/footer.html
%{_datadir}/manual/mod/header.html
%{_datadir}/manual/mod/index-bytype.html.html
%{_datadir}/manual/mod/index-bytype.html.en
%lang(fr) %{_datadir}/manual/mod/index-bytype.html.fr
%lang(ja) %{_datadir}/manual/mod/index-bytype.html.ja.jis
%{_datadir}/manual/mod/index.html.html
%{_datadir}/manual/mod/index.html.en
%lang(fr) %{_datadir}/manual/mod/index.html.fr
%lang(ja) %{_datadir}/manual/mod/index.html.ja.jis
%{_datadir}/manual/mod/mod_access.html.html
%{_datadir}/manual/mod/mod_access.html.en
%lang(ja) %{_datadir}/manual/mod/mod_access.html.ja.jis
%{_datadir}/manual/mod/mod_alias.html.html
%{_datadir}/manual/mod/mod_alias.html.en
%lang(ja) %{_datadir}/manual/mod/mod_alias.html.ja.jis
%{_datadir}/manual/mod/mod_asis.html.html
%{_datadir}/manual/mod/mod_asis.html.en
%lang(ja) %{_datadir}/manual/mod/mod_asis.html.ja.jis
%{_datadir}/manual/mod/mod_autoindex.html
%{_datadir}/manual/mod/mod_cern_meta.html
%{_datadir}/manual/mod/mod_cgi.html.html
%{_datadir}/manual/mod/mod_cgi.html.en
%lang(ja) %{_datadir}/manual/mod/mod_cgi.html.ja.jis
%{_datadir}/manual/mod/mod_env.html.html
%{_datadir}/manual/mod/mod_env.html.en
%lang(ja) %{_datadir}/manual/mod/mod_env.html.ja.jis
%{_datadir}/manual/mod/mod_include.html
%{_datadir}/manual/mod/mod_log_agent.html
%{_datadir}/manual/mod/mod_log_config.html.html
%{_datadir}/manual/mod/mod_log_config.html.en
%lang(ja) %{_datadir}/manual/mod/mod_log_config.html.ja.jis
%{_datadir}/manual/mod/mod_log_referer.html
%{_datadir}/manual/mod/mod_mime.html.html
%{_datadir}/manual/mod/mod_mime.html.en
%lang(ja) %{_datadir}/manual/mod/mod_mime.html.ja.jis
%{_datadir}/manual/mod/mod_mime_magic.html
%{_datadir}/manual/mod/mod_negotiation.html.html
%{_datadir}/manual/mod/mod_negotiation.html.en
%lang(ja) %{_datadir}/manual/mod/mod_negotiation.html.ja.jis
%{_datadir}/manual/mod/mod_setenvif.html.html
%{_datadir}/manual/mod/mod_setenvif.html.en
%lang(ja) %{_datadir}/manual/mod/mod_setenvif.html.ja.jis
%{_datadir}/manual/mod/mod_so.html.html
%{_datadir}/manual/mod/mod_so.html.en
%lang(ja) %{_datadir}/manual/mod/mod_so.html.ja.jis
%{_datadir}/manual/mod/mod_speling.html.html
%{_datadir}/manual/mod/mod_speling.html.en
%lang(ja) %{_datadir}/manual/mod/mod_speling.html.ja.jis
%{_datadir}/manual/mod/mod_userdir.html.html
%{_datadir}/manual/mod/mod_userdir.html.en
%lang(ja) %{_datadir}/manual/mod/mod_userdir.html.ja.jis
%{_datadir}/manual/mod/module-dict.html.html
%{_datadir}/manual/mod/module-dict.html.en
%lang(ja) %{_datadir}/manual/mod/module-dict.html.ja.jis
%dir %{_datadir}/manual/programs
%{_datadir}/manual/programs/ab.html
%{_datadir}/manual/programs/apachectl.html.html
%{_datadir}/manual/programs/apachectl.html.en
%lang(ja) %{_datadir}/manual/programs/apachectl.html.ja.jis
%{_datadir}/manual/programs/apxs.html
%{_datadir}/manual/programs/dbmmanage.html
%{_datadir}/manual/programs/footer.html
%{_datadir}/manual/programs/header.html
%{_datadir}/manual/programs/htdigest.html
%{_datadir}/manual/programs/htpasswd.html.html
%{_datadir}/manual/programs/htpasswd.html.en
%lang(ja) %{_datadir}/manual/programs/htpasswd.html.ja.jis
%{_datadir}/manual/programs/httpd.html.html
%{_datadir}/manual/programs/httpd.html.en
%lang(ja) %{_datadir}/manual/programs/httpd.html.ja.jis
%{_datadir}/manual/programs/index.html.html
%{_datadir}/manual/programs/index.html.en
%lang(ja) %{_datadir}/manual/programs/index.html.ja.jis
%{_datadir}/manual/programs/logresolve.html
%{_datadir}/manual/programs/other.html
%{_datadir}/manual/programs/rotatelogs.html
%dir %{_datadir}/manual/vhosts
%{_datadir}/manual/vhosts/details.html
%{_datadir}/manual/vhosts/examples.html
%{_datadir}/manual/vhosts/fd-limits.html.html
%{_datadir}/manual/vhosts/fd-limits.html.en
%lang(ja) %{_datadir}/manual/vhosts/fd-limits.html.ja.jis
%{_datadir}/manual/vhosts/footer.html
%{_datadir}/manual/vhosts/header.html
%{_datadir}/manual/vhosts/host.html
%{_datadir}/manual/vhosts/index.html.html
%{_datadir}/manual/vhosts/index.html.en
%lang(ja) %{_datadir}/manual/vhosts/index.html.ja.jis
%{_datadir}/manual/vhosts/ip-based.html
%{_datadir}/manual/vhosts/mass.html
%{_datadir}/manual/vhosts/name-based.html.html
%{_datadir}/manual/vhosts/name-based.html.en
%lang(ja) %{_datadir}/manual/vhosts/name-based.html.ja.jis
%{_datadir}/manual/vhosts/vhosts-in-depth.html
%{_datadir}/manual/vhosts/virtual-host.html

%attr(755,root,root) %dir %{_datadir}/html
%config(noreplace,missingok) %{_datadir}/html/index.html
# note: html extensions are not the same as (g)libc locale names
%lang(ca) %{_datadir}/html/index.html.ca
%lang(cs) %{_datadir}/html/index.html.cz
%lang(de) %{_datadir}/html/index.html.de
%lang(da) %{_datadir}/html/index.html.dk
%lang(et) %{_datadir}/html/index.html.ee
%lang(el) %{_datadir}/html/index.html.el
%{_datadir}/html/index.html.en
%lang(es) %{_datadir}/html/index.html.es
%lang(fr) %{_datadir}/html/index.html.fr
%lang(he) %{_datadir}/html/index.html.he.iso8859-8
%lang(it) %{_datadir}/html/index.html.it
%lang(ja) %{_datadir}/html/index.html.ja.jis
%lang(ko) %{_datadir}/html/index.html.kr.iso-kr
%lang(de_LU) %{_datadir}/html/index.html.lb.utf8
%lang(nl) %{_datadir}/html/index.html.nl
%lang(nn) %{_datadir}/html/index.html.nn
%lang(no) %{_datadir}/html/index.html.no
%lang(pl) %{_datadir}/html/index.html.po.iso-pl
%lang(pt) %{_datadir}/html/index.html.pt
%lang(pt_BR) %{_datadir}/html/index.html.pt-br
%lang(ru) %{_datadir}/html/index.html.ru.cp-1251
%lang(ru) %{_datadir}/html/index.html.ru.cp866
%lang(ru) %{_datadir}/html/index.html.ru.iso-ru
%lang(ru) %{_datadir}/html/index.html.ru.koi8-r
%lang(ru) %{_datadir}/html/index.html.ru.ucs2
%lang(ru) %{_datadir}/html/index.html.ru.ucs4
%lang(ru) %{_datadir}/html/index.html.ru.utf8
%lang(sv) %{_datadir}/html/index.html.se
%lang(zh_TW) %{_datadir}/html/index.html.zh-tw.big5

%{_datadir}/html/*.gif
%{_datadir}/errordocs
%dir %{_datadir}/icons
%{_datadir}/icons/*.gif
%{_datadir}/icons/*.png
%dir %{_datadir}/icons/small
%{_datadir}/icons/small/*.gif
%{_datadir}/icons/small/*.png
%attr(755,root,root) %{_datadir}/cgi-bin

%files suexec
%defattr(644,root,root,755)
%attr(4755,root,root) %{_sbindir}/suexec
%{_datadir}/manual/suexec.html.html
%{_datadir}/manual/suexec.html.en
%lang(ja) %{_datadir}/manual/suexec.html.ja.jis
%{_datadir}/manual/programs/suexec.html.html
%{_datadir}/manual/programs/suexec.html.en
%lang(ja) %{_datadir}/manual/programs/suexec.html.ja.jis

%files devel
%defattr(644,root,root,755)
%{_includedir}

%files mod_actions
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_actions.so
%{_datadir}/manual/mod/mod_actions.html.html
%{_datadir}/manual/mod/mod_actions.html.en
%lang(ja) %{_datadir}/manual/mod/mod_actions.html.ja.jis

%files mod_auth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_auth.so
%attr(755,root,root) %{_bindir}/htpasswd
%{_datadir}/manual/howto/auth.html
%{_datadir}/manual/mod/mod_auth.html.html
%{_datadir}/manual/mod/mod_auth.html.en
%lang(ja) %{_datadir}/manual/mod/mod_auth.html.ja.jis

%files mod_auth_anon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_auth_anon.so
%{_datadir}/manual/mod/mod_auth_anon.html

%files mod_auth_db
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_auth_db.so
%attr(755,root,root) %{_bindir}/dbmmanage
%{_datadir}/manual/mod/mod_auth_db.html
%{_mandir}/man1/dbmmanage.1*
%{_mandir}/man1/htpasswd.1*

%files mod_auth_digest
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_auth_digest.so
%{_datadir}/manual/mod/mod_auth_digest.html

%files mod_define
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_define.so
%{_datadir}/manual/mod/mod_define.html

%files mod_digest
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_digest.so
%{_datadir}/manual/mod/mod_digest.html

%files mod_dir
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_dir.so
%{_datadir}/manual/mod/mod_dir.html.html
%{_datadir}/manual/mod/mod_dir.html.en
%lang(ja) %{_datadir}/manual/mod/mod_dir.html.ja.jis

%files mod_expires
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_expires.so
%{_datadir}/manual/mod/mod_expires.html

%files mod_headers
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_headers.so
%{_datadir}/manual/mod/mod_headers.html

%files mod_mmap_static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_mmap_static.so
%{_datadir}/manual/mod/mod_mmap_static.html

%files mod_imap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_imap.so
%{_datadir}/manual/mod/mod_imap.html

%files mod_info
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_info.so
%{_datadir}/manual/mod/mod_info.html.html
%{_datadir}/manual/mod/mod_info.html.en
%lang(ja) %{_datadir}/manual/mod/mod_info.html.ja.jis

%files mod_proxy
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mod_proxy.conf
%attr(755,root,root) %{_libexecdir}/libproxy.so
%{_datadir}/manual/mod/mod_proxy.html
%dir %attr(770,root,http) /var/cache/apache

%files mod_rewrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_rewrite.so
%{_datadir}/manual/mod/mod_rewrite.html
%{_datadir}/manual/images/mod_rewrite*

%files mod_status
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mod_status.conf
%attr(755,root,root) %{_libexecdir}/mod_status.so
%{_datadir}/manual/mod/mod_status.html

%files mod_usertrack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_usertrack.so
%{_datadir}/manual/mod/mod_cookies.html
%{_datadir}/manual/mod/mod_usertrack.html

%files mod_unique_id
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_unique_id.so
%{_datadir}/manual/mod/mod_unique_id.html.html
%{_datadir}/manual/mod/mod_unique_id.html.en
%lang(ja) %{_datadir}/manual/mod/mod_unique_id.html.ja.jis

%files mod_vhost_alias
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_vhost_alias.so
%{_datadir}/manual/mod/mod_vhost_alias.html
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mod_vhost_alias.conf
