Summary:	GUI to browse and search Zeitgeist activities
Name:		gnome-activity-journal
Version:	0.8.0
Release:	0.1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://launchpad.net/gnome-activity-journal/0.8/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	46e493f090b41a49cfce422203791bc0
URL:		http://launchpad.net/gnome-activity-journal
BuildRequires:	python
BuildRequires:	python-distutils-extra
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,preun):	GConf2
Requires:	hicolor-icon-theme
Requires:	python-PIL
Requires:	python-chardet
Requires:	python-dbus
Requires:	python-gnome-gconf
Requires:	python-gnome-ui
Requires:	python-gstreamer
Requires:	python-pygments
Requires:	python-pygobject
Requires:	python-pygtk-gtk
Requires:	python-pyxdg
Requires:	zeitgeist
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Activity Journal (formerly known as GNOME Zeitgeist) is a tool
for easily browsing and finding files on your computer. It keeps a
chronological journal of all file activity and supports tagging and
establishing relationships between groups of files.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT{%{_datadir},%{_sysconfdir}}/gconf/schemas/gnome-activity-journal.schemas

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%gconf_schema_install gnome-activity-journal.schemas

%preun
%gconf_schema_uninstall gnome-activity-journal.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-activity-journal
%{_datadir}/gnome-activity-journal
%{_desktopdir}/gnome-activity-journal.desktop
%{_mandir}/man1/gnome-activity-journal.1*
%{_pixmapsdir}/gnome-activity-journal.xpm
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{py_sitescriptdir}/gnome_activity_journal-*.egg-info
%{_sysconfdir}/gconf/schemas/gnome-activity-journal.schemas
%{_datadir}/zeitgeist/_zeitgeist/engine/extensions/gnome_activity_journal.py
