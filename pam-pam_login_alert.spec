Summary:	A module that informs admin about logins into system
Summary(pl):	Modu³ informuj±cy administratora o logowaniu do systemu
Name:		pam-pam_login_alert
Version:	0.10
Release:	1
Epoch:		0
License:	GPL
Vendor:		Dustin Puryear <dpuryear@usa.net>
Group:		Applications/System
Source0:	http://www.kernel.org/pub/linux/libs/pam/pre/modules/pam_login_alert-%{version}.tar.bz2
# Source0-md5:	55591c36291247977fd7e1e824191f05
URL:		http://www.kernel.org/pub/linux/libs/pam/pre/modules/
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alert an administrator via email and/or syslog when a given user(s)
accesses the system. Useful primarily when monitoring user activity
and access.

%description -l pl
Modu³ informuj±cy administratora poczt± elektroniczn± lub przez
sysloga o logowaniu do systemu wybranych u¿ytkowników. Przydatny
podczas ¶ledzenia aktywno¶ci u¿ytkowników.

%prep
%setup -q -c -n pam_login_alert-%{version}

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/security,lib/security} \
	   $RPM_BUILD_ROOT%{_mandir}/man8

install pam_login_alert.so $RPM_BUILD_ROOT/lib/security
install login_alert.conf $RPM_BUILD_ROOT%{_sysconfdir}/security/login_alert.conf
install login_alert.users $RPM_BUILD_ROOT%{_sysconfdir}/security/login_alert.users
install pam_login_alert.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) /lib/security/pam_login_alert.so
%{_mandir}/man8/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/security/login_alert.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/security/login_alert.users
