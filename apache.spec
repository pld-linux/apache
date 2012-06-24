# TODO:
# - config examples for mod_*
# - --with-suexec-gidmin=500 or =100 ?
# - --with-suexec-uidmin=500 or =1000 ?
# - subpackages for MPMs
# - !!!check if all modules (*.so) are exactly the same for different MPMs
# - check those autn modules inner deps
# - for external packages: don't use any apache module name in dep as they
#   differ for apache 1.3/2.0/2.2!? any better ideas? rpm Suggests: tags?
# - for mod_auth_* modules require each auth module to require virtual authn so at least *_default is chosen?
# - same for mod_authz
# - mod_auth_digest and mod_auth_basic R: apache(authn) ?
# - drop mod_case_filter* or find summary and description for them
# - build modules only once (not with each mpm)

# Conditional build:
%bcond_without	ssl		# build without SSL support
%bcond_without	ldap		# build without LDAP support
%bcond_without	metuxmpm	# metux MPM
%bcond_without	peruser		# peruser MPM
%bcond_without	event		# event MPM
%bcond_with     distcache	# distcache support
%bcond_with	bucketeer	# debug one
#
%include	/usr/lib/rpm/macros.perl
# this is internal macro, don't change to %%apache_modules_api
%define		_apache_modules_api 20051115
Summary:	The most widely used Web server on the Internet
Summary(de):	Leading World Wide Web-Server
Summary(es):	Servidor HTTPD para proveer servicios WWW
Summary(fr):	Le serveur web le plus utilise sur Internet
Summary(pl):	Serwer WWW (World Wide Web)
Summary(pt_BR):	Servidor HTTPD para prover servi�os WWW
Summary(ru):	����� ���������� ���-������
Summary(tr):	Lider WWW taray�c�
Name:		apache
Version:	2.2.3
Release:	6
License:	Apache Group License
Group:		Networking/Daemons
Source0:	http://www.apache.org/dist/httpd/httpd-%{version}.tar.gz
# Source0-md5:	f72ffb176e2dc7b322be16508c09f63c
Source1:	%{name}.init
Source2:	%{name}.logrotate
Source3:	%{name}-icons.tar.gz
# Source3-md5:	2b085cbc19fd28536dc883f0b864cd83
Source4:	%{name}.sysconfig
Source5:	%{name}.monitrc
Source6:	%{name}-httpd.conf
Source7:	%{name}-common.conf
Source8:	%{name}-mod_vhost_alias.conf
Source9:	%{name}-mod_status.conf
Source10:	%{name}-mod_proxy.conf
Source11:	%{name}-mod_info.conf
Source12:	%{name}-mod_ssl.conf
Source13:	%{name}-mod_dav.conf
Source14:	%{name}-mod_dir.conf
Source15:	%{name}-mod_suexec.conf
Source16:	%{name}-mod_deflate.conf
Source17:	%{name}-mod_autoindex.conf
Source18:	%{name}-multilang-errordoc.conf
Source19:	%{name}-manual.conf
Source20:	%{name}-server.crt
Source21:	%{name}-server.key
Source22:	%{name}-mod_userdir.conf
Source23:	%{name}-mpm.conf
Source24:	%{name}-languages.conf
Source25:	%{name}-mod_mime.conf
Source27:	%{name}-mod_authz_host.conf
Source28:	%{name}-mod_cgid.conf
Source29:	%{name}-mod_log_config.conf
Source30:	%{name}-mod_mime_magic.conf
Source31:	%{name}-mod_cache.conf
Patch0:		%{name}-configdir_skip_backups.patch
Patch1:		%{name}-layout.patch
Patch2:		%{name}-suexec.patch
Patch4:		%{name}-apr.patch
# project homepage http://www.metux.de/mpm/en/?patpage=index
# http://www.sannes.org/metuxmpm/
Patch5:		httpd-2.0.48-metuxmpm-r8.patch
# what about this? it isn't applied...
Patch6:		httpd-2.0.40-xfsz.patch
Patch7:		%{name}-syslibs.patch
Patch8:		httpd-2.0.45-encode.patch
Patch9:		%{name}-paths.patch
Patch10:	httpd-2.0.46-dav401dest.patch
Patch12:	httpd-2.0.46-sslmutex.patch
Patch14:	httpd-2.0.48-corelimit.patch
Patch15:	httpd-2.0.48-debuglog.patch
Patch18:	%{name}-v6only-ENOPROTOOPT.patch
Patch19:	%{name}-conffile-path.patch
Patch20:	%{name}-apxs.patch
# http://www.telana.com/peruser.php
Patch21:	httpd-2.0.52-peruser-0.1.6.patch
Patch22:	%{name}-libtool.patch
Patch23:	%{name}-revert-bug-40463.patch
URL:		http://httpd.apache.org/
BuildRequires:	apr-devel >= 1:1.2
BuildRequires:	apr-util-devel >= 1:1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
%{?with_distcache:BuildRequires:	distcache-devel}
BuildRequires:	expat-devel
BuildRequires:	gdbm-devel >= 1.8.3
BuildRequires:	libtool >= 2:1.5
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_ssl:BuildRequires:	openssl-tools >= 0.9.7d}
BuildRequires:	pcre-devel
BuildRequires:	rpm-build >= 4.4.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
# packages that were in apache-2.0.rpm, for compatibility
Requires:	%{name}-errordocs = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Requires:	%{name}-mod_asis = %{version}-%{release}
Requires:	%{name}-mod_auth = %{version}-%{release}
Requires:	%{name}-mod_cern_meta = %{version}-%{release}
Requires:	%{name}-mod_cgi = %{version}-%{release}
Requires:	%{name}-mod_env = %{version}-%{release}
Requires:	%{name}-mod_include = %{version}-%{release}
Requires:	%{name}-mod_log_config = %{version}-%{release}
Requires:	%{name}-mod_mime = %{version}-%{release}
Requires:	%{name}-mod_mime_magic = %{version}-%{release}
Requires:	%{name}-mod_negotiation = %{version}-%{release}
Requires:	%{name}-mod_setenvif = %{version}-%{release}
Requires:	%{name}-mod_speling = %{version}-%{release}
Requires:	%{name}-mod_userdir = %{version}-%{release}
Requires:	%{name}-mod_version = %{version}-%{release}
Requires:	%{name}-tools = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/httpd
%define		_includedir	%{_prefix}/include/apache
%define		_datadir	/home/services/httpd
%define		_libexecdir	%{_libdir}/apache
%define		_cgibindir	%{_prefix}/lib/cgi-bin/%{name}

%description
Apache is a powerful, full-featured, efficient and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

%description -l de
Apache ist ein voll funktionsf�higer Web-Server, der kostenlos
erh�ltlich und weit verbreitet ist.

%description -l es
El servidor web Apache es el mejor servidor gratuito disponible en el
mundo UNIX hoy. Usa HTTP (HyperText Transfer Protocol) para permitir
que navegadores vean documentos y sometan datos remotamente. Puede
ejecutar varias funciones diferentes, incluyendo funciones de proxy y
cach�, y nos ofrece caracter�sticas como monitor de estado, conversi�n
din�mica de tipo, y otras m�s.

%description -l fr
Apache est un serveur Web puissant, efficace, gratuit et complet.
Apache est aussi le serveur Web le plus populaire sur Internet.

%description -l pl
Apache jest serwerem WWW (World Wide Web). Instaluj�c ten pakiet
b�dziesz m�g� prezentowa� w�asne strony WWW w sieci Internet.

%description -l pt_BR
O servidor web Apache � o melhor servidor gratuito dispon�vel no mundo
UNIX hoje. Ele usa HTTP (HyperText Transfer Protocol) para permitir
que browsers web vejam documentos e submetam dados remotamente. Ele
pode executar v�rias fun��es diferentes, incluindo fun��es de proxy e
cache, e oferece caracter�sticas como monitor de status, convers�o
din�mica de tipo, e mais.

%description -l ru
Apache - ������, ��������������, ���������������������� � ��������
���������������� ���-������.

%description -l tr
Apache serbest da��t�lan ve �ok kullan�lan yetenekli bir web
sunucusudur.

%package base
Summary:	The Number One HTTP Server On The Internet
Summary(pl):	Wiod�cy w Internecie serwer HTTP
Group:		Networking/Daemons
Requires(post):	fileutils
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	/etc/mime.types
Requires:	/sbin/chkconfig
Requires:	apr >= 1:1.2
Requires:	mailcap
Requires:	psmisc >= 20.1
Requires:	rc-scripts >= 0.4.0.15
Provides:	apache(modules-api) = %{_apache_modules_api}
Provides:	group(http)
Provides:	user(http)
Provides:	webserver = apache
Obsoletes:	apache-extra
Obsoletes:	apache6
# packaged by mistake. really sample code
Obsoletes:	apache-mod_optional_fn_export
Obsoletes:	apache-mod_optional_fn_import
Obsoletes:	apache-mod_optional_fn_import
Obsoletes:	apache-mod_optional_hook_import
Conflicts:	apache < 2.2.0
# for the posttrans scriptlet, conflicts because in vserver environment rpm package is not installed.
Conflicts:	rpm < 4.4.2-0.2

%description base
Apache is a powerful, full-featured, efficient and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

%description base -l pl
Apache jest pot�nym, w pe�ni funkcjonalnym, wydajnym i wolnodost�pnym
serwerem WWW (World Wide Web). Jest tak�e najbardziej popularnym
serwerem WWW w Internecie.

%package suexec
Summary:	Apache suexec wrapper
Summary(pl):	Wrapper suexec do serwera WWW Apache
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/suexec.html
Requires:	%{name}-base = %{version}-%{release}

%description suexec
The suEXEC feature provides Apache users the ability to run CGI and
SSI programs under user IDs different from the user ID of the calling
web-server. Normally, when a CGI or SSI program executes, it runs as
the same user who is running the web server.

%description suexec -l pl
SuEXEC umo�liwia serwerowi Apache uruchamianie program�w CGI i SSI z
innym UID ni� wywo�uj�cy je serwer. Normalnie programy CGI i SSI s�
wykonywane jako taki sam u�ytkownik jak serwer WWW.

%package tools
Summary:	Apache tools
Summary(pl):	Narz�dzia Apache'a
Group:		Development/Tools

%description tools
Apache tools.

%description tools -l pl
Narz�dzia Apache'a.

%package index
Summary:	Apache index.html* files
Summary(pl):	Pliki Apache index.html*
Group:		Documentation
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	indexhtml

%description index
Apache index.html* files.

%description index -l pl
Pliki index.html* Apache'a.

%package doc
Summary:	Apache manual
Summary(pl):	Podr�cznik Apache'a
Group:		Documentation
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Requires:	%{name}-mod_dir = %{version}-%{release}
Requires:	%{name}-mod_negotiation = %{version}-%{release}
Requires:	%{name}-mod_setenvif = %{version}-%{release}

%description doc
Apache manual.

%description doc -l pl
Podr�cznik Apache'a.

%package errordocs
Summary:	Multi-language error messages for Apache
Summary(pl):	Wieloj�zyczne komunikaty b��d�w dla Apache'a
Group:		Applications/WWW
URL:		http://httpd.apache.org/docs-project/
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Requires:	%{name}-mod_authz_host = %{version}-%{release}
Requires:	%{name}-mod_include = %{version}-%{release}
Requires:	%{name}-mod_negotiation = %{version}-%{release}

%description errordocs
Multi-language error messages.

%description errordocs -l pl
Dokumenty opisuj�ce b��dy HTTP dla Apache'a w wielu j�zykach.

%package apxs
Summary:	APache eXtenSion tool
Summary(pl):	Narz�dzie do rozszerzania Apache'a
Group:		Development/Tools
Requires:	apr-devel

%description apxs
APache eXtenSion tool.

%description apxs -l pl
Narz�dzie do rozszerzania Apache'a.

%package devel
Summary:	Module development tools for the Apache web server
Summary(es):	Archivos de inclusi�n del Apache para desarrollo de m�dulos
Summary(fr):	Les outils de developpement de modules pour le serveur web Apache
Summary(pl):	Pliki nag��wkowe do tworzenia modu��w rozszerze� do serwera WWW Apache
Summary(pt_BR):	Arquivos de inclus�o do Apache para desenvolvimento de m�dulos
Summary(ru):	�������� ���������� ������� ��� ���-������� Apache
Group:		Networking/Utilities
Requires:	%{name}-apxs = %{version}-%{release}
Requires:	apr-util-devel >= 1:1.2
Requires:	libtool
Obsoletes:	apache-static

%description devel
The apache-devel package contains header files for Apache.

