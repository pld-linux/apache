Summary:	HTTP server daemon to provide WWW services with IPv6 support
Summary(de):	Leading World Wide Web-Server
Summary(fr):	Serveur Web leader du marché
Summary(pl):	Serwer WWW (World Wide Web) ze wsparciem dla IPv6
Summary(tr):	Lider WWW tarayýcý
Name:		apache
Version:	1.3.6
Release:	1
Group:		Networking/Daemons
Group(pl):	Sieci/Demony
Source0:	ftp://ftp.apache.org/apache/dist/%{name}_%{version}.tar.gz
Source1:	apache.init
Source2:	%{name}.logrotate
Source3:	%{name}-extra.tar.bz2
########	http://stonecold.unity.ncsu.edu/software/mod_auth_kerb/index.html
Source5:	mod_auth_kerb-4.3.tar.gz
Source6:	apache_1.3.6.tar.gz.asc
Source7:	apache_1.3.6.tar.gz.md5
Patch0:		%{name}-suexec.patch
Patch1:		%{name}_1.3.6.ipv6.patch
Copyright:	BSD-like
Obsoletes:	apache-extra
Obsoletes:	apache6
Provides:	httpd
Provides:	webserver
Prereq:		/sbin/chkconfig
URL:		http://www.apache.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Apache is a full featured web server that is freely available, and also
happens to be the most widely used. This version supports IPv6.

%description -l de
Apache ist ein voll funktionsfähiger Web-Server, der kostenlos
erhältlich und weit verbreitet ist.

%description -l fr
Apache est un serveur Web complet, disponible librement, et se trouve être
aussi le plus utilisé à travers le monde.

%description -l pl
Apache jest serwerem WWW (World Wide Web). Instaluj±c ten pakiet bêdziesz 
móg³ prezentowaæ w³asne strony WWW w sieci internet. Apache umo¿liwia równie¿
konfigurowanie serwerów wirtualnych. Ta wersja wspiera IPv6.

%description -l tr
Apache serbest daðýtýlan ve çok kullanýlan yetenekli bir web sunucusudur.

%package suexec
Summary:	Apache suexec wrapper
Summary(pl):	Suexec wrapper do serwera www Apache
Group:		Networking/Development
Group(pl):	Sieci/Programowanie
Requires:	%{name} = %{version}

%description suexec
The suEXEC feature provides Apache users the ability to run CGI and SSI
programs under user IDs different from the user ID of the calling web-server.
Normally, when a CGI or SSI program executes, it runs as the same user 
who is running the web server. 

%description -l pl suexec
SuEXEC umo¿liwia serwerowi Apache uruchamianie programów CGI i SSI z innym
UID ni¿ wywo³uj±cy je serwer. Normalnie programy CGI i SSI s± wykonywane
jako taki sam u¿ytkownik jak serwer WWW.

%package devel
Summary:	Apache include files
Summary(pl):	Pliki nag³ówkowe do serwera www Apache
Group:		Networking/Development
Group(pl):	Sieci/Programowanie
Requires:	%{name} = %{version}

%description devel
Apache include files.

%description -l pl devel
Pliki nag³ówkowe dla serwera WWW Apache.

%package doc
Summary:	Apache dokumentation
Summary(pl):	Dokumentacja do Apache
Group:		Documentation
Group(pl):	Dokumentacja
Requires:	%{name} = %{version}
URL:		http://www.apache.org/

%description doc
Documentation for apache in HTML format.

%description -l pl doc
Dokumentacja do Apache w formacie HTML

%prep 
%setup -q -n apache_%{version} -a3
%patch0 -p1
%patch1 -p1

%build
OPTIM=$RPM_OPT_FLAGS LDFLAGS=-s\
    ./configure \
	--prefix=/usr \
	--sysconfdir=/etc/httpd/conf \
	--datadir=/home/httpd \
	--libexecdir=/usr/libexec/apache \
	--localstatedir=/var \
	--runtimedir=/var/run \
	--logfiledir=/var/log/httpd \
	--without-confadjust \
	--enable-module=all \
	--enable-shared=max \
	--disable-module=auth_db \
	--proxycachedir=/var/spool/proxy \
	--with-perl=%{_bindir}/perl \
	--enable-suexec \
	--suexec-caller=http \
	--suexec-uidmin=500 \
	--suexec-gidmin=500 \
	--sbindir=%{_sbindir} \
	--includedir=%{_includedir}/apache \
	--enable-rule=INET6

make

%install
rm -rf $RPM_BUILD_ROOT

make install-quiet root="$RPM_BUILD_ROOT"

mv $RPM_BUILD_ROOT/home/httpd/htdocs $RPM_BUILD_ROOT/home/httpd/html

