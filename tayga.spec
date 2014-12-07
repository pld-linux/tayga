# TODO:
# - tigervnc.init
Summary:	A NAT64 daemon
Name:		tayga
Version:	0.9.2
Release:	1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://www.litech.org/tayga/%{name}-%{version}.tar.bz2
# Source0-md5:	7a7b24165ce008df772f398d86fa280e
URL:		http://www.litech.org/tayga/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TAYGA is an out-of-kernel stateless NAT64 implementation for Linux
that uses the TUN driver to exchange IPv4 and IPv6 packets with the
kernel. It is intended to provide production-quality NAT64 service for
networks where dedicated NAT64 hardware would be overkill.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_sysconfdir}/tayga.conf{.example,}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tayga.conf
%attr(755,root,root) %{_sbindir}/tayga
%{_mandir}/man5/tayga.conf.5*
%{_mandir}/man8/tayga.8*