%description devel -l es
Este paquete contiene los archivos de inclusi�n para el Apache, bien
como el utilitario apxs para la construcci�n de objetos compartidos
din�micos (DSOs). Ha ce falta instalar este paquete si deseas compilar
o desarrollar m�dulos adicionales para Apache.

%description devel -l fr
Le package apache-devel contient le code source pour le serveur Web
Apache et le binaire APXS dont vous aurez besoin pour construire des
Objets Dynamiques Partages (DSOs) pour Apache.

%description devel -l pl
Pliki nag��wkowe i inne zasoby niezb�dne przy budowaniu modu��w DSO
(Dynamic Shared Objects) dla Apache'a.

%description devel -l ru
�������� ���������� ������� ��� ���-������� Apache.

%description devel -l pt_BR
Este pacote contem os arquivos de inclus�o para o Apache, bem como o
utilit�rio apxs para a constru��o de objetos compartilhados din�micos
(DSOs). Este pacote precisa ser instalado se voc� deseja compilar ou
desenvolver m�dulos adicionais para o Apache.

%package mod_actions
Summary:	Apache module for executing CGI scripts based on media type or request method
Summary(pl):	Modu� Apache'a do uruchamiania skrypt�w CGI w oparciu o rodzaj danych lub ��dania
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_actions.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_actions) = %{version}-%{release}

%description mod_actions
This module has two directives. The Action directive lets you run CGI
scripts whenever a file of a certain MIME content type is requested.
The Script directive lets you run CGI scripts whenever a particular
method is used in a request. This makes it much easier to execute
scripts that process files.

%description mod_actions -l pl
Ten modu� ma dwie dyrektywy. Dyrektywa Action pozwala uruchamia�
skrypty CGI przy ��daniu pliku o danym typie zawarto�ci MIME.
Dyrektywa Script pozwala uruchamia� skrypty CGI przy danej metodzie
��dania. Znacznie u�atwia to wykonywanie skrypt�w przetwarzaj�cych
pliki.

%package mod_alias
Summary:	Mapping different parts of the host filesystem in the document tree and for URL redirection
Summary(pl):	Odwzorowywanie r�nych cz�ci systemu plik�w w drzewie dokument�w i przekierowywanie URL-i
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_alias.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_alias) = %{version}-%{release}
Provides:	webserver(alias)

%description mod_alias
The directives contained in this module allow for manipulation and
control of URLs as requests arrive at the server. The Alias and
ScriptAlias directives are used to map between URLs and filesystem
paths. This allows for content which is not directly under the
DocumentRoot served as part of the web document tree. The ScriptAlias
directive has the additional effect of marking the target directory as
containing only CGI scripts.

The Redirect directives are used to instruct clients to make a new
request with a different URL. They are often used when a resource has
moved to a new location.

mod_alias is designed to handle simple URL manipulation tasks. For
more complicated tasks such as manipulating the query string, use the
tools provided by mod_rewrite.

%description mod_alias -l pl
Dyrektywy zawarte w tym module umo�liwiaj� manipulacje i sterowanie
URL-ami kiedy ��dania s� dostarczane do serwera. Dyrektywy Alias i
ScriptAlias s� u�ywane do odwzorowywania mi�dzy URL-ami i �cie�kami w
systemie plik�w. Umo�liwia to serwowanie tre�ci nie b�d�cej
bezpo�rednio wewn�trz DocumentRoota jako cz�� drzewa dokument�w WWW.
Dyrektywa ScriptAlias ma dodatkowy efekt oznaczania katalogu
docelowego jako zawieraj�cego wy��cznie skrypty CGI.

Dyrektywy Redirect s�u�� do instruowania klient�w, aby wykonali nowe
��danie z innym URL-em. S� u�ywane zwykle w przypadku, gdy zasoby
zosta�y przeniesione w inne miejsce.

mod_alias zosta� zaprojektowany do obs�ugi prostych manipulacji na
URL-ach. Bardziej skomplikowane zadania, takie jak modyfikowanie
�a�cucha zapytania mo�na wykona� przy u�yciu mod_rewrite.

%package mod_asis
Summary:	Sends files that contain their own HTTP headers
Summary(pl):	Wysy�anie plik�w zawieraj�cych w�asne nag��wki HTTP
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_asis.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_asis) = %{version}-%{release}

%description mod_asis
This module provides the handler send-as-is which causes Apache to
send the document without adding most of the usual HTTP headers.

This can be used to send any kind of data from the server, including
redirects and other special HTTP responses, without requiring a
cgi-script or an nph script.

For historical reasons, this module will also process any file with
the mime type httpd/send-as-is.

%description mod_asis -l pl
Ten modu� udost�pnia procesur� obs�ugi send-as-is powoduj�c�, �e
Apache wysy�a dokument bez dodawania wi�kszo�ci zwykle u�ywanych
nag��wk�w HTTP.

Mo�e to by� u�ywane do wysy�ania dowolnego rodzaju danych z serwera,
w��cznie z przekierowaniami i innymi specjalnymi odpowiedziami HTTP
bez wymagania skryptu CGI lub nph.

%package mod_auth
Summary:	Virtual package which which provides backward compatibility with apache 2.0
Summary(pl):	Pakiet wirtualny zapewniaj�cy kompatybilno�� wsteczn� z apache 2.0
Group:		Networking/Daemons
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_auth_basic = %{version}-%{release}
Requires:	%{name}-mod_authn_file = %{version}-%{release}
Requires:	%{name}-mod_authz_groupfile = %{version}-%{release}
Requires:	%{name}-mod_authz_user = %{version}-%{release}
Provides:	apache(mod_auth) = %{version}-%{release}
Provides:	webserver(auth)

%description mod_auth
Virtual package which requires apache-mod_authn_file,
apache-mod_authz_user and apache-mod_authz_groupfile for backward
compatibility with apache 2.0.

%description mod_auth -l pl
Pakiet wirtualny wymagaj�cy apache-mod_authn_file,
apache-mod_authz_user i apache-mod_authz_groupfile dla kompatybilno�ci
wstecznej z apache 2.0.

%package mod_auth_basic
Summary:	Apache module that allows Basic authentication
Summary(pl):	Modu� Apache'a umo�liwiaj�cy korzystawnie z uwierzytelnienia Basic
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_auth_basic.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_auth_basic) = %{version}-%{release}

%description mod_auth_basic
This module allows the use of HTTP Basic Authentication to restrict
access by looking up users in the given providers.

HTTP Digest Authentication is provided by mod_auth_digest. This module
should usually be combined with at least one authentication module
such as mod_authn_file and one authorization module such as
mod_authz_user.

%description mod_auth_basic -l pl
Ten modu� pozwala u�ywa� uwierzytelnienia HTTP Basic do ograniczania
dost�pu poprzez wyszukiwanie u�ytkownik�w we wskazanych miejscach

%package mod_auth_dbm
Summary:	Virtual package which which provides backward compatibility with apache 2.0
Summary(pl):	Pakiet wirtualny zapewniaj�cy kompatybilno�� wsteczn� z apache 2.0
Group:		Networking/Daemons
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-dbmtools = %{version}-%{release}
Requires:	%{name}-mod_authn_dbm = %{version}-%{release}
Requires:	%{name}-mod_authz_dbm = %{version}-%{release}
Provides:	apache(mod_auth_dbm) = %{version}-%{release}

%description mod_auth_dbm
Virtual package which requires apache-mod_authn_dbm and
apache-mod_authz_dbm for backward compatibility with apache 2.0.

%description mod_auth_dbm -l pl
Pakiet wirtualny wymagaj�cy apache-mod_authn_dbm i
apache-mod_authz_dbm dla kompatybilno�ci wstecznej z apache 2.0.

%package mod_auth_digest
Summary:	User authentication using MD5 Digest Authentication
Summary(pl):	Uwierzytelnianie u�ytkownik�w przy u�yciu MD5 Digest
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_auth_digest.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_auth_digest) = %{version}-%{release}

%description mod_auth_digest
This module implements HTTP Digest Authentication. However, it has not
been extensively tested and is therefore marked experimental.

%description mod_auth_digest -l pl
Ten modu� implementuje uwierzytelnienie HTTP Digest. Nie zosta� on
jednak zbyt obszernie przetestowany, wi�c jest oznaczony jako
eksperymentalny.

%package mod_authn_alias
Summary:	Apache module that provides the ability to create extended authentication
Summary(pl):	Modu� Apache'a umo�liwiaj�cy tworzenie rozszerzonego uwierzytelniania
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_alias.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authn_alias) = %{version}-%{release}

%description mod_authn_alias
This module allows extended authentication providers to be created
within the configuration file and assigned an alias name.

%description mod_authn_alias -l pl
Ten modu� umo�liwia tworzenie rozszerzonych sposob�w uwierzytelniania
w pliku konfiguracyjnym i nadawanie im alias�w.

%package mod_authn_anon
Summary:	Apache module that allows "anonymous" user access to authenticated areas
Summary(pl):	Modu� Apache'a umo�liwiaj�cy dost�p anonimowych u�ytkownik�w do stref uwierzytelnianych
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_anon.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authn_anon) = %{version}-%{release}
# compat
Provides:	apache(mod_auth_anon) = %{version}-%{release}
Provides:	apache-mod_auth_anon = %{version}-%{release}
Obsoletes:	apache-mod_auth_anon < 2.2.0-0.5

%description mod_authn_anon
This module provides authentication front-ends such as mod_auth_basic
to authenticate users similar to anonymous-ftp sites, i.e. have a
'magic' user id 'anonymous' and the email address as a password. These
email addresses can be logged.

%description mod_authn_anon -l pl
Ten modu� udmo�liwia frontendom uwierzytelniaj�cym takim jak
mod_auth_basic uwierzytelnianie u�ytkownik�w podobnie do serwis�w
anonimowego ftp, tzn. przez udost�pnianie "magicznego" identyfikatora
"anonymous" i adresu pocztowego jako has�a. Te adresy pocztowe mog�
by� logowane.

%package mod_authn_dbd
Summary:	Apache module that allows user authentication using an SQL
Summary(pl):	Modu� Apache'a umo�liwiaj�cy uwierzytelnianie u�ytkownik�w przy u�yciu tabel SQL
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_dbd.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_dbd = %{version}-%{release}
Provides:	apache(mod_authn_dbd) = %{version}-%{release}

%description mod_authn_dbd
This module provides authentication front-ends such as mod_auth_digest
and mod_auth_basic to authenticate users by looking up users in SQL
tables.

%description mod_authn_dbd -l pl
Ten modu� udost�pnia frontendom uwierzytelniaj�cym takim jak
mod_auth_digest i mod_auth_basic uwierzytelnianie u�ytkownik�w poprzez
wyszukiwanie w tabelach SQL.

%package mod_authn_dbm
Summary:	Apache module that allows user authentication using DBM files
Summary(pl):	Modu� Apache'a umo�liwiaj�cy uwierzytelnianie u�ytkownik�w przy u�yciu plik�w DBM
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_dbm.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authn_dbm) = %{version}-%{release}

%description mod_authn_dbm
This module provides authentication front-ends such as mod_auth_digest
and mod_auth_basic to authenticate users by looking up users in DBM
password files.

%description mod_authn_dbm -l pl
Ten modu� udost�pnia frontendom uwierzytelniaj�cym takim jak
mod_auth_digest i mod_auth_basic uwierzytelnianie u�ytkownik�w poprzez
wyszukiwanie w tabelach hase� DBM.

%package mod_authn_default
Summary:	Apache module that rejects any credentials supplied by the user
Summary(pl):	Modu� Apache'a odrzucaj�cy wszystkie dane podane przez u�ytkownika
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_default.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authn_default) = %{version}-%{release}

%description mod_authn_default
This module is designed to be the fallback module, if you don't have
configured an authentication module like mod_auth_basic. It simply
rejects any credentials supplied by the user.

%description mod_authn_default -l pl
Ten modu� zosta� pomy�lany jako domy�lny modu� uwierzytelniaj�cy,
je�li nie skonfigurowano modu�u uwierzytelniaj�cego takiego jak
mod_auth_basic. Modu� ten po prostu odrzuca wszelkie dane przekazane
przez u�ytkownika.

%package mod_authn_file
Summary:	Apache module that allows user authentication using text files
Summary(pl):	Modu� Apache'a umo�liwiaj�cy uwierzytelnianie u�ytkownik�w poprzez pliki tekstowe
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authn_file.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authn_file) = %{version}-%{release}

%description mod_authn_file
This module provides authentication front-ends such as mod_auth_digest
and mod_auth_basic to authenticate users by looking up users in plain
text password files.