install -d $RPM_BUILD_ROOT/etc/{httpd/conf,logrotate.d,rc.d/init.d}
install -d $RPM_BUILD_ROOT/home/httpd/{html/manual,icons,cgi-bin}
install -d $RPM_BUILD_ROOT/{usr/{lib/apache,sbin,man/man{1,8}},var/log/httpd}

install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/apache
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/httpd

install -d $RPM_BUILD_ROOT%{_includedir}/apache

rm -f $RPM_BUILD_ROOT/etc/httpd/conf/*
rm -f $RPM_BUILD_ROOT/home/httpd/html/manual/expand.pl

touch $RPM_BUILD_ROOT/var/log/httpd/{access,error}_log

mv -f apache-extra/errordocs	$RPM_BUILD_ROOT/home/httpd/
cp -a apache-extra/icons/*	$RPM_BUILD_ROOT/home/httpd/icons
cp -a apache-extra/*.conf	$RPM_BUILD_ROOT/etc/httpd/conf
cp -a apache-extra/m*		$RPM_BUILD_ROOT/etc/httpd/conf

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{man1/*,man8/*}
gzip -9nf ABOUT_APACHE src/CHANGES KEYS README

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add httpd

%preun
if [ $1 = 0 ]; then
   if [ -f /var/lock/subsys/httpd ]; then
       /etc/rc.d/init.d/httpd stop >&2
   fi
   /sbin/chkconfig --del httpd
fi

%files
%defattr(644,root,root,755)
%doc ABOUT_APACHE.gz src/CHANGES.gz KEYS.gz README.gz
%doc conf/mime.types

%attr(750,root,root) %dir /etc/httpd
%attr(750,root,root) %dir /etc/httpd/conf
%attr(640,root,root) %config %verify(not size mtime md5) /etc/httpd/conf/*

%attr(640,root,root) %config /etc/logrotate.d/*
%attr(755,root,root) %dir /home/httpd/html

%config(noreplace) /home/httpd/html/index.html

%attr(644,root,root) /home/httpd/html/*.gif
%attr(700,root,root) %config %verify(not size mtime md5) /etc/rc.d/init.d/*

%attr(755,root,root,755) /home/httpd/cgi-bin
%attr(755,root,root,755) /usr/libexec/apache

%attr(755,root,root,755) %dir /home/httpd/icons
/home/httpd/icons/*.gif

%attr(755,root,root,755) %dir /home/httpd/errordocs
/home/httpd/errordocs/*

%attr(755,root,root) %{_bindir}/dbmmanage 
%attr(755,root,root) %{_bindir}/htdigest
%attr(755,root,root) %{_bindir}/htpasswd

%attr(755,root,root) %{_sbindir}/ab
%attr(755,root,root) %{_sbindir}/apachectl
%attr(755,root,root) %{_sbindir}/apxs
%attr(755,root,root) %{_sbindir}/httpd
%attr(755,root,root) %{_sbindir}/logresolve
%attr(755,root,root) %{_sbindir}/rotatelogs

%{_mandir}/man[18]/*

%attr(750,root,root) %dir /var/log/httpd
%attr(640,root,root) %config %verify(not size mtime md5) /var/log/httpd/*

%files suexec
%attr(4711,root,root) %{_sbindir}/suexec

%files devel
%defattr(644,root,root,755) 

%dir %{_includedir}/apache
%{_includedir}/apache/*

%files doc
%defattr(644,root,root,755)
/home/httpd/html/manual

%changelog
* Thu Feb 10 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [1.3.4-6d]
- added LDFLAGS=-s
- gzipping instead bzipping
- cosmetic changes

* Tue Jan 26 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.4-5d]
- rebuild against new kernel-2.2.0 ;)  

* Mon Jan 25 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.4-4d]
- added errordocs.  

* Thu Jan 21 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.4-3d]
- fixed files permission,
- fixed apache.init,
- some other changes.

* Sun Jan 17 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.4-2d]
- fixed sbindir && apache includes (by Mirek Nowakowski <nowam@pg.gda.pl>),
- compressed documentation,
- fixed Group(pl).

* Wed Nov 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3.3-1]
- removed making symlinks in /etc/rc.d/rc?.d and in %install also
  removed this symlinks from %files (/etc/rc.d/init.d/httpd suports
  chkconfig),
- more simplifications in %install,
- added new apache-config.patch,
- added "%ghost /var/log/httpd/suexec_log" for suexec subpackage,
- added "Requires: setup >= 1.10.0" for proper install in enviroment with
  http user/group.

* Wed Oct 14 1998 Konrad Stêpieñ <konrad@interdata.com.pl>
  [1.3.3-1d]
- up to 1.3.3
- changed user/group to http
- added patch against GNU libc-2.1, 
  prepared by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- enabled all modules (without auth_db ....)
- added magic (for mod_mime_magic)
- rebuild spec file to minimize number of patches
- suEXEC in separated package

* Wed Oct 14 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.2-1d]
- build against Tornado (GNU libc-2.1),
- minor changes. 

* Fri Sep 25 1998 Konrad Stêpieñ <konrad@interdata.com.pl>
  [1.3.2-1]
- up to 1.3.2
- reconfig to use /etc/mime.types (again)
  orginal mime.types can be found in documentation directory
- changed to user/group httpd
- restore orginal start page
- documentation in separate package
- added "Provides:httpd"

* Thu Sep  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3.1-2]
- removed /home/httpd/icons/README
- added devel subpackage,
- added pl translation (Wojtek ¦lusarczyk <wojtek@shadow.eu.org>),
- removed Serial: filed,
- removed Packager: field (this must be placed in private ~/.rpmrc),
- simplification in %files and %install,
- /home/httpd/html/manual is now marked as %doc,
- added /etc/rc.d/rc*.d/* symlinks as a %config(missingok),
- changed permidssion on logrotate config file to 600,
- changed permidssion on /var/log/httpd to 700,
- added %ghost /var/log/httpd/*
- added striping modules.
- added patch to defeat header dos attack

* Sat Jul 18 1998 Manoj Kasichainula <manojk@io.com>
  [1.3.1-1]
  some of the changes from 1.3.0-1 (mine was done independantly, so there are
  probably other changes)
- /etc/rc.d/init.d/httpd includes reload
- logrotate doesn't kill all httpd processes, just one. This is recommended.
- Doesn't uses Red Hat MIME typesm since RH mime.types doesn't include .htm,
  and there are other differences which will probably just cause lots of
  annoying bug reports
- Don't change ServerAdmin (this fake address is on purpose according
  to the Apache Group)
- don't enable mod_auth_dbm, since it can supposedly conflict with
  mod_auth_db

* Sun May 31 1998 Manoj Kasichainula <manojk@io.com>
  [1.3b8_dev-1]
- Updated to 1.3b8_dev
- Deleted some patchwork because of improvements in APACI
- Added translations from RH 5.1 Apache RPM
- Loosened permissions to match RH 5.1 Apache RPM in /home
- Allow index.htm
- Collapsed doc package into main package (partly inspired by RPM bug)

* Fri May 22 1998 Manoj Kasichainula <manojk@io.com>
  [1.3b7-0]
- Upgraded to 1.3b7
- Uses APACI configuration interface -- radical rewrite
- No more apache-extra, at least for now
- more descriptive Copyright field
- Now builds suEXEC
- Explicitly decided not to use built-in mime.types, but included patch to do
  so

* Thu Apr 16 1998 Manoj Kasichainula <manojk@io.com>
  [1.3b6-4]
- Upgraded to 1.3b6
- Split perl path patch from other config (saves a little time when upgrading
  packages)
- Started the process of separating out shared modules. So far, only the proxy
  module has been done.
- Yeah, I'm aware of 1.3b6-3 RPM in contrib. It has problems that I would
  discuss with the packager if I could find out who that was.

* Thu Mar 5 1998 Manoj Kasichainula <manojk@io.com>

- Upgraded to 1.3b5
- Buildable by non-root

* Fri Jan 2 1998 Manoj Kasichainula <manojk@io.com>

- Includes changes from Red Hat 5.0's Apache release
  - added patch for backslash DoS attach
  - made the default index.html be config(noreplace) so we no longer
    blow away other folks' index.html
  - added chkconfig support
  - added restart|status options to initscript
  - renamed httpd.init to httpd
  - New index.html
  - Now uses Red Hat's mime.types file (I may change my mind on this)
  - No longer keeps an agent and referer log.
  - Much more
- Upgraded to 1.3b3
- Fixed sillyness in /etc/rc.d/init.d/httpd
- Now require recent version of initscripts with killproc fix.
- Changed logrotate script
- Undid Red Hat's ServerAdmin change (Red Hat's choice results in a
  seemingly valid but nonsensical address)
- suexec moved to /home/httpd/sbin/suexec
- Replaced a reference to apache_pb.gif to /icons/apache_pb.gif, to save a
  bit of space)

* Thu Oct 16 1997 Manoj Kasichainula <manojk@io.com>
- Upgraded to 1.3b2
- MaxRequestsPerChild upped to 10000
- apache-suexec absorbed into apache
- Uncommented Serial: line. Now, it requires a recent version of RPM
