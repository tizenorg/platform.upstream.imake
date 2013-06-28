Name:           imake
Version:        1.0.5
Release:        0
License:        MIT
Summary:        C preprocessor interface to the make utility
Url:            http://xorg.freedesktop.org/
Group:          Development/Tools/Building
Source:         %{name}-%{version}.tar.bz2
Source1001: 	imake.manifest
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)
# This was part of the xorg-x11-util-devel package up to version 7.6
Requires:       xorg-cf-files

%description
Imake is used to generate Makefiles from a template, a set of cpp macro
functions, and a per-directory input file called an Imakefile.

The X Window System used imake extensively up through the X11R6.9
release, for both full builds within the source tree and external
software. X has since moved to GNU autoconf and automake for its build
system in X11R7.0 and later releases, but still maintains imake for
building existing external software programs that have not yet
converted.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --with-config-dir=%{_datadir}/X11/config
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/ccmakedep
%{_bindir}/cleanlinks
%{_bindir}/imake
%{_bindir}/makeg
%{_bindir}/mergelib
%{_bindir}/mkdirhier
%{_bindir}/mkhtmlindex
%{_bindir}/revpath
%{_bindir}/xmkmf

%docs_package

%changelog