%description mod_authn_file -l pl
Ten modu� udost�pnia frontendom uwierzytelniaj�cym takim jak
mod_auth_digest i mod_auth_basic uwierzytelnianie u�ytkownik�w poprzez
wyszukiwanie w plikach tekstowych z has�ami.

%package mod_authnz_ldap
Summary:	Apache module that allows an LDAP directory to be used to store the database for HTTP Basic authentication
Summary(pl):	Modu� Apache'a umo�liwiaj�cy przechowywanie danych dla uwierzytelnienia HTTP Basic w bazie LDAP
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authnz_ldap.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_ldap = %{version}-%{release}
Provides:	apache(mod_authnz_ldap) = %{version}-%{release}
# compat
Provides:	apache(mod_auth_ldap) = %{version}-%{release}
Provides:	apache-mod_auth_ldap = %{version}-%{release}
Obsoletes:	apache-mod_auth_ldap < 2.2.0-0.5

%description mod_authnz_ldap
This module provides authentication front-ends such as mod_auth_basic
to authenticate users through an LDAP directory.

%description mod_authnz_ldap -l pl
Ten modu� udost�pnia frontendom uwierzytelniaj�cym takim jak
mod_auth_basic uwierzytelnianie u�ytkownik�w poprzez katalog LDAP.

%package mod_authz_dbm
Summary:	Apache module that allows group authorization using DBM files
Summary(pl):	Modu� Apache'a umo�liwiaj�cy uwierzytelnianie grup z u�yciem plik�w DBM
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authz_dbm.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authz_dbm) = %{version}-%{release}

%description mod_authz_dbm
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site by
group membership stored in DBM file.

%description mod_authz_dbm -l pl
Ten modu� daje mo�liwo�� udost�pniania b�d� blokowania cz�ci serwisu
WWW dla uwierzytelnionych u�ytkownik�w na podstawie ich przynale�no�ci
do grupy zapisywanej w pliku DBM.

%package mod_authz_default
Summary:	Apache module that rejects any authorization request
Summary(pl):	Modu� Apache'a odrzucaj�cy wszystkie ��dania autoryzacji
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authz_default.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authz_default) = %{version}-%{release}

%description mod_authz_default
This module is designed to be the fallback module, if you don't have
configured an authorization module like mod_authz_user or
mod_authz_groupfile. It simply rejects any authorization request.

%description mod_authz_default -l pl
Ten modu� zosta� pomy�lany jako domy�lny modu� autoryzuj�cy je�li nie
skonfigurowano modu�u autoryzuj�cego takiego jak mod_authz_user czy
mod_authz_groupfile. Modu� ten po prostu odrzuca wszelkie ��dania
autoryzacji.

%package mod_authz_groupfile
Summary:	Apache module that allows group authorization using plaintext files
Summary(pl):	Modu� Apache'a umo�liwiaj�cy autoryzacj� grup przy u�yciu plik�w tekstowych
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authz_groupfile.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authz_groupfile) = %{version}-%{release}

%description mod_authz_groupfile
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site by
group membership stored in plain text file.

%description mod_authz_groupfile -l pl
Ten modu� daje mo�liwo�� udost�pniania b�d� blokowania cz�ci serwisu
WWW dla uwierzytelnionych u�ytkownik�w na podstawie ich przynale�no�ci
do grupy zapisywanej w pliku tekstowym.

%package mod_authz_host
Summary:	Apache module that allows group authorizations based on host (name or IP address)
Summary(pl):	Modu� Apache'a umo�liwiaj�cy autoryzacj� grup w oparcu o host (nazw� lub IP)
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_authz_host.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authz_host) = %{version}-%{release}
# for apache < 2.2.0
Provides:	apache(mod_access) = %{version}-%{release}
Provides:	webserver(access)

%description mod_authz_host
The directives provided by mod_authz_host are used in <Directory>,
<Files>, and <Location> sections as well as .htaccess files to control
access to particular parts of the server. Access can be controlled
based on the client hostname, IP address, or other characteristics of
the client request, as captured in environment variables.

%description mod_authz_host -l pl
Dyrektyw udost�pnianych przez mod_authz_host mo�na u�ywa� w sekcjach
<Directory>, <Files> i <Location>, a tak�e plikach .htaccess w celu
sterowania dost�pem do poszczeg�lnych cz�ci serwera. Dost�pem mo�na
sterowa� na podstawie nazwy hosta klienta, adresu IP lub innej
charakterystyki ��dania klienta dost�pnej w zmiennych �rodowiskowych.

%package mod_authz_owner
Summary:	Apache module that allows authorization based on file ownership
Summary(pl):	Modu� Apache'a umo�liwiaj�cy autoryzacje w oparciu o w�asno�� plik�w
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_authz_owner.html
Requires:	%{name}-base = %{version}-%{release}
#Requires:	any-auth-module
Provides:	apache(mod_authz_owner) = %{version}-%{release}

%description mod_authz_owner
This module authorizes access to files by comparing the userid used
for HTTP authentication (the web userid) with the file-system owner or
group of the requested file. The supplied username and password must
be already properly verified by an authentication module, such as
mod_auth_basic or mod_auth_digest.

%description mod_authz_owner -l pl
Ten modu� autoryzuje dost�p do plik�w poprzez por�wnanie
identyfikatora u�ytkownika u�ytego przy uwierzytelnianiu HTTP (web
userid) z w�a�cicielem lub grup� ��danego pliku w systemie plik�w.
Podana nazwa u�ytkownika i has�o musz� by� wcze�niej zweryfikowane
przez modu� uwierzytelniania, taki jak mod_auth_basic lub
mod_auth_digest.

%package mod_authz_user
Summary:	Apache module that allows user authorization
Summary(pl):	Modu� Apache'a umo�liwiaj�cy autoryzacj� u�ytkownik�w
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_authz_user.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_authz_user) = %{version}-%{release}

%description mod_authz_user
This module provides authorization capabilities so that authenticated
users can be allowed or denied access to portions of the web site.

%description mod_authz_user -l pl
Ten modu� daje mo�liwo�� udost�pniania b�d� blokowania cz�ci serwisu
WWW dla uwierzytelnionych u�ytkownik�w.

%package mod_autoindex
Summary:	Apache module - display index of files
Summary(pl):	Modu� apache do wy�wietlania indeksu plik�w
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_autoindex.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Provides:	apache(mod_autoindex) = %{version}-%{release}

%description mod_autoindex
This package contains mod_autoindex module. It provides generation
index of files.

%description mod_autoindex -l pl
Ten pakiet dostarcza modu� autoindex, kt�ry generuje indeks plik�w.

%package mod_bucketeer
Summary:	buckets manipulation filter
Summary(pl):	Dzielenie kube�k�w po znalezieniu znaku steruj�cego
Group:		Networking/Daemons
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_bucketeer) = %{version}-%{release}

%description mod_bucketeer
Split buckets whenever we find a control-char.

%description mod_bucketeer -l pl
Dzielenie kube�k�w po znalezieniu znaku steruj�cego.

%package mod_cache
Summary:	Content cache keyed to URIs
Summary(pl):	Pami�� podr�czna wg klucza URI
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_cache.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_cache) = %{version}-%{release}

%description mod_cache
mod_cache implements an RFC 2616 compliant HTTP content cache that can
be used to cache either local or proxied content. Two storage
management modules are included in the base Apache distribution:
mod_disk_cache implements a disk based storage manager (generally used
for proxy caching) and mod_mem_cache implements an in-memory based
storage manager (primarily useful for caching local content).

%description mod_cache -l pl
Implementacja zgodnej z RFC 2616 pami�ci podr�cznej, kt�ra mo�e by�
u�ywana do zapami�tywania zawarto�ci lokalnej lub dost�pnej przez
proxy. Do��czono dwa modu�y pozwalaj�ce magazynowa� dane w pami�ci
(g��wnie u�yteczne przy cache'owaniu lokalnej zawarto�ci) oraz na
dysku (u�ywane do cache'owania proxy).

%package mod_case_filter
Summary:	TODO
Group:		Networking/Daemons
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_case_filter) = %{version}-%{release}

%description mod_case_filter

%package mod_case_filter_in
Summary:	TODO
Group:		Networking/Daemons
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_case_filter_in) = %{version}-%{release}

%description mod_case_filter_in

%package mod_cern_meta
Summary:	CERN httpd metafile semantics
Summary(pl):	Obs�uga semantyki metaplik�w CERN httpd
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_cern_meta.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_cern_meta) = %{version}-%{release}

%description mod_cern_meta
Emulate the CERN HTTPD Meta file semantics. Meta files are HTTP
headers that can be output in addition to the normal range of headers
for each file accessed. They appear rather like the Apache .asis
files, and are able to provide a crude way of influencing the Expires:
header, as well as providing other curiosities. There are many ways to
manage meta information, this one was chosen because there is already
a large number of CERN users who can exploit this module.

%description mod_cern_meta -l pl
Modu� emuluj�cy semantyk� metaplik�w CERN HTTPD. Metapliki to nag��wki
HTTP, kt�re mog� by� wysy�ane opr�cz normalnego zestawu nag��wk�w dla
ka�dego przetwarzanego pliku. Zachowuj� si� bardziej jak pliki .asis
Apache'a i mog� dawa� brutalny spos�b wp�ywania na nag��wek Expires:,
a tak�e dostarcza� inne ciekawostki. Jest wiele sposob�w zarz�dzania
metainformacjami, ta zosta�a wybrana poniewa� istnieje ju� wielu
u�ytkownik�w CERN wykorzystuj�cych ten modu�.

%package mod_cgi
Summary:	Execution of CGI scripts
Summary(pl):	Uruchamianie skrypt�w CGI
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_cgi.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Provides:	apache(mod_cgi) = %{version}-%{release}
Provides:	webserver(cgi)

%description mod_cgi
Any file that has the mime type application/x-httpd-cgi or handler
cgi-script (Apache 1.1 or later) will be treated as a CGI script, and
run by the server, with its output being returned to the client. Files
acquire this type either by having a name containing an extension
defined by the AddType directive, or by being in a ScriptAlias
directory.

When using a multi-threaded MPM under unix, the module mod_cgid should
be used in place of this module. At the user level, the two modules
are essentially identical.

%description mod_cgi -l pl
Ten modu� powoduje, �e dowolny plik o typie MIME
application/x-httpd-cgi albo procedurze obs�ugi cgi-script (w Apache'u
1.1 lub nowszym) b�dzie traktowany jako skrypt CGI i uruchamiany przez
serwer, a jego wyj�cie b�dzie zwracane klientowi. Pliki uzyskuj� ten
typ przez posiadanie nazwy zawieraj�cej rozszerzenie okre�lone
dyrektyw� AddType lub b�d�c w katalogu ScriptAlias.

Przy u�ywaniu wielow�tkowych MPM pod uniksem zamiast tego modu�u
nale�y u�ywa� modu�u mod_cgid. Z poziomu u�ytkownika oba te modu�y
zachowuj� si� identycznie.

%package mod_cgid
Summary:	Execution of CGI scripts using an external CGI daemon
Summary(pl):	Uruchamianie zewn�trznych skrypt�w CGI za pomoc� daemona CGI
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_cgid.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_alias = %{version}-%{release}
Provides:	apache(mod_cgid) = %{version}-%{release}
Provides:	webserver(cgi)

%description mod_cgid
Execution of CGI scripts using an external CGI daemon.

Except for the optimizations and the additional ScriptSock directive,
mod_cgid behaves similarly to mod_cgi.

This module should be used instead of mod_cgi whenever a
multi-threaded MPM is selected.

%description mod_cgid -l pl
Uruchamianie skrypt�w CGI za pomoc� zewn�trznego demona CGI.

Z wyj�tkiem optymalizacji i dodatkowej dyrektywy ScriptSock, mod_cgid
zachowuje si� podobnie do mod_cgi.

Tego modu�u nale�y u�ywa� zamiast mod_cgi zawsze, je�li wybrano
wielow�tkowy MPM.

%package mod_charset_lite
Summary:	Specify character set translation or recoding
Summary(pl):	Translacja lub przekodowywanie znak�w
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_charset_lite.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_charset_lite) = %{version}-%{release}

%description mod_charset_lite
Specify character set translation or recoding.

This module provides a small subset of configuration mechanisms
implemented by Russian Apache and its associated mod_charset.

This is an experimental module and should be used with care.

%description mod_charset_lite -l pl
Translacja lub przekodowywanie znak�w.

Ten modu� udost�pnia niewielki podzbi�r mechanizm�w konfiguracyjnych
zaimplementowanych przez Russian Apache i powi�zany z nim mod_charset.

Jest to modu� eksperymentalny i nale�y u�ywa� go z uwag�.

%package mod_dav
Summary:	Apache module - Distributed Authoring and Versioning
Summary(pl):	Modu� Apache'a - rozproszone autorstwo i wersjonowanie
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_dav.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	apache-mod_authn_file
Requires:	apache-mod_setenvif
Provides:	apache(mod_dav) = %{version}-%{release}

%description mod_dav
This module provides class 1 and class 2 WebDAV ('Web-based
Distributed Authoring and Versioning') functionality for Apache. This
extension to the HTTP protocol allows creating, moving, copying, and
deleting resources and collections on a remote web server.

%description mod_dav -l pl
Modu� udost�pnia klas� 1 oraz klas� 2 WebDAV (Bazuj�cego na WWW
rozproszonego autorstwa i wersjonowania). To rozszerzenie HTTP pozwala
na tworzenie, przesuwanie, kopiowanie oraz kasowanie zasob�w na
zdalnym serwerze WWW.

%package mod_dbd
Summary:	Manages SQL database connections
Summary(pl):	Zarz�dzanie po��czeniami z baz� danych SQL
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/en/mod/mod_dbd.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_dbd) = %{version}-%{release}

%description mod_dbd
mod_dbd manages SQL database connections using apr_dbd. It provides
database connections on request to modules requiring SQL database
functions, and takes care of managing databases with optimal
efficiency and scalability for both threaded and non-threaded MPMs.

%description mod_dbd -l pl
mod_dbd zarz�dza po��czeniami z baz� danych SQL przy u�yciu apr_dbd.
Udost�pnia po��czenia z baz� danych na ��danie modu��w wymagaj�cych
funkcji bazy danych SQL, a nast�pnie dba o zarz�dzanie bazami danych z
optymaln� wydajno�ci� i skalowalno�ci� zar�wno dla w�tkowych jak i
niew�tkowych MPM.

%package mod_deflate
Summary:	Apache module: Compress content before it is delivered to the client
Summary(pl):	Modu� Apache'a kompresuj�cy dane przed przes�aniem ich do klienta
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_deflate.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_headers = %{version}-%{release}
Provides:	apache(mod_deflate) = %{version}-%{release}

%description mod_deflate
Compress content before it is delivered to the client.

%description mod_deflate -l pl
Modu� kompresuj�cy dane przed przes�aniem ich do klienta.

%package mod_dir
Summary:	Apache module for "trailing slash" redirects and serving directory index files
Summary(pl):	Modu� Apache'a oferuj�cy przekierowania i udost�pnianie informacji o zawarto�ci katalogu
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_dir.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_dir) = %{version}-%{release}
Provides:	webserver(indexfile)

%description mod_dir
This package contains mod_dir which provides "trailing slash"
redirects and serving directory index files.

%description mod_dir -l pl
Modu� oferuj�cy przekierowania i udost�pnianie informacji o zawarto�ci
katalogu.

%package mod_dumpio
Summary:	Dumps all I/O to error log as desired
Summary(pl):	Zrzucanie ca�o�ci wej�cia/wyj�cia do logu b��d�w
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_dumpio.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_dumpio) = %{version}-%{release}

%description mod_dumpio
mod_dumpio allows for the logging of all input received by Apache
and/or all output sent by Apache to be logged (dumped) to the
error.log file.

The data logging is done right after SSL decoding (for input) and
right before SSL encoding (for output). As can be expected, this can
produce extreme volumes of data, and should only be used when
debugging problems.

%description mod_dumpio -l pl
mod_dumpio umo�liwia logowanie ca�ego wej�cia otrzymanego przez
Apache'a i/lub ca��go wyj�cia wysy�anego przez Apache'a do pliku
error.log.

Logowanie danych nast�puja zaraz po zdekodowaniu SSL (dla wej�cia) i
zaraz przed kodowaniem SSL (dla wyj�cia). Jak mo�na si� spodziewa�, ta
opcja mo�e tworzy� ogromne ilo�ci danych i powinna by� u�ywana tylko
przy diagnostyce problem�w.

%package mod_echo
Summary:	A simple echo server to illustrate protocol modules
Summary(pl):	Prosty serwer ocho ilustruj�cy modu�y protoko��w
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_echo.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_echo) = %{version}-%{release}

%description mod_echo
This module provides an example protocol module to illustrate the
concept. It provides a simple echo server. Telnet to it and type
stuff, and it will echo it.

%description mod_echo -l pl
Ten modu� udost�pnia przyk�adowy modu� protoko�u ilustruj�cy ide�.
Udost�pnia prosty serwer echo. Mo�na si� na niego zatelnetowa� i
napisa� cokolwiek, a on odpowie tym samym.

%package mod_env
Summary:	Modifies the environment which is passed to CGI scripts and SSI pages
Summary(pl):	Modyfikowanie �rodowiska przekazywanego skryptom CGI i stronom SSI
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_env.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_env) = %{version}-%{release}

%description mod_env
This module allows for control of the environment that will be
provided to CGI scripts and SSI pages. Environment variables may be
passed from the shell which invoked the httpd process. Alternatively,
environment variables may be set or unset within the configuration
process.

%description mod_env -l pl
Ten modu� pozwala na kontrol� �rodowiska udost�pnianego skryptom CGI i
stronom SSI. Zmienne �rodowiskowe mog� by� przekazywane z pow�oki w
czasie uruchamiania procesu httpd, albo - alternatywnie - ustawiane i
usuwane w procesie konfiguracji.

%package mod_expires
Summary:	Apache module which generates Expires HTTP headers
Summary(pl):	Modu� Apache'a generuj�cy nag��wki HTTP Expires
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_expires.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_expires) = %{version}-%{release}

%description mod_expires
This module controls the setting of the Expires HTTP header in server
responses. The expiration date can set to be relative to either the
time the source file was last modified, or to the time of the client
access.

%description mod_expires -l pl
Modu� kontroluje ustawianie nag��wka HTTP Expires. Data wyga�ni�cia
wa�no�ci mo�e by� ustalana w zale�no�ci od czasu modyfikacji plik�w
�r�d�owych lub odwo�ania klienta.

%package mod_ext_filter
Summary:	Pass the response body through an external program before delivery to the client
Summary(pl):	Przekazywanie cia�a odpowiedzi do zewn�trznego programu przed przekazaniem klientowi
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_ext_filter.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_ext_filter) = %{version}-%{release}

%description mod_ext_filter
mod_ext_filter presents a simple and familiar programming model for
filters. With this module, a program which reads from stdin and writes
to stdout (i.e., a Unix-style filter command) can be a filter for
Apache.

This filtering mechanism is much slower than using a filter which is
specially written for the Apache API and runs inside of the Apache
server process, but it does have the following benefits:
- the programming model is much simpler
- any programming/scripting language can be used, provided that it
  allows the program to read from standard input and write to standard
  output
- existing programs can be used unmodified as Apache filters

Even when the performance characteristics are not suitable for
production use, mod_ext_filter can be used as a prototype environment
for filters.

%description mod_ext_filter -l pl
mod_ext_filter przedstawia prosty i przyjazny model programowania dla
filtr�w. Przy u�yciu tego modu�u program czytaj�cy ze standardowego
wej�cia i pisz�cy na standardowe wyj�cie (czyli uniksowe polecenie
filtruj�ce) mo�e by� filtrem dla Apache'a.

Ten mechanizm filtruj�cy jest znacznie wolniejszy ni� u�ycie filtru
napisanego specjalnie dla API Apache'a i dzia�aj�cego wewn�trz procesu
Apache'a, ale ma nast�puj�ce zalety:
- znacznie prostszy model programowania
- mo�liwo�� u�ycia dowolnego j�zyka programowania/skryptowego, je�li
  tylko umo�liwia czytanie ze standardowego wej�cia i pisanie na
  standardowe wyj�cie
- mo�liwo�� u�ycia istniej�cych program�w bez modyfikacji jako filtr�w
  Apache'a.

Nawet kiedy charakterystyka wydajno�ci nie jest odpowiednia dla u�ytku
produkcyjnego, mod_ext_filter mo�na u�ywa� w �rodowisku prototypowym
dla filtr�w.

%package mod_file_cache
Summary:	Apache module: caches a static list of files in memory
Summary(pl):	Modu� Apache'a cache'uj�cy statyczn� list� plik�w w pami�ci
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_file_cache.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_file_cache) = %{version}-%{release}
Obsoletes:	apache-mmap_static

%description mod_file_cache
Caches a static list of files in memory.

This module is an extension of and borrows heavily from the
mod_mmap_static module in Apache 1.3.

%description mod_file_cache -l pl
Modu� cache'uj�cy statyczn� list� plik�w w pami�ci.

%package mod_filter
Summary:	Context-sensitive smart filter configuration module
Summary(pl):	Modu� inteligentnej, zale�nej od kontekstu konfiguracji filtr�w
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_filter.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_filter) = %{version}-%{release}

%description mod_filter
This module enables smart, context-sensitive configuration of output
content filters. For example, apache can be configured to process
different content-types through different filters, even when the
content-type is not known in advance (e.g. in a proxy).

%description mod_filter -l pl
Ten modu� umo�liwia inteligentne, zale�ne od kontekstu konfigurowanie
wyj�ciowych filtr�w tre�ci. Na przyk�ad, Apache'a mo�na skonfigurowa�
do przetwarzania r�nych content-type poprzez r�ne filtry, nawet
je�li content-type nie jest znany z g�ry (np. w wypadku proxy).

%package mod_headers
Summary:	Apache module allows for the customization of HTTP response headers
Summary(pl):	Modu� Apache'a pozwalaj�cy na modyfikacj� nag��wk�w HTTP
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_headers.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_headers) = %{version}-%{release}

%description mod_headers
This package contains mod_headers module. The module allows for the
customization of HTTP response headers. Headers can be merged,
replaced or removed.

%description mod_headers -l pl
Modu� pozwalaj�cy na ��czenie, usuwanie oraz zamian� nag��wk�w HTTP
wysy�anych do przegl�darki.

%package mod_ident
Summary:	RFC 1413 ident lookups
Summary(pl):	Sprawdzanie identyfikacji RFC 1413
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_ident.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_ident) = %{version}-%{release}

%description mod_ident
This module queries an RFC 1413 compatible daemon on a remote host to
look up the owner of a connection.

%description mod_ident -l pl
Ten modu� odpytuje demona zgodnego z RFC 1413 na zdalnym ho�cie w celu
sprawdzenia w�a�ciciela po��czenia.

%package mod_imagemap
Summary:	Server-side imagemap processing
Summary(pl):	Przetwarzanie map obraz�w po stronie serwera
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_imagemap.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_imagemap) = %{version}-%{release}
Provides:	apache-mod_imap
Obsoletes:	apache-mod_imap

%description mod_imagemap
This module processes .map files, thereby replacing the functionality
of the imagemap CGI program. Any directory or document type configured
to use the handler imap-file (using either AddHandler or SetHandler)
will be processed by this module.

%description mod_imagemap -l pl
Ten modu� przetwarza pliki .map zast�puj�c funkcjonalno�� programu CGI
imagemap. Dowolny katalog lub rodzaj dokumentu skonfigurowany do
u�ywania procedury obs�ugi imap-file (poprzez AddHandler lub
SetHandler) b�dzie przetwarzany przez ten modu�.

%package mod_include
Summary:	Server-parsed html documents (Server Side Includes)
Summary(pl):	Dokumenty przetwarzane przez serwer (Server Side Includes)
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_include.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_include) = %{version}-%{release}

%description mod_include
This module provides a filter which will process files before they are
sent to the client. The processing is controlled by specially
formatted SGML comments, referred to as elements. These elements allow
conditional text, the inclusion of other files or programs, as well as
the setting and printing of environment variables.

%description mod_include -l pl
Ten modu� dostarcza procedur� obs�ugi przetwarzaj�c� pliki przed
wys�aniem ich do klienta. Przetwarzanie jest sterowane specjalnie
sformatowanymi komentarzami SGML, nazywanymi elementami. Elementy te
pozwalaj� na tekst warunkowy, do��czanie innych plik�w lub program�w,
a tak�e ustawianie i wypisywanie zmiennych �rodowiskowych.

%package mod_info
Summary:	Apache module with comprehensive overview of the server configuration
Summary(pl):	Modu� Apache'a udost�pniaj�cy informacje o serwerze
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_info.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_authz_host = %{version}-%{release}
Provides:	apache(mod_info) = %{version}-%{release}

%description mod_info
This package contains mod_info module. It provides a comprehensive
overview of the server configuration including all installed modules
and directives in the configuration files.

%description mod_info -l pl
Modu� udost�pniaj�cy informacje o konfiguracji serwera,
zainstalowanych modu�ach itp.

%package mod_ldap
Summary:	Apache module to use LDAP connections
Summary(pl):	Modu� Apache'a umo�liwiaj�cy korzystanie z po��cze� LDAP
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_ldap.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_ldap) = %{version}-%{release}

%description mod_ldap
Apache module to use LDAP connections.

%description mod_ldap -l pl
Modu� Apache'a umo�liwiaj�cy korzystanie z po��cze� LDAP.

%package mod_log_config
Summary:	Logging of the requests made to the server
Summary(pl):	Logowanie ��da� zg�aszanych do serwera
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_log_config.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_log_config) = %{version}-%{release}

%description mod_log_config
This module provides for flexible logging of client requests. Logs are
written in a customizable format, and may be written directly to a
file, or to an external program. Conditional logging is provided so
that individual requests may be included or excluded from the logs
based on characteristics of the request.

%description mod_log_config -l pl
Ten modu� umo�liwia elastyczne logowanie ��da� klient�w. Logi s�
zapisywane w konfigurowalnym formacie i mog� by� zapisywane
bezpo�rednio do pliku lub przekazywane do zewn�trznego programu.
Dost�pne jest logowanie warunkowe polegaj�ce na w��czeniu lub
wy��czeniu poszczeg�lnych ��da� z logowania na podstawie
charakterystyki ��dania.

%package mod_log_forensic
Summary:	Forensic Logging of the requests made to the server
Summary(pl):	Logowanie �ada� zg�aszanych do serwera w celu p�niejszej analizy
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_log_forensic.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_log_forensic) = %{version}-%{release}

%description mod_log_forensic
This module provides for forensic logging of client requests. Logging
is done before and after processing a request, so the forensic log
contains two log lines for each request.

%description mod_log_forensic -l pl
Ten modu� pozwala na logowanie ��da� w celu p�niejszej analizy.
Logowanie jest wykonywane przed i po przetworzeniu ��dania, wi�c log
zawiera dwie linie dla ka�dego ��dania.

%package mod_logio
Summary:	Logging of input and output bytes per request
Summary(pl):	Logowanie liczby bajt�w wej�cia i wyj�cia dla zapyta�
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_logio.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_log_config = %{version}-%{release}
Provides:	apache(mod_logio) = %{version}-%{release}

%description mod_logio
This module provides the logging of input and output number of bytes
received/sent per request. The numbers reflect the actual bytes as
received on the network, which then takes into account the headers and
bodies of requests and responses. The counting is done before SSL/TLS
on input and after SSL/TLS on output, so the numbers will correctly
reflect any changes made by encryption.

%description mod_logio -l pl
Ten modu� zapewnia logowanie liczby bajt�w wej�cia i wyj�cia
odbieranych/wysy�anych przy ka�dym zapytaniu. Liczby odzwierciedlaj�
rzeczywiste bajty przesy�ane przez sie�, z wliczonymi nag��wkami i
cia�ami ��da� i odpowiedzi. Zliczanie jest wykonywane przed SSL/TLS na
wej�ciu i po SSL/TLS na wyj�ciu, wi�c liczby b�d� w�a�ciwie
odzwierciedla�y wszystkie zmiany dokonywane przez szyfrowanie.

%package mod_mime
Summary:	Associates the requested filename's extensions with the file's behavior and content
Summary(pl):	Wi�zanie okre�lonych rozszerze� plik�w z zachowaniem i zawarto�ci�
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_mime.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_mime) = %{version}-%{release}

%description mod_mime
This module is used to associate various bits of "meta information"
with files by their filename extensions. This information relates the
filename of the document to it's mime-type, language, character set
and encoding. This information is sent to the browser, and
participates in content negotiation, so the user's preferences are
respected when choosing one of several possible files to serve. See
mod_negotiation for more information about content negotiation.

%description mod_mime -l pl
Ten modu� s�u�y do wi�zania okre�lonych cz�ci "metainformacji" z
plikami w zale�no�ci od rozszerze� nazw plik�w. Informacje te ��cz�
nazwy plik�w dokument�w z ich typem MIME, j�zykiem, zestawem znak�w i
kodowaniem. Informacje te s� wysy�ane przegl�darce i maj� wp�yw na
negocjacj� tre�ci, tak �e preferencje u�ytkownika s� respektowane przy
wybieraniu jednego z kilku dost�pnych do zaserwowania. Wi�cej
informacji o negocjacji tre�ci jest w dokumentacji do mod_negotiation.

%package mod_mime_magic
Summary:	Determines the MIME type of a file by looking at a few bytes of its contents
Summary(pl):	Okre�lanie typu MIME pliku poprzez sprawdzanie kilku bajt�w jego zawarto�ci
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_mime_magic.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	file
Provides:	apache(mod_mime_magic) = %{version}-%{release}

%description mod_mime_magic
This module determines the MIME type of files in the same way the Unix
file(1) command works: it looks at the first few bytes of the file. It
is intended as a "second line of defense" for cases that mod_mime
can't resolve.

%description mod_mime_magic -l pl
Ten modu� okre�la typ MIME plik�w w ten sam spos�b, co uniksowe
polecenie file(1): patrzy na kilka pocz�tkowych bajt�w pliku. Ma
s�u�y� jako "druga linia obrony" dla przypadk�w, kt�rych nie mo�e
rozwi�za� mod_mime.

%package mod_negotiation
Summary:	Provides for content negotiation
Summary(pl):	Modu� do negocjacji tre�ci
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_negotiation.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_mime = %{version}-%{release}
Provides:	apache(mod_negotiation) = %{version}-%{release}

%description mod_negotiation
Content negotiation, or more accurately content selection, is the
selection of the document that best matches the clients capabilities,
from one of several available documents.

%description mod_negotiation -l pl
Negocjacja tre�ci, lub bardziej precyzyjnie - wyb�r tre�ci, to wyb�r
dokumentu najbardziej odpowiadaj�cego mo�liwo�ciom klient�w spo�r�d
kilku mo�liwych dokument�w.

%package mod_proxy
Summary:	Apache module with Web proxy
Summary(pl):	Modu� Apache'a dodaj�cy obs�ug� serwera proxy
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_proxy.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_authz_host = %{version}-%{release}
Provides:	apache(mod_proxy) = %{version}-%{release}

%description mod_proxy
This package contains module with implementation a proxy/cache for
Apache. It implements proxying capability for FTP, CONNECT (for SSL),
HTTP/0.9, HTTP/1.0 and HTTP/1.1. The module can be configured to
connect to other proxy modules for these and other protocols.

%description mod_proxy -l pl
Modu� zawiera implementacj� serwera proxy/cache dla Apache.
Implementacja zawiera obs�ug� FTP, CONNECT (dla SSL), HTTP/0.9,
HTTP/1.0 i HTTP/1.1.

%package mod_rewrite
Summary:	Apache module with rule-based engine for rewrite requested URLs on the fly
Summary(pl):	Modu� Apache'a do "przepisywania" adres�w URL w locie
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_rewrite) = %{version}-%{release}

%description mod_rewrite
This package contains It provides a rule-based rewriting engine to
rewrite requested URLs on the fly.

%description mod_rewrite -l pl
Modu� oferuj�cy mo�liwo�� "przepisywania" adres�w URL w locie.

%package mod_setenvif
Summary:	Allows the setting of environment variables based on characteristics of the request
Summary(pl):	Ustawianie zmiennych �rodowiskowych w oparciu o charakterystyk� ��dania
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_setenvif.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_setenvif) = %{version}-%{release}

%description mod_setenvif
The mod_setenvif module allows you to set environment variables
according to whether different aspects of the request match regular
expressions you specify. These environment variables can be used by
other parts of the server to make decisions about actions to be taken.

%description mod_setenvif -l pl
Modu� mod_setenvif pozwala na ustawianie zmiennych �rodowiskowych w
zale�no�ci od r�nych aspekt�w ��dania pasuj�cych do podanych wyra�e�
regularnych. Te zmienne �rodowiskowe mog� by� u�ywane przez inne
cz�ci serwera do podejmowania decyzji o podejmowanych akcjach.

%package mod_speling
Summary:	Attempts to correct mistaken URLs by ignoring capitalization and by allowing up to one misspelling
Summary(pl):	Pr�ba poprawiania b��dnych URL-i poprzez ignorowanie wielko�ci liter i zezwalanie na jedn� liter�wk�
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_speling.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_speling) = %{version}-%{release}

%description mod_speling
Requests to documents sometimes cannot be served by the core apache
server because the request was misspelled or miscapitalized. This
module addresses this problem by trying to find a matching document,
even after all other modules gave up. It does its work by comparing
each document name in the requested directory against the requested
document name without regard to case, and allowing up to one
misspelling (character insertion / omission / transposition or wrong
character). A list is built with all document names which were matched
using this strategy.

%description mod_speling -l pl
Czasami ��dania dokument�w nie mog� by� wykonane przez sam serwer
Apache, poniewa� ��danie zosta�o napisane z b��dem w znakach lub
wielko�ci liter. Ten modu� pr�buje rozwi�za� ten problem pr�buj�c
znale�� pasuj�cy dokument, nawet je�li inne modu�y si� podda�y. Dzia�a
on poprzez por�wnywanie nazwy ka�dego dokumentu w ��danym katalogu z
��dan� nazw� dokumentu bez zwracania uwagi na wielko�� liter i
pozwalaj�c na jeden b��d (dodany, pomini�ty, przestawiony lub z�y
znak). Tworzona jest lista dla wszystkich nazw dokument�w pasuj�cych
dla tej strategii.

%package mod_ssl
Summary:	SSL/TLS module for the Apache HTTP server
Summary(pl):	Modu� SSL/TSL dla serwera Apache
Summary(ru):	������ SSL/TLS ��� ���-������� Apache
Epoch:		1
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_ssl.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_ssl) = 1:%{version}-%{release}

%description mod_ssl
The mod_ssl module provides strong cryptography for the Apache Web
server via the Secure Sockets Layer (SSL) and Transport Layer Security
(TLS) protocols.

%description mod_ssl -l pl
Modu� mod_ssl udost�pnia wsparcie do silnej kryptografii dla serwera
Apache poprzez protoko�y SSL/TSL (Secure Sockets Layer/Transport Layer
Security).

%description mod_ssl -l ru
������ mod_ssl ������������ ��������� � ���-������� Apache ���������
���������� ���������� Secure Sockets Layer (SSL) � Transport Layer

%package mod_status
Summary:	Server status report module for Apache
Summary(pl):	Modu� udost�pniaj�cy informacje statystyczne z serwera Apache
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_status.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_authz_host = %{version}-%{release}
Provides:	apache(mod_status) = %{version}-%{release}

%description mod_status
The Status module allows a server administrator to find out how well
their server is performing. A HTML page is presented that gives the
current server statistics in an easily readable form. If required this
page can be made to automatically refresh (given a compatible
browser).

%description mod_status -l pl
Modu� pozwala administratorowi na przegl�danie statystyk dotycz�cych
pracy serwera Apache (w postaci strony HTML).

%package mod_unique_id
Summary:	Apache module which provides a magic token for each request
Summary(pl):	Modu� Apache'a nadaj�cy ka�demu zapytaniu unikalny token
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_unique_id.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_unique_id) = %{version}-%{release}

%description mod_unique_id
This package contains the mod_unique_id. This module provides a magic
token for each request which is guaranteed to be unique across "all"
requests under very specific conditions. The unique identifier is even
unique across multiple machines in a properly configured cluster of
machines. The environment variable UNIQUE_ID is set to the identifier
for each request. Unique identifiers are useful for various reasons
which are beyond the scope of this document.

%description mod_unique_id -l pl
Modu� nadaje ka�demu zapytaniu token unikalny w ramach wszystkich
zapyta�, nawet w ramach poprawnie skonfigurowanego klastra z wielu
maszyn. Modu� ustawia przy ka�dym zapytaniu zmienn� �rodowiskow�
UNIQUE_ID.

%package mod_userdir
Summary:	User-specific directories
Summary(pl):	Katalogi specyficzne dla u�ytkownik�w
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_userdir.html
Requires:	%{name}-base = %{version}-%{release}
Requires:	%{name}-mod_authz_host = %{version}-%{release}
Provides:	apache(mod_userdir) = %{version}-%{release}

%description mod_userdir
This module allows user-specific directories to be accessed using the
http://example.com/~user/ syntax.

%description mod_userdir -l pl
Ten modu� pozwala na dost�p do katalog�w specyficznych dla
u�ytkownik�w przy u�yciu sk�adni http://example.com/~user/ .

%package mod_usertrack
Summary:	Apache module for user tracking using cookies
Summary(pl):	Modu� Apache'a s�u��cy do �ledzenia "ciasteczek"
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_usertrack.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_usertrack) = %{version}-%{release}

%description mod_usertrack
This package contains the user tracking module which did its own
logging using CookieLog directory. This module allow multiple log
files.

%description mod_usertrack -l pl
Ten pakiet zawiera modu� �ledz�cy u�ytkownik�w zapisuj�cy w�asny log
przy u�yciu katalogu CookieLog. Pozwala na u�ycie wielu plik�w log�w.

%package mod_version
Summary:	Version dependent configuration
Summary(pl):	Konfiguracja zale�na od wersji
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_version.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_version) = %{version}-%{release}

%description mod_version
This module is designed for the use in test suites and large networks
which have to deal with different httpd versions and different
configurations. It provides a new container -- <IfVersion>, which
allows a flexible version checking including numeric comparisons and
regular expressions.

%description mod_version -l pl
Ten modu� jest przeznaczony do u�ywania w zestawach test�w i du�ych
sieciach, gdzie trzeba inaczej obs�ugiwa� r�ne wersje httpd i r�ne
konfiguracje. Udost�pnia nowy kontener: <IfVersion>, umo�liwiaj�cy
elastyczne sprawdzanie wersji w��cznie z por�wnaniami liczbowymi i
wyra�eniami regularnymi.

%package mod_vhost_alias
Summary:	Apache module for dynamically configured mass virtual hosting
Summary(pl):	Modu� Apache'a dodaj�cy obs�ug� host�w wirtualnych
Group:		Networking/Daemons
URL:		http://httpd.apache.org/docs/2.2/mod/mod_vhost_alias.html
Requires:	%{name}-base = %{version}-%{release}
Provides:	apache(mod_vhost_alias) = %{version}-%{release}

%description mod_vhost_alias
This package contains the mod_vhost_alias. It provides support for
dynamically configured mass virtual hosting.

%description mod_vhost_alias -l pl
Modu� umo�liwia na dynamiczne konfigurowanie masowej ilo�ci serwer�w
wirtualnych.

%package -n htpasswd-%{name}
Summary:	Apache 2 htpasswd utility: manage user files for basic authentication
Summary(pl):	Narz�dzie htpasswd z Apache'a 2 do zarz�dzania plikami uwierzytelnienia basic
Group:		Networking/Utilities
Provides:	htpasswd
Obsoletes:	htpasswd

%description -n htpasswd-%{name}
htpasswd is used to create and update the flat-files used to store
usernames and password for basic authentication of HTTP users. This
package contains htpasswd from Apache 2; this version supports
plaintext passwords and CRYPT (default), MD5 and SHA1 encryptions.

%description -n htpasswd-%{name} -l pl
htpasswd s�u�y do tworzenia i uaktualniania plik�w tekstowych
s�u��cych do przechowywania nazw u�ytkownik�w i hase� do podstawowego
uwierzytelnienia u�ytkownik�w HTTP. Ten pakiet zawiera htpasswd z
Apache'a 2; ta wersja obs�uguje has�a zapisane czystym tekstem oraz
zakodowane algorytmami CRYPT (domy�lnym), MD5 i SHA1.

%package dbmtools
Summary:	Apache 2 tools for manipulating DBM files
Summary(pl):	Narz�dzia Apache'a 2 do obr�bki plik�w DBM
Group:		Networking/Utilities
Requires:	%{name}-base = %{version}-%{release}

%description dbmtools
Apache 2 tools for manipulating DBM files.

%description dbmtools -l pl
Narz�dzia Apache'a 2 do obr�bki plik�w DBM.

%package cgi_test
Summary:	cgi test/demo programs
Summary(pl):	Programy testowe/przyk�adowe cgi
Group:		Networking/Utilities
Requires:	%{name}-base = %{version}-%{release}
Requires:	filesystem >= 3.0-11

%description cgi_test
Two cgi test/demo programs: test-cgi and print-env.

%description cgi_test -l pl
Dwa programy testowe/przyk�adowe cgi: test-cgi and print-env.

%prep
%setup -q -n httpd-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch12 -p1
%patch14 -p1
%patch15 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

# using system apr, apr-util and pcre
rm -rf srclib/{apr,apr-util,pcre}

# sanity check
MODULES_API=`awk '/#define MODULE_MAGIC_NUMBER_MAJOR/ {print $3}' include/ap_mmn.h`
if [ "$MODULES_API" != "%_apache_modules_api" ]; then
	echo "Set %%_apache_modules_api to $MODULES_API and rerun."
	exit 1
fi

%build
cp /usr/share/apr/build/apr_common.m4 build
cp /usr/share/libtool/ltmain.sh build
cp /usr/share/automake/config.* build
%{__autoheader}
%{__autoconf}

# from ./buildconf
: fixing timestamps for mod_ssl sources
cd modules/ssl
touch ssl_expr_parse.y
sleep 1
touch ssl_expr_parse.c ssl_expr_parse.h ssl_expr_scan.l
sleep 1
touch ssl_expr_scan.c
cd ../..

CPPFLAGS="-DMAX_SERVER_LIMIT=200000 -DBIG_SECURITY_HOLE=1"
for mpm in prefork worker %{?with_metuxmpm:metuxmpm} %{?with_peruser:peruser} %{?with_event:event}; do
install -d "buildmpm-${mpm}"; cd "buildmpm-${mpm}"
../%configure \
	--enable-layout=PLD \
	--disable-v4-mapped \
	$( [ "${mpm}" = "prefork" -o "${mpm}" = "worker" -o "${mpm}" = "event" ] && echo "--enable-exception-hook" ) \
	--enable-modules=all \
	--enable-mods-shared=all \
	--enable-auth-anon \
	--enable-auth-dbm \
	--enable-authn-dbd \
	--enable-authn-alias \
	--enable-authz-dbm \
	--enable-authz-owner \
	%{?with_ldap:--enable-authnz-ldap} \
	--enable-auth-digest \
	--enable-file-cache \
	--enable-cache \
	--enable-disk-cache \
	--enable-mem-cache \
	--enable-dbd \
	%{?with_bucketeer:--enable-bucketeer} \
	--enable-dumpio \
	--enable-echo \
	--enable-charset-lite \
	--enable-deflate \
	%{?with_ldap:--enable-ldap} \
	--enable-ext-filter \
	--enable-case-filter \
	--enable-case-filter-in \
	--enable-log-forensic \
	--enable-logio \
	--with-z=%{_prefix} \
	--enable-mime-magic \
	--enable-cern-meta \
	--enable-expires \
	--enable-headers \
	--enable-ident \
	--enable-usertrack \
	--enable-unique-id \
	--enable-proxy \
	--enable-proxy-connect \
	--enable-proxy-ftp \
	--enable-proxy-http \
	--enable-proxy-ajp \
	--enable-proxy-balancer \
	%{?with_ssl:--enable-ssl %{?with_distcache:--enable-distcache}} \
	--enable-http \
	--enable-dav \
	--enable-info \
	--enable-suexec \
	--enable-cgi \
	--enable-cgid \
	--enable-dav-fs \
	--enable-dav-lock \
	--enable-vhost-alias \
	--enable-imagemap \
	--enable-speling \
	--enable-rewrite \
	--enable-so \
	--with-program-name=httpd.${mpm} \
	--with-mpm=${mpm} \
%ifarch %{ix86}
%ifnarch i386 i486
	$( [ "${mpm}" = "leader" ] && echo "--enable-nonportable-atomics=yes" ) \
%endif
%endif
	--with-suexec-bin=%{_sbindir}/suexec \
	--with-suexec-caller=http \
	--with-suexec-docroot=%{_datadir} \
	--with-suexec-logfile=/var/log/httpd/suexec_log \
	--with-suexec-uidmin=500 \
	--with-suexec-gidmin=500 \
	--with-suexec-umask=077 \
	--with-apr=%{_bindir}/apr-1-config \
	--with-apr-util=%{_bindir}/apu-1-config \
	--with-pcre

%{__make}
./httpd.${mpm} -l | grep -v "${mpm}" > modules-inside
cd ..

done

for mpm in %{?with_metuxmpm:metuxmpm} %{?with_peruser:peruser} worker %{?with_event:event}; do
	if ! cmp -s buildmpm-prefork/modules-inside buildmpm-${mpm}/modules-inside; then
		echo "List of compiled modules is different between prefork-MPM and ${mpm}-MPM!"
		echo "Build failed."
		exit 1
	fi
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,sysconfig,monit} \
	$RPM_BUILD_ROOT%{_var}/{log/{httpd,archiv/httpd},{run,cache}/httpd,lock/mod_dav} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{webapps.d,conf.d} \
	$RPM_BUILD_ROOT%{_datadir}/cgi-bin

# prefork is default one
%{__make} -C buildmpm-prefork install \
	DESTDIR=$RPM_BUILD_ROOT

# install other mpm-s
for mpm in %{?with_metuxmpm:metuxmpm} %{?with_peruser:peruser} worker %{?with_event:event}; do
	install buildmpm-${mpm}/httpd.${mpm} $RPM_BUILD_ROOT%{_sbindir}/httpd.${mpm}
done

ln -s httpd.prefork $RPM_BUILD_ROOT%{_sbindir}/httpd
ln -s %{_libexecdir} $RPM_BUILD_ROOT%{_sysconfdir}/modules
ln -s %{_localstatedir}/run/httpd $RPM_BUILD_ROOT%{_sysconfdir}/run
ln -s %{_var}/log/httpd $RPM_BUILD_ROOT%{_sysconfdir}/logs
ln -s conf.d $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/httpd
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/httpd
install %{SOURCE5} $RPM_BUILD_ROOT/etc/monit/httpd.monitrc

touch $RPM_BUILD_ROOT/var/log/httpd/{access,error,agent,referer,suexec}_log

%if %{with ssl}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/ssl
install %{SOURCE20} $RPM_BUILD_ROOT%{_sysconfdir}/ssl/server.crt
install %{SOURCE21} $RPM_BUILD_ROOT%{_sysconfdir}/ssl/server.key
%endif

install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf

CFG="$RPM_BUILD_ROOT%{_sysconfdir}/conf.d/"

install %{SOURCE7} $CFG/10_common.conf

install %{SOURCE25} $CFG/01_mod_mime.conf
install %{SOURCE27} $CFG/01_mod_authz_host.conf
install %{SOURCE28} $CFG/01_mod_cgid.conf
install %{SOURCE29} $CFG/01_mod_log_config.conf
install %{SOURCE30} $CFG/01_mod_mime_magic.conf
install %{SOURCE31} $CFG/01_mod_cache.conf
install %{SOURCE8} $CFG/20_mod_vhost_alias.conf
install %{SOURCE9} $CFG/25_mod_status.conf
install %{SOURCE10} $CFG/30_mod_proxy.conf
install %{SOURCE11} $CFG/35_mod_info.conf
install %{SOURCE12} $CFG/40_mod_ssl.conf
install %{SOURCE13} $CFG/45_mod_dav.conf
install %{SOURCE14} $CFG/59_mod_dir.conf
install %{SOURCE15} $CFG/13_mod_suexec.conf
install %{SOURCE16} $CFG/58_mod_deflate.conf
install %{SOURCE17} $CFG/57_mod_autoindex.conf
install %{SOURCE18} $CFG/30_errordocs.conf
install %{SOURCE19} $CFG/30_manual.conf
install %{SOURCE22} $CFG/16_mod_userdir.conf
install %{SOURCE23} $CFG/10_mpm.conf
install %{SOURCE24} $CFG/20_languages.conf

echo "LoadModule alias_module modules/mod_alias.so" > $CFG/00_mod_alias.conf
echo "LoadModule authn_file_module	modules/mod_authn_file.so" > $CFG/00_mod_authn_file.conf
echo "LoadModule authn_dbm_module	modules/mod_authn_dbm.so" > $CFG/00_mod_authn_dbm.conf
echo "LoadModule authn_anon_module	modules/mod_authn_anon.so" > $CFG/00_mod_authn_anon.conf
echo "LoadModule authn_dbd_module	modules/mod_authn_dbd.so" > $CFG/00_mod_authn_dbd.conf
echo "LoadModule authn_default_module	modules/mod_authn_default.so" > $CFG/00_mod_authn_default.conf
echo "LoadModule authn_alias_module	modules/mod_authn_alias.so" > $CFG/00_mod_authn_alias.conf
echo "LoadModule authz_groupfile_module	modules/mod_authz_groupfile.so" > $CFG/00_mod_authz_groupfile.conf
echo "LoadModule authz_user_module	modules/mod_authz_user.so" > $CFG/00_mod_authz_user.conf
echo "LoadModule authz_dbm_module	modules/mod_authz_dbm.so" > $CFG/00_mod_authz_dbm.conf
echo "LoadModule authz_owner_module	modules/mod_authz_owner.so" > $CFG/00_mod_authz_owner.conf
echo "LoadModule authnz_ldap_module	modules/mod_authnz_ldap.so" > $CFG/00_mod_authnz_ldap.conf
echo "LoadModule authz_default_module	modules/mod_authz_default.so" > $CFG/00_mod_authz_default.conf
echo "LoadModule auth_basic_module	modules/mod_auth_basic.so" > $CFG/00_mod_auth_basic.conf
echo "LoadModule dbd_module	modules/mod_dbd.so" > $CFG/00_mod_dbd.conf
%if %{with bucketeer}
echo "LoadModule bucketeer_module	modules/mod_bucketeer.so" > $CFG/00_mod_bucketeer.conf
%endif
echo "LoadModule dumpio_module	modules/mod_dumpio.so" > $CFG/00_mod_dumpio.conf
echo "LoadModule echo_module	modules/mod_echo.so" > $CFG/00_mod_echo.conf
echo "LoadModule case_filter_module	modules/mod_case_filter.so" > $CFG/00_mod_case_filter.conf
echo "LoadModule case_filter_in_module	modules/mod_case_filter_in.so" > $CFG/00_mod_case_filter_in.conf
echo "LoadModule ext_filter_module	modules/mod_ext_filter.so" > $CFG/00_mod_ext_filter.conf
echo "LoadModule include_module	modules/mod_include.so" > $CFG/00_mod_include.conf
echo "LoadModule filter_module	modules/mod_filter.so" > $CFG/00_mod_filter.conf
echo "LoadModule log_forensic_module	modules/mod_log_forensic.so" > $CFG/00_mod_log_forensic.conf
echo "LoadModule logio_module	modules/mod_logio.so" > $CFG/00_mod_logio.conf
echo "LoadModule env_module	modules/mod_env.so" > $CFG/00_mod_env.conf
echo "LoadModule cern_meta_module	modules/mod_cern_meta.so" > $CFG/00_mod_cern_meta.conf
echo "LoadModule ident_module	modules/mod_ident.so" > $CFG/00_mod_ident.conf
echo "LoadModule setenvif_module	modules/mod_setenvif.so" > $CFG/00_mod_setenvif.conf
echo "LoadModule version_module	modules/mod_version.so" > $CFG/00_mod_version.conf
echo "LoadModule asis_module	modules/mod_asis.so" > $CFG/00_mod_asis.conf
echo "LoadModule cgi_module	modules/mod_cgi.so" > $CFG/00_mod_cgi.conf
echo "LoadModule negotiation_module	modules/mod_negotiation.so" > $CFG/00_mod_negotiation.conf
echo "LoadModule imagemap_module	modules/mod_imagemap.so" > $CFG/00_mod_imagemap.conf
echo "LoadModule speling_module	modules/mod_speling.so" > $CFG/00_mod_speling.conf
echo "LoadModule ldap_module	modules/mod_ldap.so" > $CFG/00_mod_ldap.conf
echo "LoadModule actions_module	modules/mod_actions.so" > $CFG/00_mod_actions.conf
echo "LoadModule auth_digest_module	modules/mod_auth_digest.so" > $CFG/00_mod_auth_digest.conf
echo "LoadModule charset_lite_module	modules/mod_charset_lite.so" > $CFG/00_mod_charset_lite.conf
echo "LoadModule expires_module	modules/mod_expires.so" > $CFG/00_mod_expires.conf
echo "LoadModule file_cache_module	modules/mod_file_cache.so" > $CFG/00_mod_file_cache.conf
echo "LoadModule headers_module	modules/mod_headers.so" > $CFG/00_mod_headers.conf
echo "LoadModule rewrite_module	modules/mod_rewrite.so" > $CFG/00_mod_rewrite.conf
echo "LoadModule usertrack_module	modules/mod_usertrack.so" > $CFG/00_mod_usertrack.conf
echo "LoadModule unique_id_module	modules/mod_unique_id.so" > $CFG/00_mod_unique_id.conf

# anything in style dir not ending with .css is trash
rm -rf $RPM_BUILD_ROOT%{_datadir}/manual/style/{lang,latex,xsl}
find $RPM_BUILD_ROOT%{_datadir}/manual/style -type f ! -name '*.css' -print0 | xargs -0r rm -f

# find manual files
> manual.files
cur=$(pwd)
cd $RPM_BUILD_ROOT
find ./%{_datadir}/manual -type d -printf "%%%%dir %{_datadir}/manual/%%P\n" >> "$cur/manual.files"
find ./%{_datadir}/manual -type f -printf "%{_datadir}/manual/%%P\n" | sed -e '
s/^.*\.\(de\|es\|fr\|ja\|ko\|ru\)\(\..*\)\?/%%lang(\1) &/
s/^.*\.\(pt-br\)/%%lang(pt_BR) &/
' >> "$cur/manual.files"
cd $cur

# htpasswd goes to %{_bindir}
mv $RPM_BUILD_ROOT%{_sbindir}/htpasswd $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_bindir}/htpasswd $RPM_BUILD_ROOT%{_sbindir}

# cgi_test: create config file with ScriptAlias
cat << EOF > $CFG/09_cgi_test.conf
ScriptAlias /cgi-bin/printenv %{_cgibindir}/printenv
ScriptAlias /cgi-bin/test-cgi %{_cgibindir}/test-cgi
EOF

# no value
rm $RPM_BUILD_ROOT%{_libexecdir}/build/config.nice
rm $RPM_BUILD_ROOT%{_sysconfdir}/mime.types
rm $RPM_BUILD_ROOT%{_sysconfdir}/httpd.prefork.conf
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/{extra,original}

%clean
rm -rf $RPM_BUILD_ROOT

%pre base
%groupadd -g 51 http
%useradd -u 51 -r -d /home/services/httpd -s /bin/false -c "HTTP User" -g http http

%pretrans base
# change httpd.conf from dir to symlink
if [ ! -L /etc/httpd/httpd.conf ]; then
	if [ -d /etc/httpd/httpd.conf ]; then
		if [ -d /etc/httpd/conf.d ]; then
			mv /etc/httpd/httpd.conf/* /etc/httpd/conf.d
			rmdir /etc/httpd/httpd.conf 2>/dev/null || mv -v /etc/httpd/httpd.conf{,.rpmsave}
		else
			mv /etc/httpd/httpd.conf /etc/httpd/conf.d
		fi

		# new module packages issue error as first installed over 2.0 installation
		mv -f /var/lock/subsys/httpd{,.disabled} 2>/dev/null
	fi

	# always have httpd.conf symlink (until all packages from Ac use new dir)
	install -d /etc/httpd
	ln -s conf.d /etc/httpd/httpd.conf
fi
exit 0

%post base
/sbin/chkconfig --add httpd
umask 137
touch /var/log/httpd/{access,error,agent,referer}_log

%preun base
if [ "$1" = "0" ]; then
	%service httpd stop
	/sbin/chkconfig --del httpd
fi

%postun base
if [ "$1" = "0" ]; then
	%userremove http
	%groupremove http
fi

%triggerpostun base -- %{name} <= 2.0.50-6
%banner %{name}-2.0.50-6 << EOF
WARNING!!!
Since apache-2.0.50-6 autoindex module has been separated to package
%{name}-mod_autoindex If you want to have the same functionality do:
poldek -Uv %{name}-mod_autoindex
EOF

%triggerpostun base -- %{name} < 2.0.54-4
%banner %{name}-2.0.54-2 << EOF
WARNING!!!
CGI demo/test programs - printenv and test-cgi, have been released
from package apache into separate subpackage apache-cgi_test. If you
need printenv and/or test-cgi, please install apache-cgi_test package,
e.g. by running poldek -Uv apache-cgi_test
EOF

# update /etc/sysconfig/apache -> httpd rename
if [ -f /etc/sysconfig/apache.rpmsave ]; then
	cp -f /etc/sysconfig/httpd{,.rpmnew}
	mv -f /etc/sysconfig/{apache.rpmsave,httpd}
fi

%triggerpostun base -- %{name} < 2.0.55-3.1
# check for config first as in 2.2 it's .rpmsave
if [ -f /etc/httpd/httpd.conf/10_httpd.conf ]; then
	if ! grep -q 'Include webapps.d/' /etc/httpd/httpd.conf/10_httpd.conf; then
		# make sure webapps.d is included
		cp -f /etc/httpd/httpd.conf/10_httpd.conf{,.rpmsave}
		# this file is ugly, so just append new lines
		cat <<-EOF >> /etc/httpd/httpd.conf/10_httpd.conf
		# Include webapps config
		Include webapps.d/*.conf
EOF
	fi
fi

%triggerpostun base -- %{name} < 2.2.0
# rename monitrc to be service name like other files
if [ -f /etc/monit/apache.monitrc.rpmsave ]; then
	mv -f /etc/monit/httpd.monitrc{,.rpmnew}
	mv -f /etc/monit/{apache.monitrc.rpmsave,httpd.monitrc}
fi

# change HTTPD_CONF to point to new location. *only* if it's the
# default config setting
cp -f /etc/sysconfig/httpd{,.rpmorig}
sed -i -e '/^HTTPD_CONF="\/etc\/httpd\/httpd.conf"/s,.*,HTTPD_CONF="/etc/httpd/apache.conf",' /etc/sysconfig/httpd

if [ -f /etc/httpd/conf.d/10_httpd.conf.rpmsave ]; then
	sed -e '
	# as separate modules
	/^LoadModule access_module/s,^,#,
	/^LoadModule alias_module/s,^,#,
	/^LoadModule asis_module/s,^,#,
	/^LoadModule cern_meta_module/s,^,#,
	/^LoadModule cgi_module/s,^,#,
	/^LoadModule env_module/s,^,#,
	/^LoadModule include_module/s,^,#,
	/^LoadModule log_config_module/s,^,#,
	/^LoadModule mime_magic_module/s,^,#,
	/^LoadModule mime_module/s,^,#,
	/^LoadModule negotiation_module/s,^,#,
	/^LoadModule setenvif_module/s,^,#,
	/^LoadModule speling_module/s,^,#,
	/^LoadModule userdir_module/s,^,#,

	# in 30_errordocs.conf
	/<IfModule mod_include.c>/,/<\/IfModule>/s,^,#,

	# in 57_mod_autoindex.conf
	/^Alias \/icons\//s,^,#,

	# in apache.conf
	/^ScriptAlias \/cgi-bin\//s,^,#,
	/^Listen 80/s,^,#,

	# avoid loops
	/Include conf.d\/\*.conf/s,^,#,
	/Include webapps.d\/\*.conf/s,^,#,

	' < /etc/httpd/conf.d/10_httpd.conf.rpmsave > /etc/httpd/conf.d/10_httpd.conf
fi

%banner -e %{name} <<'EOF'
NB! Apache main config has been changed to /etc/httpd/apache.conf

There has been changed a lot, so many things could be broken.
Please report bugs to http://bugs.pld-linux.org/.

EOF

%triggerpostun mod_ssl -- %{name}-mod_ssl < 1:2.2.0-3.1
cp -f /etc/httpd/conf.d/40_mod_ssl.conf{,.rpmsave}
sed -i -e '
	s,/var/run/apache,/var/run/httpd,g
	s,/var/cache/apache,/var/cache/httpd,g
' /etc/httpd/conf.d/40_mod_ssl.conf

%posttrans base
# restore lock which we disabled in pretrans
mv -f /var/lock/subsys/httpd{.disabled,} 2>/dev/null

# minimizing apache restarts logics. we restart webserver:
#
# 1. at the end of transaction. (posttrans, feature from rpm 4.4.2)
# 2. first install of module (post: $1 = 1)
# 2. uninstall of module (postun: $1 == 0)
#
# the strict internal deps between apache modules and
# main package are very important for all this to work.

# restart webserver at the end of transaction
%service httpd restart

# macro called at module post scriptlet
%define	module_post \
if [ "$1" = "1" ]; then \
	%service -q httpd restart \
fi

# macro called at module postun scriptlet
%define	module_postun \
if [ "$1" = "0" ]; then \
	%service -q httpd restart \
fi

# it's sooo annoying to write them
%define	module_scripts() \
%post %1 \
%module_post \
\
%postun %1 \
%module_postun

%module_scripts mod_actions
%module_scripts mod_alias
%module_scripts mod_asis
%module_scripts mod_auth_basic
%module_scripts mod_auth_dbm
%module_scripts mod_auth_digest
%module_scripts mod_authn_alias
%module_scripts mod_authn_anon
%module_scripts mod_authn_dbd
%module_scripts mod_authn_dbm
%module_scripts mod_authn_default
%module_scripts mod_authn_file
%module_scripts mod_authnz_ldap
%module_scripts mod_authz_dbm
%module_scripts mod_authz_default
%module_scripts mod_authz_groupfile
%module_scripts mod_authz_host
%module_scripts mod_authz_owner
%module_scripts mod_authz_user
%module_scripts mod_autoindex
%module_scripts mod_bucketeer
%module_scripts mod_cache
%module_scripts mod_case_filter
%module_scripts mod_case_filter_in
%module_scripts mod_cern_meta
%module_scripts mod_cgi
%module_scripts mod_cgid
%module_scripts mod_charset_lite
%module_scripts mod_dav
%module_scripts mod_dbd
%module_scripts mod_deflate
%module_scripts mod_dir
%module_scripts mod_dumpio
%module_scripts mod_echo
%module_scripts mod_env
%module_scripts mod_expires
%module_scripts mod_ext_filter
%module_scripts mod_file_cache
%module_scripts mod_filter
%module_scripts mod_headers
%module_scripts mod_ident
%module_scripts mod_imagemap
%module_scripts mod_include
%module_scripts mod_info
%module_scripts mod_ldap
%module_scripts mod_log_config
%module_scripts mod_log_forensic
%module_scripts mod_logio
%module_scripts mod_mime
%module_scripts mod_mime_magic
%module_scripts mod_negotiation
%module_scripts mod_proxy
%module_scripts mod_rewrite
%module_scripts mod_setenvif
%module_scripts mod_speling
%module_scripts mod_ssl
%module_scripts mod_status
%module_scripts mod_unique_id
%module_scripts mod_userdir
%module_scripts mod_usertrack
%module_scripts mod_version
%module_scripts mod_vhost_alias
%module_scripts suexec

%post cgi_test
if [ "$1" = "1" ]; then
	%service -q httpd reload
fi

%postun cgi_test
if [ "$1" = "0" ]; then
	%service -q httpd reload
fi

%post errordocs
if [ "$1" = "1" ]; then
	%service -q httpd reload
fi

%postun errordocs
if [ "$1" = "0" ]; then
	%service -q httpd reload
fi

%files
%defattr(644,root,root,755)

%files base
%defattr(644,root,root,755)
%doc ABOUT_APACHE CHANGES README
%doc docs/conf/mime.types

%attr(754,root,root) /etc/rc.d/init.d/httpd

%attr(751,root,root) %dir %{_sysconfdir}
%{_sysconfdir}/modules
%{_sysconfdir}/run
%{_sysconfdir}/logs
%ghost %{_sysconfdir}/httpd.conf
%attr(750,root,root) %dir %{_sysconfdir}/conf.d
%attr(750,root,root) %dir %{_sysconfdir}/webapps.d
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_common.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mpm.conf
%attr(640,root,root) %{_sysconfdir}/magic
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/httpd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/monit/*.monitrc

%dir %{_libexecdir}

%attr(755,root,root) %{_sbindir}/checkgid
%attr(755,root,root) %{_sbindir}/httpd
%attr(755,root,root) %{_sbindir}/httpd.*

%dir %attr(770,root,http) /var/run/httpd
%dir %attr(770,root,http) /var/cache/httpd

%{_mandir}/man8/httpd.8*

%attr(2751,root,logs) %dir /var/log/httpd
%attr(2750,root,logs) %dir /var/log/archiv/httpd
%attr(640,root,logs) %ghost /var/log/httpd/*

%dir %{_datadir}

%dir %{_datadir}/cgi-bin
%dir %{_datadir}/html
%{_datadir}/icons

%files doc -f manual.files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_manual.conf

%files errordocs
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_errordocs.conf
%{_datadir}/error

%files suexec
%defattr(644,root,root,755)
%attr(4755,root,root) %{_sbindir}/suexec
%attr(755,root,root) %{_libexecdir}/mod_suexec.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_suexec.conf
%{_mandir}/man8/suexec.8*

%files index
%defattr(644,root,root,755)
%config(noreplace,missingok) %{_datadir}/html/index.html*
%{_datadir}/html/*.gif
%{_datadir}/html/*.png

%files apxs
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/apxs
%attr(755,root,root) %{_sbindir}/envvars*
# package libexecdir also to -apxs, as -apxs and -devel don't require -base package
%dir %{_libexecdir}
%dir %{_libexecdir}/build
%{_libexecdir}/build/config_vars.mk
%{_mandir}/man8/apxs.8*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ab
%attr(755,root,root) %{_sbindir}/apachectl
%attr(755,root,root) %{_sbindir}/htdigest
%attr(755,root,root) %{_sbindir}/logresolve
%attr(755,root,root) %{_sbindir}/rotatelogs
%{_mandir}/man8/ab.8*
%{_mandir}/man8/apachectl.8*
%{_mandir}/man1/htdigest.1*
%{_mandir}/man8/logresolve.8*
%{_mandir}/man8/rotatelogs.8*

%files devel
%defattr(644,root,root,755)
%{_includedir}
# FIXME: httpd.exp needed only on AIX
%{_libexecdir}/*.exp
%{_libexecdir}/build/[lprs]*.mk
%attr(755,root,root) %{_libexecdir}/build/*.sh

%files mod_actions
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_actions.conf
%attr(755,root,root) %{_libexecdir}/mod_actions.so

%files mod_alias
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_alias.conf
%attr(755,root,root) %{_libexecdir}/mod_alias.so

%files mod_asis
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_asis.conf
%attr(755,root,root) %{_libexecdir}/mod_asis.so

%files mod_auth
%defattr(644,root,root,755)

%files mod_auth_basic
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_auth_basic.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_basic.so

%files mod_auth_dbm
%defattr(644,root,root,755)

%files mod_auth_digest
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_auth_digest.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_digest.so

%files mod_authn_alias
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_alias.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_alias.so

%files mod_authn_anon
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_anon.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_anon.so

%files mod_authn_dbd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_dbd.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_dbd.so

%files mod_authn_dbm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_dbm.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_dbm.so

%files mod_authn_default
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_default.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_default.so

%files mod_authn_file
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authn_file.conf
%attr(755,root,root) %{_libexecdir}/mod_authn_file.so

%if %{with ldap}
%files mod_authnz_ldap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authnz_ldap.conf
%attr(755,root,root) %{_libexecdir}/mod_authnz_ldap.so
%endif

%files mod_authz_dbm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_dbm.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_dbm.so

%files mod_authz_default
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_default.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_default.so

%files mod_authz_groupfile
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_groupfile.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_groupfile.so

%files mod_authz_host
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_host.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_host.so

%files mod_authz_owner
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_owner.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_owner.so

%files mod_authz_user
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_authz_user.conf
%attr(755,root,root) %{_libexecdir}/mod_authz_user.so

%files mod_autoindex
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_autoindex.conf
%attr(755,root,root) %{_libexecdir}/mod_autoindex.so

%if %{with bucketeer}
%files mod_bucketeer
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_bucketeer.conf
%attr(755,root,root) %{_libexecdir}/mod_bucketeer.so
%endif

%files mod_cache
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_cache.conf
%attr(755,root,root) %{_sbindir}/htcacheclean
%attr(755,root,root) %{_libexecdir}/mod_cache.so
%attr(755,root,root) %{_libexecdir}/mod_disk_cache.so
%attr(755,root,root) %{_libexecdir}/mod_mem_cache.so
%{_mandir}/man8/htcacheclean.8*

%files mod_case_filter
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_case_filter.conf
%attr(755,root,root) %{_libexecdir}/mod_case_filter.so

%files mod_case_filter_in
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_case_filter_in.conf
%attr(755,root,root) %{_libexecdir}/mod_case_filter_in.so

%files mod_cern_meta
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_cern_meta.conf
%attr(755,root,root) %{_libexecdir}/mod_cern_meta.so

%files mod_cgi
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_cgi.conf
%attr(755,root,root) %{_libexecdir}/mod_cgi.so

%files mod_cgid
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_cgid.conf
%attr(755,root,root) %{_libexecdir}/mod_cgid.so

%files mod_charset_lite
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_charset_lite.conf
%attr(755,root,root) %{_libexecdir}/mod_charset_lite.so

%files mod_dav
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_dav.conf
%attr(755,root,root) %{_libexecdir}/mod_dav*.so
%dir %attr(770,root,http) /var/lock/mod_dav

%files mod_dbd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_dbd.conf
%attr(755,root,root) %{_libexecdir}/mod_dbd.so

%files mod_deflate
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_deflate.conf
%attr(755,root,root) %{_libexecdir}/mod_deflate.so

%files mod_dir
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_dir.conf
%attr(755,root,root) %{_libexecdir}/mod_dir.so

%files mod_dumpio
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_dumpio.conf
%attr(755,root,root) %{_libexecdir}/mod_dumpio.so

%files mod_echo
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_echo.conf
%attr(755,root,root) %{_libexecdir}/mod_echo.so

%files mod_env
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_env.conf
%attr(755,root,root) %{_libexecdir}/mod_env.so

%files mod_expires
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_expires.conf
%attr(755,root,root) %{_libexecdir}/mod_expires.so

%files mod_ext_filter
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_ext_filter.conf
%attr(755,root,root) %{_libexecdir}/mod_ext_filter.so

%files mod_file_cache
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_file_cache.conf
%attr(755,root,root) %{_libexecdir}/mod_file_cache.so

%files mod_filter
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_filter.conf
%attr(755,root,root) %{_libexecdir}/mod_filter.so

%files mod_headers
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_headers.conf
%attr(755,root,root) %{_libexecdir}/mod_headers.so

%files mod_ident
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_ident.conf
%attr(755,root,root) %{_libexecdir}/mod_ident.so

%files mod_imagemap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_imagemap.conf
%attr(755,root,root) %{_libexecdir}/mod_imagemap.so

%files mod_include
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_include.conf
%attr(755,root,root) %{_libexecdir}/mod_include.so

%files mod_info
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_info.conf
%attr(755,root,root) %{_libexecdir}/mod_info.so

%if %{with ldap}
%files mod_ldap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_ldap.conf
%attr(755,root,root) %{_libexecdir}/mod_ldap.so
%endif

%files mod_log_config
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_log_config.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_log_config.conf

%files mod_log_forensic
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_log_forensic.conf
%attr(755,root,root) %{_libexecdir}/mod_log_forensic.so

%files mod_logio
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_logio.conf
%attr(755,root,root) %{_libexecdir}/mod_logio.so

%files mod_mime
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_mime.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_mime.conf

%files mod_mime_magic
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_mime_magic.conf
%attr(755,root,root) %{_libexecdir}/mod_mime_magic.so

%files mod_negotiation
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_negotiation.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_languages.conf
%attr(755,root,root) %{_libexecdir}/mod_negotiation.so

%files mod_proxy
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_proxy.conf
%attr(755,root,root) %{_libexecdir}/mod_proxy*.so

%files mod_rewrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/httxt2dbm
%attr(755,root,root) %{_libexecdir}/mod_rewrite.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_rewrite.conf

%files mod_setenvif
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_setenvif.conf
%attr(755,root,root) %{_libexecdir}/mod_setenvif.so

%files mod_speling
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_speling.conf
%attr(755,root,root) %{_libexecdir}/mod_speling.so

%if %{with ssl}
%files mod_ssl
%defattr(644,root,root,755)
%attr(750,root,root) %dir %{_sysconfdir}/ssl
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ssl/server.*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_ssl.conf
%attr(755,root,root) %{_libexecdir}/mod_ssl.so
%endif

%files mod_status
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_status.conf
%attr(755,root,root) %{_libexecdir}/mod_status.so

%files mod_unique_id
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_unique_id.conf
%attr(755,root,root) %{_libexecdir}/mod_unique_id.so

%files mod_userdir
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_userdir.conf
%attr(755,root,root) %{_libexecdir}/mod_userdir.so

%files mod_usertrack
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_usertrack.conf
%attr(755,root,root) %{_libexecdir}/mod_usertrack.so

%files mod_version
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_version.conf
%attr(755,root,root) %{_libexecdir}/mod_version.so

%files mod_vhost_alias
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/mod_vhost_alias.so
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_vhost_alias.conf

%files -n htpasswd-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/htpasswd
%attr(755,root,root) %{_sbindir}/htpasswd
%{_mandir}/man1/htpasswd.1*

%files dbmtools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/dbmmanage
%attr(755,root,root) %{_sbindir}/htdbm
%{_mandir}/man1/dbmmanage.1*
%{_mandir}/man1/htdbm.1*

%files cgi_test
%defattr(644,root,root,755)
%dir %{_cgibindir}
%attr(755,root,root) %{_cgibindir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_cgi_test.conf
